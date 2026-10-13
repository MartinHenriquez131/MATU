"""
MATU · Pruebas de aislamiento del modelo de datos contra PostgreSQL real.

Prototipo de backend/tests/test_aislamiento.py (arquitectura, sección 7.7 y 12.5).
Requiere una base recién migrada con db/00_roles.sql a db/03_permisos.sql.

    MATU_TEST_DSN="host=/tmp port=5433 user=postgres dbname=matu" pytest -q tests/

La conexión es de superusuario solo para sembrar datos. Cada verificación corre
con SET ROLE matu_app (o el rol que corresponda), que NO evade RLS.
"""
import os
import uuid

import psycopg
import pytest
from psycopg import errors

DSN = os.environ.get("MATU_TEST_DSN", "host=/tmp port=5433 user=postgres dbname=matu")

# Identificadores fijos para leer las pruebas con facilidad
U_ADMIN_A, U_OBS_A, U_PAG_A, U_PAG2_A = (uuid.UUID(f"00000000-0000-0000-0000-0000000000a{i}") for i in (1, 2, 3, 4))
U_ADMIN_B = uuid.UUID("00000000-0000-0000-0000-0000000000b1")
U_ENC = uuid.UUID("00000000-0000-0000-0000-0000000000c1")
U_REP = uuid.UUID("00000000-0000-0000-0000-0000000000d1")
U_NUEVO = uuid.UUID("00000000-0000-0000-0000-0000000000e1")
G_A = uuid.UUID("00000000-0000-0000-0000-00000000000a")
G_B = uuid.UUID("00000000-0000-0000-0000-00000000000b")
P_A = uuid.UUID("00000000-0000-0000-0000-0000000001a0")
P_B = uuid.UUID("00000000-0000-0000-0000-0000000001b0")
PLAN_A = uuid.UUID("00000000-0000-0000-0000-0000000002a0")
PLAN_B = uuid.UUID("00000000-0000-0000-0000-0000000002b0")
ACC_VIGENTE = uuid.UUID("00000000-0000-0000-0000-0000000003a1")
ACC_VENCIDO = uuid.UUID("00000000-0000-0000-0000-0000000003a2")
ACC_REVOCADO = uuid.UUID("00000000-0000-0000-0000-0000000003a3")
COMERCIO = uuid.UUID("00000000-0000-0000-0000-0000000004c1")
REPARTIDOR = uuid.UUID("00000000-0000-0000-0000-0000000005d1")
PED_A_ENVIADO = uuid.UUID("00000000-0000-0000-0000-0000000006a1")
PED_A_BORRADOR = uuid.UUID("00000000-0000-0000-0000-0000000006a2")
PED_B_ENVIADO = uuid.UUID("00000000-0000-0000-0000-0000000006b1")

INFRA_SIN_RLS = {"evento_outbox", "evento_consumido", "indice_token", "indice_credencial"}
REFERENCIA_PUBLICA = {"categoria_cuidado", "producto", "oferta", "comercio"}

