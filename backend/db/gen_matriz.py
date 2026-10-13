"""Genera la matriz de acceso por eje (diagramas/10-rls-matriz-de-acceso.png y .svg).
Cada celda está respaldada por una prueba de tests/test_aislamiento.py."""
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SALIDA = pathlib.Path(__file__).resolve().parents[2] / "docs" / "diagramas" / "modelo-datos"
COLUMNAS = ["Plan de cuidado\n(secciones, clave,\naccesos)", "Perfil de\nconsumo", "Pedido", "Líneas y\nprecios",
            "Dirección\nde entrega", "Cargo y\npagos", "Liquidación\nal comercio", "Auditoría"]
FILAS = [
    ("Familia\nusuario + grupo", ["Según rol*", "Sí", "Sí", "Sí", "Sí", "Sí", "Nunca", "Su grupo"]),
    ("Relevo\nrol relevo + acceso\n(sin grupo)", ["Solo secciones\nhabilitadas y vigente", "Nunca", "Nunca", "Nunca",
                                               "Nunca", "Nunca", "Nunca", "Inserta la\nsuya"]),
    ("Comercio\ncomercio_id", ["Nunca", "Nunca", "Enviados o\nposteriores", "Sí", "Nunca", "Nunca", "Los suyos", "Nunca"]),
    ("Repartidor\nrepartidor_id", ["Nunca", "Nunca", "Su asignación\nactiva", "Nunca", "Su asignación\nactiva",
                                   "Nunca", "Nunca", "Nunca"]),
    ("Operación\nrol operacion", ["Nunca", "Nunca", "Todos", "Todos", "Todos", "Todos", "Todos", "Lee todo"]),
    ("Sistema · worker\nrol sistema + grupo", ["Nunca", "Su grupo", "Su grupo", "Su grupo", "Su grupo", "Su grupo",
                                               "Nunca", "Inserta"]),
    ("Sin contexto", ["Nunca"] * 8),
]


def color(v):
    if v.startswith("Nunca"):
        return "#f6d5d2"
    if v in ("Sí", "Todos"):
        return "#d4ecd9"
    return "#fdf0c8"


fig, ax = plt.subplots(figsize=(17, 7.4))
ax.axis("off")
t = ax.table(cellText=[f[1] for f in FILAS], rowLabels=[f[0] for f in FILAS], colLabels=COLUMNAS,
             cellLoc="center", loc="center", cellColours=[[color(v) for v in f[1]] for f in FILAS],
             rowColours=["#eef1f6"] * len(FILAS), colColours=["#0A253E"] * len(COLUMNAS))
t.auto_set_font_size(False)
t.set_fontsize(10.5)
for (r, c), celda in t.get_celld().items():
    celda.set_height(0.13 if r > 0 else 0.15)
    celda.set_edgecolor("#9aa4b2")
    if r == 0:
        celda.get_text().set_color("white")
        celda.get_text().set_weight("bold")
    if c == -1:
        celda.get_text().set_weight("bold")
        celda.set_width(0.14)
ax.set_title("MATU · Qué filas alcanza cada eje de acceso (RLS forzado · verificado por tests/test_aislamiento.py)",
             fontsize=14, weight="bold", pad=18)
fig.text(0.02, 0.02, "* admin y cuidador siempre · pagador solo con permiso explícito · observador nunca.     "
         "Verde: acceso completo     Amarillo: acotado     Rojo: cero filas por política", fontsize=10)
for ext in ("png", "svg"):
    fig.savefig(SALIDA / f"10-rls-matriz-de-acceso.{ext}", dpi=160, bbox_inches="tight", facecolor="white")
print("matriz escrita")
