# 2026-11-12 · MATU-42 y MATU-53 · Invitar a un familiar y ver el grupo

**PR revisados:** MartinHenriquez131/MATU_PROYECTO#89 (0026, política 0.15) y MartinHenriquez131/MATU#82
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 12/11/2026
**Revisión obligatoria:** sí (datos personales y roles)
**Veredicto general:** PASS, sin P1

## Revisiones

- **QA:** PASS.
  - La 0026 tiene RLS separada por operación y el trigger que impide dejar el grupo sin quien lo administre.
  - Las funciones `SECURITY DEFINER` tienen el `search_path` fijo, no dan permisos a PUBLIC y aceptan `p_ahora` solo dentro de ±5 min.
  - La invitación no guarda el correo ni el teléfono de la persona invitada, guarda el código como HMAC y se bloquea al 5.º intento fallido.
  - Un recurso de otro grupo responde 404 y nunca 403.
  - El token va en el fragmento de la dirección y se limpia con `replaceState`.
  - Los logs no llevan el código, el token ni datos de contacto.
- **Analista:** CUMPLE en minimización, quién da acceso, conservación de las invitaciones (30 días), lo que se informa y la auditoría. REQUIERE CONSULTA LEGAL: CL-57, CL-58 y CL-59.
- **Diseñador (Martín):** APROBADAS /grupo, /grupo/invitar, /grupo/invitar/listo e /invitacion, a 320 px al 200 %, 360, 1280 y 1920, en claro y oscuro. No hay desplazamiento horizontal ni texto bajo 17 px fuera de la barra inferior.
- **Documentos:** sin P1.

## Fusión y despliegue (hora de Chile)

- **Fusiones:** #89 (2674b97) y MATU#82 (0ffb536), con merge commit.
- **Staging:** `POLITICA_VERSION=0.15`, y `Running upgrade 0025 -> 0026` sin errores a las 15:26.
  - La migración revisa que la tabla `invitacion` esté vacía y se detiene si no lo está. No hizo falta consultarla a mano.
- **Demo:** quedó en la 0027 junto con MATU-46. Se redesplegó `matu-cron-borrados` en los dos entornos.

## Prueba en el teléfono

El 12-11, de 15:45 a 15:51, en la demo (informado por Martín). Se usaron dos teléfonos: el Motorola Edge 50 con Edge, como Carmen (admin), y el iPhone 11 con iOS 26.6.2 y Safari, sin sesión.

| # | Prueba | Resultado |
|---|---|---|
| G1 | Crear la invitación: el código de 4 dígitos con «No lo volverás a ver» | OK |
| G2 | Cambiar de app y volver: el código sigue. Al recargar: «El código ya no se puede ver» | OK |
| G3 | «Enviar el enlace» por WhatsApp: el mensaje no trae el código ni nombres | OK |
| G4 | En el iPhone: el enlace muestra «Te unes a…», y el código se acepta escrito con un espacio | OK |
| G5 | Crear la cuenta desde la invitación (`@example.com`) y quedar dentro del grupo | OK |
| G6 | «Atrás» no vuelve a una dirección con `#` | OK |
| G7 | Cambiar el rol desde el Motorola | OK |
| G8 | Sacar del grupo: el iPhone deja de ver el grupo | OK |
| G9 | /grupo con la letra al máximo y en tema oscuro | OK |

**Resultado:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P2 | Un miembro activo podría leer por SQL directo el correo y el celular de los demás miembros. Hoy solo lo impide la API, y la política §6 promete que no se ven (analista, O3) | Que MATU-102 sea condición antes de usar datos reales |
| H2 | P3 | Los rótulos de la barra inferior miden 14,9 px, y «Grupo» activo tiene contraste 3,13:1 en tema claro. La barra no es de este PR | Revisarlo en una tarjeta aparte |
| H3 | P3 | `arquitectura.md` 11.8 citaba la D-46-7 antes de que existiera. Se corrige con MATU#83, ya fusionado | Se anota |

**A la consulta legal:** CL-57, CL-58 y CL-59.
