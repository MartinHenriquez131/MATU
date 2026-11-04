# TESTER · Revisiones de Martín

Aquí quedan las revisiones de Martín (Tester/QA y despliegue) de lo que construye Jorge. Es parte del reparto en prueba ([`docs/sprints/reparto-en-prueba.md`](../docs/sprints/reparto-en-prueba.md)).

## Reglas

- **Un archivo por revisión**, con el nombre `AAAA-MM-DD-MATU-XX-<tema>.md`. Por ejemplo, `2026-11-05-MATU-50-ficha-ampliada.md`. Si una historia tiene una segunda revisión, se escribe en un archivo nuevo con su fecha.
- **El veredicto es por criterio:** PASS o FAIL, siempre con evidencia, que puede ser:
  - el comando y su salida;
  - una captura;
  - la ruta y la línea del archivo;
  - el paso exacto en el teléfono.
- **Severidad:**
  - **P1:** bloquea la fusión o el paso a Terminado. Rompe un criterio, la seguridad, la accesibilidad o una regla innegociable.
  - **P2:** se corrige antes de cerrar la historia, o en una tarjeta con fecha.
  - **P3:** pulido. Queda anotado.
- **Martín no cambia decisiones.** Si un hallazgo pide cambiar una decisión, se marca como «Para decidir (PO)» y lo decide Jorge.
- **Solo datos sintéticos** en la evidencia: sin datos reales, sin secretos, sin tokens ni PIN, y sin texto de la ficha de una persona real.
- **El orquestador de Jorge** lee esta carpeta al retomar una historia y responde a cada hallazgo en «Respuesta de Jorge». Un hallazgo se cierra cuando Martín marca «Verificado».
- **En la tarjeta de Trello**, Martín deja un comentario breve con el veredicto general y el enlace al archivo.

## Plantilla

Copia esto en un archivo nuevo:

```markdown
# AAAA-MM-DD · MATU-XX · <tema>

**Historia:** MATU-XX · <título> (enlace a la tarjeta de Trello)
**PR revisado:** <repositorio>#<número> (commit <sha corto>)
**Revisó:** Martín Henríquez · **Fecha:** DD/MM/AAAA
**Veredicto general:** PASS / FAIL

## Contexto de la revisión

- CI del PR: verde / rojo / pendiente (si está en verde, no se repite el pipeline completo)
- Entorno: local / staging · teléfono y navegador: <modelo y navegador>
- Qué no se revisó y por qué

## Criterios de aceptación

| # | Criterio (copiado de la tarjeta o del backlog) | Veredicto | Evidencia |
|---|---|---|---|
| 1 | | PASS / FAIL | |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | | |
| 2. Integración: camino feliz y de error | | |
| 3. Contrato OpenAPI | | |
| 4. Accesibilidad (estrategia de pruebas, sección 7) | | |
| 5. Revisión de la otra persona si toca datos sensibles o dinero | | |
| 6. Prueba que falla sin la corrección, si se corrigió un defecto | | |

## Prueba en el teléfono

- Recorrido y pasos:
- Resultado:

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P1 / P2 / P3 | | | |

## Para decidir (PO)

- Lo que no es un defecto sino una decisión de Jorge.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | sí / no |
```