SEMILLA = f"""
TRUNCATE usuario, grupo_familiar, comercio, categoria_cuidado, evento_outbox, evento_consumido,
         indice_token, auditoria RESTART IDENTITY CASCADE;
INSERT INTO usuario (id, email, nombre, password_hash) VALUES
 ('{U_ADMIN_A}', 'admin.a@x.cl', 'Admin A', 'h'), ('{U_OBS_A}', 'obs.a@x.cl', 'Obs A', 'h'),
 ('{U_PAG_A}', 'pag.a@x.cl', 'Pag A', 'h'),       ('{U_PAG2_A}', 'pag2.a@x.cl', 'Pag2 A', 'h'),
 ('{U_ADMIN_B}', 'admin.b@x.cl', 'Admin B', 'h'), ('{U_ENC}', 'enc@comercio.cl', 'Encargado', 'h'),
 ('{U_REP}', 'rep@x.cl', 'Repartidor', 'h'),      ('{U_NUEVO}', 'nuevo@x.cl', 'Nuevo', 'h');
INSERT INTO grupo_familiar (id, nombre, creado_por) VALUES
 ('{G_A}', 'Familia A', '{U_ADMIN_A}'), ('{G_B}', 'Familia B', '{U_ADMIN_B}');
INSERT INTO membresia (grupo_id, usuario_id, rol, puede_ver_plan) VALUES
 ('{G_A}', '{U_ADMIN_A}', 'admin', false), ('{G_A}', '{U_OBS_A}', 'observador', false),
 ('{G_A}', '{U_PAG_A}', 'pagador', false),  ('{G_A}', '{U_PAG2_A}', 'pagador', true),
 ('{G_B}', '{U_ADMIN_B}', 'admin', false);
INSERT INTO direccion (id, grupo_id, calle, numero, comuna) VALUES
 ('00000000-0000-0000-0000-00000000d1a0', '{G_A}', 'Los Aromos', '123', 'La Reina');
INSERT INTO persona_cuidada (id, grupo_id, nombre, nombre_pila, nivel_apoyo, direccion_entrega_id) VALUES
 ('{P_A}', '{G_A}', 'María Soto', 'María', 'apoyo_total', '00000000-0000-0000-0000-00000000d1a0'),
 ('{P_B}', '{G_B}', 'Luis Pérez', 'Luis', 'apoyo_parcial', NULL);
INSERT INTO clave_datos (grupo_id, persona_cuidada_id, dek_cifrada_con_kek, kek_version) VALUES
 ('{G_A}', '{P_A}', '\\x01', 1), ('{G_B}', '{P_B}', '\\x02', 1);
INSERT INTO plan_cuidado (id, grupo_id, persona_cuidada_id) VALUES
 ('{PLAN_A}', '{G_A}', '{P_A}'), ('{PLAN_B}', '{G_B}', '{P_B}');
INSERT INTO plan_seccion (plan_id, tipo, contenido_cifrado, nonce, tag_auth, kek_version) VALUES
 ('{PLAN_A}', 'rutina',             '\\xaa', '\\x000000000000000000000001', '\\x00000000000000000000000000000000', 1),
 ('{PLAN_A}', 'manejo_situaciones', '\\xaa', '\\x000000000000000000000002', '\\x00000000000000000000000000000000', 1),
 ('{PLAN_A}', 'red_apoyo',          '\\xaa', '\\x000000000000000000000003', '\\x00000000000000000000000000000000', 1),
 ('{PLAN_B}', 'rutina',             '\\xbb', '\\x000000000000000000000004', '\\x00000000000000000000000000000000', 1);
INSERT INTO acceso_relevo (id, grupo_id, plan_id, otorgado_por, otorgado_a_nombre, otorgado_a_telefono,
                           nombre_pila_persona, secciones_permitidas, motivo, token_hash, pin_hash, expira_en) VALUES
 ('{ACC_VIGENTE}',  '{G_A}', '{PLAN_A}', '{U_ADMIN_A}', 'Relevo',   '+56911111111', 'María',
  ARRAY['rutina','manejo_situaciones'], 'fin de semana', sha256('t1'), 'p', now() + interval '1 day'),
 ('{ACC_VENCIDO}',  '{G_A}', '{PLAN_A}', '{U_ADMIN_A}', 'Vencido',  '+56922222222', 'María',
  ARRAY['rutina'], 'turno', sha256('t2'), 'p', now() + interval '1 day'),
 ('{ACC_REVOCADO}', '{G_A}', '{PLAN_A}', '{U_ADMIN_A}', 'Revocado', '+56933333333', 'María',
  ARRAY['rutina'], 'turno', sha256('t3'), 'p', now() + interval '1 day');
UPDATE acceso_relevo SET creado_en = now() - interval '3 days', expira_en = now() - interval '1 day'
 WHERE id = '{ACC_VENCIDO}';
UPDATE acceso_relevo SET revocado_en = now() WHERE id = '{ACC_REVOCADO}';

INSERT INTO categoria_cuidado (id, nombre) VALUES ('00000000-0000-0000-0000-000000000c01', 'Incontinencia');
INSERT INTO producto (id, categoria_id, nombre, presentacion, unidad, unidades_por_envase) VALUES
 ('00000000-0000-0000-0000-000000000f01', '00000000-0000-0000-0000-000000000c01', 'Pañal adulto M', 'x30', 'unidad', 30);
INSERT INTO comercio (id, razon_social, nombre_fantasia, rut, direccion, comuna) VALUES
 ('{COMERCIO}', 'Farmacia Uno SpA', 'Farmacia Uno', '76.000.000-1', 'Av. Larraín 1', 'La Reina');
INSERT INTO usuario_comercio (usuario_id, comercio_id) VALUES ('{U_ENC}', '{COMERCIO}');
INSERT INTO oferta (id, producto_id, comercio_id, precio_referencia) VALUES
 ('00000000-0000-0000-0000-000000000f11', '00000000-0000-0000-0000-000000000f01', '{COMERCIO}', 12990);
INSERT INTO perfil_consumo (grupo_id, persona_cuidada_id, producto_id, tasa_unidades, stock_unidades,
                            stock_medido_en, fecha_quiebre_estimada) VALUES
 ('{G_A}', '{P_A}', '00000000-0000-0000-0000-000000000f01', 4, 24, current_date, current_date + 6),
 ('{G_B}', '{P_B}', '00000000-0000-0000-0000-000000000f01', 3, 30, current_date, current_date + 10);

INSERT INTO pedido (id, grupo_id, persona_cuidada_id, comercio_id, estado, total_estimado,
                    destinatario_nombre_pila, creado_por) VALUES
 ('{PED_A_ENVIADO}',  '{G_A}', '{P_A}', '{COMERCIO}', 'enviado_a_comercio', 25980, 'María', '{U_ADMIN_A}'),
 ('{PED_A_BORRADOR}', '{G_A}', '{P_A}', '{COMERCIO}', 'borrador',           12990, 'María', '{U_ADMIN_A}'),
 ('{PED_B_ENVIADO}',  '{G_B}', '{P_B}', '{COMERCIO}', 'enviado_a_comercio', 12990, 'Luis',  '{U_ADMIN_B}');
INSERT INTO pedido_entrega (pedido_id, calle, numero, comuna, telefono_contacto) VALUES
 ('{PED_A_ENVIADO}', 'Los Aromos', '123', 'La Reina', '+56911111111');
INSERT INTO pedido_linea (pedido_id, oferta_id, producto_id, cantidad, precio_snapshot) VALUES
 ('{PED_A_ENVIADO}',  '00000000-0000-0000-0000-000000000f11', '00000000-0000-0000-0000-000000000f01', 2, 12990),
 ('{PED_A_BORRADOR}', '00000000-0000-0000-0000-000000000f11', '00000000-0000-0000-0000-000000000f01', 1, 12990);
INSERT INTO cargo (id, pedido_id, monto_objetivo, recaudacion_expira_en) VALUES
 ('00000000-0000-0000-0000-0000000007a1', '{PED_A_ENVIADO}', 25980, now() + interval '2 hours');
INSERT INTO participacion (id, cargo_id, usuario_id, porcentaje_bp, monto_comprometido) VALUES
 ('00000000-0000-0000-0000-0000000008a1', '00000000-0000-0000-0000-0000000007a1', '{U_ADMIN_A}', 10000, 29877);
INSERT INTO transaccion_pasarela (participacion_id, proveedor, tipo, buy_order, monto, idempotency_key) VALUES
 ('00000000-0000-0000-0000-0000000008a1', 'webpay_plus', 'autorizacion', 'MATU-0001', 29877, 'k1');
INSERT INTO repartidor (id, usuario_id, vehiculo, comuna_base) VALUES ('{REPARTIDOR}', '{U_REP}', 'auto', 'La Reina');
INSERT INTO asignacion (grupo_id, pedido_id, repartidor_id) VALUES ('{G_A}', '{PED_A_ENVIADO}', '{REPARTIDOR}');
INSERT INTO idempotencia (grupo_id, endpoint, clave, usuario_id, hash_peticion, respuesta) VALUES
 ('{G_A}', 'POST /v1/pedidos', 'k-a', '{U_ADMIN_A}', '\\x00', '{{"id": "x"}}'),
 ('{G_B}', 'POST /v1/pedidos', 'k-b', '{U_ADMIN_B}', '\\x00', '{{"id": "y"}}');
"""

