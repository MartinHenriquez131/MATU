# 2026-11-05 · Pruebas en el teléfono · MATU-39, MATU-36, MATU-37 y MATU-57

**Historias:** MATU-39 (app de familia), MATU-36 (Insumos), MATU-37 (alertas) y MATU-57 (recuperar el acceso)
**Entorno:** staging, `https://matu-api-production.up.railway.app`, desplegado desde `main` en el commit `539438e` (merge del #38, con #29, #48, #37 y #38)
**Revisó:** Martín Henríquez · **Fecha:** 05/11/2026, desde las 17:14 (hora de Chile)
**Teléfono y navegador:** Motorola Edge 50, Android, Microsoft Edge
**Veredicto general:** PASS en las cuatro. Hay un hallazgo P2 y dos P3 de textos

Se usaron solo datos inventados: una cuenta `@example.com` y el celular `+56 9 5555 0199`.

## Resultados

| # | Historia | Recorrido | Veredicto | Evidencia |
|---|---|---|---|---|
| 1 | MATU-39 | Crear cuenta, grupo, persona y autorización; llenar los tres campos de la ficha; salir y volver a entrar | PASS | La ficha sigue después de volver a entrar. **Tiempo de la ficha: 4 min 15 s** (ver P3-2) |
| 2 | MATU-36 | Autorizar el cálculo; anotar «Pañales talla M» (3, 1 por día) y «Crema» (30, 1 por día); cambiar Crema a 25; dejar de seguirla y volver a seguirla | PASS | «Alcanza para» mostró 3, 30 y después 25 días, sin errores |
| 3 | MATU-37 | «Se acaban pronto» con Pañales; «Ya lo resolví» con 10 comprados | PASS | Pañales salió del bloque y pasó a alcanzar para unos 13 días |
| 4 | MATU-57 | «¿Olvidaste tu contraseña?», el código leído en el envío simulado con `railway ssh`, la contraseña nueva | PASS | Entró con la contraseña nueva y la vieja quedó rechazada. Cierra el P2-1 de `2026-11-05-MATU-57-recuperar-acceso.md` |

## Hallazgos

| ID | Sev. | Hallazgo | Respuesta de Jorge | Verificado |
|---|---|---|---|---|
| P2-1 | P2 | **Un 429 se muestra como un problema de conexión.** Al crear la cuenta, después de 5 intentos fallidos, la API respondió 429. Se ve en los registros HTTP de Railway, 05-11, de 17:16:46 a 17:17:43. La app mostró «No pudimos completar esto. Revisa tu conexión y vuelve a intentarlo», y eso es engañoso. Debería decir algo como «Hiciste muchos intentos. Espera {minutos} minutos y vuelve a intentarlo», usando el `Retry-After`. Revisar las demás pantallas que pueden recibir 429: entrar, recuperar y el relevo | Corregido en el #51 (textos de `lenguaje.md` 13.3, MATU#36 y MATU#38) | **Verificado** 06-11 en staging (`7369df2`), Motorola Edge 50 con Edge: en el 6.º intento seguido de crear cuenta apareció «Espera un momento» y «Hubo muchos intentos desde esta conexión. Vuelve a intentarlo en 58 minutos.» En total tomó 3 minutos, sin nada raro |
| P3-1 | P3 | En staging, un correo de un dominio que no está reservado (por ejemplo `@ejemplo.com`) recibe «Revisa tu correo.», y no explica por qué. Propuesta solo para staging: «En este ambiente de prueba usa un correo terminado en @example.com» (decisión 105, `dominio_no_permitido`) | | |
| P3-2 | P3 · Para MATU-34 | La ficha tomó 4 min 15 s, y la meta es menos de 3 min. Lo hizo alguien que no conocía la pantalla, así que es un dato para las sesiones con usuarios, no una falla | | |

## Qué falta

- **MATU-50 (secciones de la ficha):** se prueba cuando entren el #41 y el #42.
- **MATU-48 (compartir, `/r` con PIN y cortar):** se prueba cuando entre el #45.
