"""
Genera los diagramas entidad-relación de MATU leyendo el catálogo de PostgreSQL.
Así los diagramas no pueden desalinearse del esquema: salen de él.

    python gen_diagramas.py  ->  escribe diagramas/*.mmd
"""
import os
import pathlib

import psycopg

DSN = os.environ.get("MATU_TEST_DSN", "host=/tmp port=5433 user=postgres dbname=matu")
SALIDA = pathlib.Path(__file__).resolve().parents[2] / "docs" / "diagramas" / "modelo-datos"

TIPOS = {
    "uuid": "uuid", "text": "text", "boolean": "bool", "integer": "int", "bigint": "bigint",
    "smallint": "smallint", "timestamp with time zone": "timestamptz", "date": "date",
    "bytea": "bytea", "jsonb": "jsonb", "numeric": "numeric", "ARRAY": "text_array",
    "daterange": "daterange", "tstzrange": "tstzrange", "inet": "inet",
    "time without time zone": "time", "character": "char",
}

# (archivo, título, tablas con detalle, tablas de contexto solo con su clave)
GRUPOS = [
    ("02-er-identidad-y-grupo", "Identidad, grupo familiar y consentimiento",
     ["usuario", "indice_credencial", "dispositivo", "sesion_refresh", "grupo_familiar", "membresia",
      "invitacion", "direccion", "persona_cuidada", "consentimiento"], []),
    ("03-er-capa1-plan-de-cuidado", "Capa 1 · Plan de cuidado, cifrado y relevo",
     ["clave_datos", "plan_cuidado", "plan_seccion", "acceso_relevo"],
     ["persona_cuidada", "grupo_familiar", "usuario"]),
    ("04-er-capa2-consumo", "Capa 2 · Perfil de consumo, reposiciones y alertas",
     ["perfil_consumo", "reposicion", "alerta_quiebre"], ["persona_cuidada", "producto", "grupo_familiar"]),
    ("05-er-catalogo", "Capa 3 · Catálogo, comercios y convenios",
     ["categoria_cuidado", "producto", "comercio", "usuario_comercio", "convenio", "oferta"], ["usuario"]),
    ("06-er-pedido-y-reposicion", "Capa 3 · Pedido, sustitución y reposición programada",
     ["pedido", "pedido_entrega", "pedido_linea", "regla_sustitucion", "pedido_transicion",
      "plan_reposicion", "plan_reposicion_linea", "ocurrencia"],
     ["oferta", "producto", "comercio", "persona_cuidada", "perfil_consumo"]),
    ("07-er-pagos", "Capa 3 · Cargo, pago dividido y pasarela",
     ["cargo", "participacion", "transaccion_pasarela", "medio_pago_inscrito"], ["pedido", "usuario"]),
    ("08-er-cumplimiento-y-liquidacion", "Capa 3 · Cumplimiento y liquidación al comercio",
     ["repartidor", "oferta_asignacion", "asignacion", "evidencia", "consumo_comercio", "liquidacion"],
     ["pedido", "comercio", "usuario"]),
    ("09-er-transversales", "Transversales · auditoría, outbox, idempotencia, notificaciones e incidencias",
     ["auditoria", "evento_outbox", "evento_consumido", "idempotencia", "indice_token",
      "notificacion", "preferencia_notificacion", "incidencia"], ["usuario", "grupo_familiar", "pedido"]),
]