CONTEXTO = ("usuario_id", "grupo_id", "comercio_id", "repartidor_id", "rol", "acceso_relevo_id")


@pytest.fixture(scope="session", autouse=True)
def semilla():
    with psycopg.connect(DSN, autocommit=True) as c:
        c.execute(SEMILLA)


@pytest.fixture
def cx():
    """Conexión en transacción que se revierte al final de cada prueba."""
    with psycopg.connect(DSN) as c:
        yield c
        c.rollback()


def como(cx, db_rol="matu_app", **ctx):
    """Cambia al rol de base de datos indicado y fija el contexto de sesión (local a la transacción)."""
    cx.execute(f"SET LOCAL ROLE {db_rol}")
    for k in CONTEXTO:
        v = ctx.get(k)
        cx.execute("SELECT set_config(%s, %s, true)", (f"app.{k}", "" if v is None else str(v)))
    return cx


def contar(cx, tabla, where="true"):
    return cx.execute(f"SELECT count(*) FROM {tabla} WHERE {where}").fetchone()[0]


def tablas_publicas(cx):
    return [r[0] for r in cx.execute(
        "SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY 1").fetchall()]


# ------------------------------------------------------------------ estructura

def test_force_activo_tabla_por_tabla(cx):
    """El escenario 'RLS finge proteger' no puede ocurrir en ninguna tabla de negocio."""
    filas = cx.execute("""
        SELECT c.relname, c.relrowsecurity, c.relforcerowsecurity
        FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE n.nspname = 'public' AND c.relkind = 'r'""").fetchall()
    for nombre, rls, force in filas:
        if nombre in INFRA_SIN_RLS:
            assert not rls, f"{nombre} es infraestructura declarada y no debe tener RLS"
        else:
            assert rls and force, f"{nombre} no tiene RLS forzado"


