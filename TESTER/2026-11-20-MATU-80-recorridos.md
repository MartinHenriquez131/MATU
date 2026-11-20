# TESTER · 20-11: MATU-80, los seis recorridos en el teléfono

**Revisor:** Martín Henríquez (modo Martín) · **Fecha:** 20-11-2026
**Resultado:** **PASS** en los seis recorridos. La carga (RNF-05) sigue abierta

## Despliegue

- **Despliegue final:** `main` en e8c468b, en staging y en la demo, el 20-11 a las 13:23.
  - Sin migraciones nuevas: la 0036 ya estaba desde las 10:48.
  - El pipeline de `main` estaba en verde (`ci`, `web` e `imagen`).
- **La demo** se restableció el 20-11 en la mañana, después de la 0036. No se restableció de nuevo porque el despliegue final no traía cambios de datos.
- **El objetivo 7 decía «desplegado el 19 de noviembre»,** pero el despliegue final quedó el 20. El motivo: la fila de PR con migraciones (#123 a #127) se fusionó y se desplegó en orden, y la última revisión terminó el 20.

## Teléfono (demo, 20-11, 16:45 a 16:57)

Motorola Edge 50 Pro con Edge, letra normal. El computador hizo de segundo dispositivo (R2) y de consola de operación (R6).

| Recorrido | Qué se probó | Resultado |
|---|---|---|
| R1 | Crear la cuenta con un correo nuevo de `example.com`, el grupo, la persona cuidada, la autorización y la ficha con sus tres campos | OK |
| R2 | Compartir con un relevo con PIN, abrirlo en otro dispositivo (la dirección queda limpia) y cortar el acceso | OK |
| R3 | Los insumos de María con el aviso de quiebre del pañal, y un insumo nuevo con su fecha de quiebre | OK |
| R4 | Exportar o compartir la lista de reposición y anotar una compra | OK |
| R5 | El pedido de Rodrigo desde la lista y el pago en Webpay (integración, tarjeta de prueba), con el monto igual al total confirmado | OK |
| R6 | Operación genera el código de retiro (que se muestra una vez), el comercio marca la parte preparando y lista, valida el código y queda retirada. La línea de tiempo lo muestra | OK |

En el informe no se anotaron enlaces, PIN, códigos de retiro ni códigos TOTP.

## Pendiente

- **Carga (RNF-05):** decisión de Jorge del 20-11 (ver `TESTER/2026-11-20-MATU-79-124-127-121-128.md`, anexo):
  - K1: el pool queda configurable;
  - K2: se busca qué pone en fila el retorno;
  - la meta sigue en 800 ms.
  - Cuando llegue ese PR: Martín lo revisa, lo despliega, repite k6 (ojalá en otro equipo) y **repite R5**, que es el único recorrido que toca el retorno.
- **MATU-80 pasa a Terminado** cuando esté la nueva corrida de k6, o la decisión de los tres sobre RNF-05.
