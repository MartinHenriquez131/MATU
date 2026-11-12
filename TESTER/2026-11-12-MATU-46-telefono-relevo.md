# 2026-11-12 · MATU-46 · Borrar el teléfono del relevo y anonimizar el nombre de pila

**PR revisados:** MartinHenriquez131/MATU_PROYECTO#90 (0027, política 0.16) y MartinHenriquez131/MATU#83
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor` y `revisor-documental` · **Fecha:** 12/11/2026
**Revisión obligatoria:** sí (datos personales)
**Veredicto general:** PASS, sin P1

## Revisiones

- **QA:** PASS.
  - El trigger hace que el teléfono solo se pueda vaciar, una vez, para todos los roles.
  - `relevo_conservar` es `SECURITY DEFINER`, solo la puede ejecutar `matu_scheduler` y rechaza un límite de menos de 30 días.
  - La bajada de la migración se detiene si ya se borró algún teléfono.
  - `conservacion_relevo` corre dentro de los borrados diarios.
  - Al borrar a la persona, el teléfono se vacía y el nombre se anonimiza en la misma sentencia.
  - El log lleva solo el contador.
- **Analista:** CUMPLE en conservación, supresión, auditoría y lo que se informa. REQUIERE CONSULTA LEGAL: CL-60 (anonimización o seudonimización), CL-29 (copias de respaldo) y CL-34 (el relevo pide borrar su teléfono antes).
- **Documentos:** sin P1. El #83 se fusionó después del #82, como pedía.

## Fusión y despliegue (hora de Chile)

- **Fusiones:** #90 (590d8a2) y MATU#83 (32d596a), con merge commit.
- **Migración:** `POLITICA_VERSION=0.16` y `Running upgrade 0026 -> 0027` sin errores, a las 15:30 en staging y a las 15:31 en la demo.
- **Cron:** `matu-cron-borrados` se redesplegó en los dos entornos.

## Prueba en el teléfono

**No aplica:** MATU-46 no tiene pantalla nueva. La prueba de los 30 días la cubren las pruebas automáticas, con el reloj adelantado.

## Hallazgos

| ID | Severidad | Hallazgo |
|---|---|---|
| H1 | P2 | La política (§8) declara 3 años para los accesos, pero todavía nada los borra. MATU-89 es condición antes de usar datos reales |
| H2 | P3 | `relevo_conservar` acepta un `ahora` hasta 5 minutos adelantado, así que el plazo de 30 días puede acortarse hasta en 5 minutos |
| H3 | P3 | Hay una línea en blanco doble después de la CL-60 en `consulta-legal.md` |

**A la consulta legal:** CL-60, y las CL-29 y CL-34 ampliadas.