def test_rol_de_aplicacion_no_es_propietario(cx):
    duenos = {r[0] for r in cx.execute(
        "SELECT DISTINCT tableowner FROM pg_tables WHERE schemaname = 'public'").fetchall()}
    assert duenos == {"matu_owner"}
    bypass = cx.execute("SELECT rolbypassrls OR rolsuper FROM pg_roles WHERE rolname = 'matu_app'").fetchone()[0]
    assert not bypass


# ------------------------------------------------------------------ contexto

def test_sin_contexto_cero_filas(cx):
    """Una consulta sin app.grupo_id no devuelve todo: devuelve nada."""
    como(cx)
    for t in tablas_publicas(cx):
        if t in INFRA_SIN_RLS | REFERENCIA_PUBLICA:
            continue
        assert contar(cx, t) == 0, f"{t} devuelve filas sin contexto"


def test_worker_sin_contexto_cero_filas(cx):
    """El rol sistema sin grupo no alcanza nada (hueco del diseño anterior)."""
    como(cx, rol="sistema")
    for t in ("perfil_consumo", "alerta_quiebre", "pedido", "plan_reposicion", "notificacion"):
        assert contar(cx, t) == 0, t


def test_worker_con_contexto_ve_solo_su_grupo(cx):
    como(cx, grupo_id=G_A, rol="sistema")
    assert contar(cx, "perfil_consumo") == 1
    assert contar(cx, "perfil_consumo", f"grupo_id = '{G_B}'") == 0


# ------------------------------------------------------------------ familia

