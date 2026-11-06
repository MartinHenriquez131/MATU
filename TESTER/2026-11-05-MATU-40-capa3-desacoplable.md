# 2026-11-05 · MATU-40 · La capa 3 se puede quitar

**Historia:** MATU-40 · Capa 3 desacoplable: las capas 1 y 2 funcionan sin el despacho
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#44 (commit 702d08b, fusionado como ac8f691)
**Revisó:** Martín Henríquez · **Fecha:** 05/11/2026
**Veredicto general:** PASS. No hay hallazgos

La revisión original quedó en GitHub ([revisión 5794403375](https://github.com/MartinHenriquez131/MATU_PROYECTO/pull/44#pullrequestreview-5794403375)). Este informe la copia en `TESTER/` para que quede junto a las demás.

## Contexto de la revisión

- **CI del PR:** verde en `ci` y en `web`, con la rama al día con `main`. No se repitió el pipeline.
- **Entorno:** revisión del código. Staging despliega `main` con el interruptor apagado (06/11, despliegue de 7369df2, `/v1/salud` 200).

## Criterios

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | `CAPA3_HABILITADA` apagado por omisión; los routers de la capa 3 se importan solo con el interruptor encendido | PASS | configuración y `main.py` del PR |
| 2 | La API arranca con los paquetes de la capa 3 bloqueados | PASS | `test_capa3_desacoplable.py` (21 pruebas) |
| 3 | El OpenAPI expone solo las capas 1 y 2 | PASS | `test_capa3_desacoplable.py` |
| 4 | Ningún import de las capas 1 y 2 llega a la capa 3 | PASS | `test_capa3_desacoplable.py` |
| 5 | Ninguna llave foránea apunta a la capa 3, salvo `perfil_consumo.producto_id`, anulable y declarada como excepción | PASS | `test_capa3_desacoplable.py` |
| 6 | Cinco flujos pasan con la capa 3 bloqueada: ficha, compartir, relevo con PIN, consumo y alertas | PASS | `test_capa3_desacoplable.py` |
| 7 | Decisión 104: `catalog` es capa 3 | PASS | `docs/api/README.md` |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | No aplica | Sin reglas de dominio nuevas |
| 2. Integración | PASS | Los cinco flujos con la capa 3 bloqueada |
| 3. Contrato OpenAPI | PASS | Sin cambios de contrato; la prueba verifica que no aparezca la capa 3 |
| 4. Accesibilidad | No aplica | Sin pantallas (no toca `web/` ni `Demo/`) |
| 5. Revisión de la otra persona | PASS | Este informe |
| 6. Prueba que falla sin la corrección | No aplica | No corrige un defecto |

**Alcance:** sin migraciones, sin cambios de contrato y sin tocar `web/` ni `Demo/`.

## Hallazgos

Ninguno.