def leer_catalogo(cx):
    columnas = {}
    for t, c, tipo, nulo in cx.execute("""
        SELECT table_name, column_name, data_type, is_nullable
        FROM information_schema.columns WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position"""):
        columnas.setdefault(t, []).append((c, TIPOS.get(tipo, tipo.replace(" ", "_")), nulo == "YES"))
    pk, uk = set(), set()
    # Solo restricciones de una columna: una UNIQUE compuesta no hace única a cada columna
    for t, c, kind in cx.execute("""
        SELECT cl.relname, a.attname, co.contype
        FROM pg_constraint co
        JOIN pg_class cl ON cl.oid = co.conrelid
        JOIN pg_namespace n ON n.oid = cl.relnamespace
        JOIN pg_attribute a ON a.attrelid = co.conrelid AND a.attnum = co.conkey[1]
        WHERE n.nspname = 'public' AND co.contype IN ('p', 'u') AND cardinality(co.conkey) = 1"""):
        (pk if kind == "p" else uk).add((t, c))
    fks = cx.execute("""
        SELECT cl.relname, a.attname, rcl.relname
        FROM pg_constraint co
        JOIN pg_class cl  ON cl.oid = co.conrelid
        JOIN pg_class rcl ON rcl.oid = co.confrelid
        JOIN pg_namespace n ON n.oid = cl.relnamespace
        JOIN pg_attribute a ON a.attrelid = co.conrelid AND a.attnum = co.conkey[1]
        WHERE co.contype = 'f' AND n.nspname = 'public'
        ORDER BY 1, 2""").fetchall()
    return columnas, pk, uk, fks


def entidad(nombre, columnas, pk, uk, fks, detalle=True):
    fk_cols = {(t, c) for t, c, _ in fks}
    lineas = [f"    {nombre} {{"]
    for c, tipo, nulo in columnas[nombre]:
        if not detalle and (nombre, c) not in pk:
            continue
        marcas = [m for m, ok in (("PK", (nombre, c) in pk), ("FK", (nombre, c) in fk_cols),
                                  ("UK", (nombre, c) in uk and (nombre, c) not in pk)) if ok]
        marca = " " + ", ".join(marcas) if marcas else ""
        nota = ' "opcional"' if nulo and detalle else ""
        lineas.append(f"        {tipo} {c}{marca}{nota}")
    lineas.append("    }")
    return "\n".join(lineas)


def relaciones(tablas, fks, uk, pk):
    out = []
    for hija, col, padre in fks:
        if hija in tablas and padre in tablas:
            unica = (hija, col) in uk or (hija, col) in pk
            card = "||--o|" if unica else "||--o{"
            out.append(f'    {padre} {card} {hija} : "{col}"')
    return out


def main():
    SALIDA.mkdir(exist_ok=True)
    with psycopg.connect(DSN) as cx:
        columnas, pk, uk, fks = leer_catalogo(cx)

    # Vista general: todas las tablas, sin atributos
    todas = sorted(columnas)
    general = ["---", "title: MATU · Modelo de datos completo (vista general)", "---", "erDiagram"]
    # En la vista general se omiten las referencias de autoría (creado_por, actualizado_por...)
    # hacia usuario: son decenas de líneas que no explican la estructura y la vuelven ilegible.
    autoria = {"creado_por", "actualizado_por", "registrada_por", "otorgado_por", "invitado_por",
               "aceptada_por", "asignada_a", "creada_por", "respaldo_usuario_id"}
    general += relaciones(set(todas), [f for f in fks if f[1] not in autoria], uk, pk)
    sueltas = [t for t in todas if not any(t in (h, p) for h, _, p in fks)]
    general += [f"    {t} {{\n        uuid id\n    }}" if "id" in dict((c, 1) for c, *_ in columnas[t])
                else f"    {t} {{\n        text clave\n    }}" for t in sueltas]
    (SALIDA / "01-er-vista-general.mmd").write_text("\n".join(general) + "\n", encoding="utf-8")

    for archivo, titulo, foco, contexto in GRUPOS:
        tablas = set(foco) | set(contexto)
        partes = ["---", f"title: MATU · {titulo}", "---", "erDiagram"]
        partes += relaciones(tablas, fks, uk, pk)
        partes += [entidad(t, columnas, pk, uk, fks, detalle=True) for t in foco]
        partes += [entidad(t, columnas, pk, uk, fks, detalle=False) for t in contexto]
        (SALIDA / f"{archivo}.mmd").write_text("\n".join(partes) + "\n", encoding="utf-8")
    print(f"{len(GRUPOS) + 1} diagramas ER escritos en {SALIDA}")


if __name__ == "__main__":
    main()