def test_grupo_a_no_ve_grupo_b(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    assert contar(cx, "persona_cuidada") == 1
    assert contar(cx, "pedido", f"id = '{PED_B_ENVIADO}'") == 0
    assert contar(cx, "plan_cuidado", f"id = '{PLAN_B}'") == 0
    assert contar(cx, "usuario", f"id = '{U_ADMIN_B}'") == 0


def test_idempotencia_de_otro_grupo_cero_filas(cx):
    """Regresión del defecto 4 de la sección 12.8."""
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    assert contar(cx, "idempotencia") == 1
    assert contar(cx, "idempotencia", "clave = 'k-b'") == 0


@pytest.mark.parametrize("usuario, ve_plan", [
    (U_ADMIN_A, True),   # admin
    (U_OBS_A, False),    # observador: nunca
    (U_PAG_A, False),    # pagador sin permiso explícito
    (U_PAG2_A, True),    # pagador con permiso explícito
])
def test_rol_de_membresia_decide_el_plan(cx, usuario, ve_plan):
    como(cx, usuario_id=usuario, grupo_id=G_A)
    esperado = 3 if ve_plan else 0
    assert contar(cx, "plan_seccion") == esperado
    assert contar(cx, "clave_datos") == (1 if ve_plan else 0)
    # el perfil de consumo sí lo ve todo miembro (sección 11.2)
    assert contar(cx, "perfil_consumo") == 1


def test_alta_de_grupo_desde_cero(cx):
    """Un usuario nuevo crea su grupo y queda como admin, sin contexto de grupo previo."""
    como(cx, usuario_id=U_NUEVO)
    g = cx.execute("INSERT INTO grupo_familiar (nombre, creado_por) VALUES ('Nueva', %s) RETURNING id",
                   (U_NUEVO,)).fetchone()[0]
    cx.execute("INSERT INTO membresia (grupo_id, usuario_id, rol) VALUES (%s, %s, 'admin')", (g, U_NUEVO))
    assert contar(cx, "grupo_familiar") == 1


def test_no_puede_autoproclamarse_admin_de_grupo_ajeno(cx):
    como(cx, usuario_id=U_NUEVO)
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("INSERT INTO membresia (grupo_id, usuario_id, rol) VALUES (%s, %s, 'admin')", (G_A, U_NUEVO))


# ------------------------------------------------------------------ operación

def test_operacion_no_alcanza_plan_ni_consumo(cx):
    """La celda 'operación · plan de cuidado · nunca' de la sección 11.2 es cierta."""
    como(cx, usuario_id=U_ADMIN_B, rol="operacion")
    for t in ("plan_cuidado", "plan_seccion", "clave_datos", "acceso_relevo",
              "perfil_consumo", "reposicion", "alerta_quiebre"):
        assert contar(cx, t) == 0, f"operación alcanza {t}"
    assert contar(cx, "pedido") == 3
    assert contar(cx, "persona_cuidada") == 2


# ------------------------------------------------------------------ relevo

def test_relevo_ve_exactamente_sus_secciones(cx):
    como(cx, rol="relevo", acceso_relevo_id=ACC_VIGENTE)
    tipos = {r[0] for r in cx.execute("SELECT tipo FROM plan_seccion").fetchall()}
    assert tipos == {"rutina", "manejo_situaciones"}
    assert contar(cx, "acceso_relevo") == 1          # no ve los otros accesos
    assert contar(cx, "clave_datos") == 1            # puede descifrar solo a esa persona


def test_relevo_no_hereda_nada_de_la_familia(cx):
    """El relevo no fija app.grupo_id: no ve pedidos, pagos, direcciones ni personas."""
    como(cx, rol="relevo", acceso_relevo_id=ACC_VIGENTE)
    for t in ("pedido", "pedido_entrega", "cargo", "direccion", "persona_cuidada",
              "perfil_consumo", "membresia", "usuario"):
        assert contar(cx, t) == 0, f"el relevo alcanza {t}"


@pytest.mark.parametrize("acceso", [ACC_VENCIDO, ACC_REVOCADO, None])
def test_relevo_vencido_revocado_o_sin_acceso_cero_filas(cx, acceso):
    como(cx, rol="relevo", acceso_relevo_id=acceso)
    for t in ("plan_seccion", "plan_cuidado", "acceso_relevo", "clave_datos"):
        assert contar(cx, t) == 0, t


def test_relevo_registra_su_apertura_en_auditoria(cx):
    como(cx, rol="relevo", acceso_relevo_id=ACC_VIGENTE)
    cx.execute("""INSERT INTO auditoria (grupo_id, actor_tipo, actor_ref, accion, entidad, entidad_id)
                  VALUES (%s, 'relevo', %s, 'relevo.abrir', 'plan_cuidado', %s)""", (G_A, ACC_VIGENTE, PLAN_A))
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("""INSERT INTO auditoria (grupo_id, actor_tipo, accion, entidad)
                      VALUES (%s, 'relevo', 'relevo.abrir', 'plan_cuidado')""", (G_B,))


# ------------------------------------------------------------------ comercio y repartidor

def test_comercio_ve_pedidos_enviados_sin_direccion_ni_pago(cx):
    como(cx, usuario_id=U_ENC, comercio_id=COMERCIO)
    assert contar(cx, "pedido") == 2                          # A y B enviados, no el borrador
    assert contar(cx, "pedido", f"id = '{PED_A_BORRADOR}'") == 0
    assert contar(cx, "pedido_linea") == 1                    # solo la del pedido enviado
    for t in ("pedido_entrega", "cargo", "participacion", "transaccion_pasarela",
              "persona_cuidada", "direccion", "plan_cuidado", "perfil_consumo"):
        assert contar(cx, t) == 0, f"el comercio alcanza {t}"


def test_repartidor_sin_precios_unitarios(cx):
    como(cx, usuario_id=U_REP, repartidor_id=REPARTIDOR)
    assert contar(cx, "pedido") == 1
    assert contar(cx, "pedido_entrega") == 1
    for t in ("pedido_linea", "cargo", "plan_seccion", "perfil_consumo", "persona_cuidada"):
        assert contar(cx, t) == 0, f"el repartidor alcanza {t}"


# ------------------------------------------------------------------ integridad

def test_auditoria_es_solo_insercion(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    cx.execute("INSERT INTO auditoria (grupo_id, actor_tipo, accion, entidad) VALUES (%s, 'usuario', 'x', 'y')", (G_A,))
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("UPDATE auditoria SET accion = 'z'")


def test_transaccion_de_pasarela_no_se_borra(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("DELETE FROM transaccion_pasarela")


def test_outbox_solo_admite_identificadores(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    cx.execute("""INSERT INTO evento_outbox (grupo_id, tipo, agregado_tipo, agregado_id, payload)
                  VALUES (%s, 'PedidoEnviado', 'pedido', %s, jsonb_build_object('pedido_id', %s::text))""",
               (G_A, PED_A_ENVIADO, PED_A_ENVIADO))
    with pytest.raises(errors.CheckViolation):
        cx.execute("""INSERT INTO evento_outbox (grupo_id, tipo, agregado_tipo, agregado_id, payload)
                      VALUES (%s, 'X', 'pedido', %s, '{"nombre": "María"}')""", (G_A, PED_A_ENVIADO))


def test_la_api_no_lee_el_outbox(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("SELECT * FROM evento_outbox")


def test_publicador_no_alcanza_tablas_de_negocio(cx):
    cx.execute("SET LOCAL ROLE matu_publisher")
    assert cx.execute("SELECT count(*) FROM evento_outbox").fetchone()[0] >= 0
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("SELECT count(*) FROM pedido")


def test_scheduler_solo_enumera_identificadores(cx):
    cx.execute("SET LOCAL ROLE matu_scheduler")
    assert cx.execute("SELECT count(id) FROM grupo_familiar").fetchone()[0] == 2
    with pytest.raises(errors.InsufficientPrivilege):
        cx.execute("SELECT nombre FROM grupo_familiar")


def test_borrado_criptografico_es_explicito(cx):
    """Regresión del defecto 5: sin clave no hay estado ambiguo."""
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    with pytest.raises(errors.CheckViolation), cx.transaction():
        cx.execute("UPDATE clave_datos SET dek_cifrada_con_kek = NULL")
    cx.execute("UPDATE clave_datos SET dek_cifrada_con_kek = NULL, destruida_en = now()")


def test_nonce_no_se_repite(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    with pytest.raises(errors.UniqueViolation):
        cx.execute("""INSERT INTO plan_seccion (plan_id, tipo, contenido_cifrado, nonce, tag_auth, kek_version)
                      VALUES (%s, 'horarios', '\\xaa', '\\x000000000000000000000001',
                              '\\x00000000000000000000000000000000', 1)""", (PLAN_A,))


def test_captura_no_supera_lo_autorizado(cx):
    como(cx, usuario_id=U_ADMIN_A, grupo_id=G_A)
    with pytest.raises(errors.CheckViolation):
        cx.execute("UPDATE participacion SET monto_autorizado = 100, monto_capturado = 101")
