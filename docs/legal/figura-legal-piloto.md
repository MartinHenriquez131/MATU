# Figura legal del piloto (MATU-27)

**Decisión:** tomada por Jorge Espinoza (Product Owner) el 24/10/2026
**Redacción:** analista normativo del equipo de agentes, a partir de la arquitectura, el backlog y la prueba de concepto de Transbank. Este documento no es asesoría legal.
**Aprobación del texto:** [PENDIENTE: Jorge Espinoza, en la revisión del pull request]

## 1. Contexto

- MATU es el proyecto de título de dos estudiantes. Hoy no existe una persona jurídica que lo respalde.
- Para cobrar con Webpay en producción se necesita un comercio dado de alta en Transbank, y el alta exige el RUT del comercio (arquitectura, sección 17).
- El objetivo del semestre se formuló sobre un entorno de demostración (arquitectura, secciones 17 y 18.1). Ninguna historia del semestre necesita cobros reales para darse por terminada.
- La política de privacidad v0.9 declara que el piloto no trata datos reales. Las versiones 0.x significan sin datos reales. La 1.0 es la primera revisada por un abogado.
- La Ley 21.719 entra en vigencia plena el 01/12/2026, antes del cierre del semestre. La consulta legal sobre el cuidador de hecho sigue abierta.
- La prueba de concepto de Transbank (S0-E) confirmó que la captura diferida cobra el monto real y revierte sin cobrar, y que opera solo con crédito.

## 2. Opciones consideradas

| Opción | Qué exige | Resultado |
|---|---|---|
| Constituir una persona jurídica durante el semestre | Constitución, inicio de actividades y alta comercial en Transbank. Plazo y costo: [PENDIENTE, no se estimaron porque se descartó la opción] | Descartada. No cabe en la ventana de construcción y el entregable no la necesita |
| Operar en el ambiente de integración de Transbank y declararlo en el informe | Nada externo al equipo | **Elegida** |

## 3. Decisión

Durante el semestre, el piloto de MATU opera solo en el ambiente de integración de Transbank, con datos sintéticos y sin cobros reales. Esto se declara en el informe.

La constitución de una persona jurídica y el alta comercial en Transbank quedan para después del semestre. Por eso el trámite de alta comercial no se inicia durante el semestre, como pide el criterio de MATU-27.

## 4. Qué implica

### 4.1 Lo que se puede hacer

- Demostrar el flujo de pago completo con las credenciales de integración de Transbank y sus tarjetas de prueba.
- Usar datos sintéticos generados por las fábricas de prueba o escritos por el equipo.
- Mostrar la aplicación al profesor, a la comisión y a quienes evalúan el proyecto.
- Desplegar un ambiente de demostración con un aviso visible en todas las pantallas: es un piloto académico y usa solo datos de prueba. Texto exacto: [PENDIENTE, sale de docs/lenguaje.md]
- Conversar con comercios sobre un eventual convenio, sin compromisos de dinero ni pedidos reales.

### 4.2 Lo que no se hace

- Ingresar datos de personas reales: ni de personas cuidadas, ni de familias, ni de cuidadoras, ni de las personas entrevistadas.
- Cobrar dinero real o usar credenciales de producción de Transbank.
- Recibir, ver o guardar datos de tarjetas. Webpay captura la tarjeta en su propio formulario, y MATU solo recibe el resultado de la transacción.
- Abrir el registro al público o captar familias.
- Enviar mensajes a teléfonos o correos de personas fuera del equipo. Los envíos de prueba van a buzones y números del equipo o a un servicio de pruebas.
- Despachar pedidos reales con un comercio.

### 4.3 Los pocos datos reales que existen igual

Aunque el producto use datos sintéticos, existen algunos datos personales reales: las cuentas que use el equipo y los registros técnicos del servidor de demostración.

- Las cuentas de prueba usan correos ficticios de dominios reservados para ejemplos (example.com, .test o .invalid).
- Si una persona fuera del equipo prueba la demostración, usa una cuenta de prueba que le entrega el equipo.
- Si el ramo exige pruebas de usabilidad con personas: [PENDIENTE, definir cómo se hacen sin que ingresen datos reales]
- Si entra un dato real por error, se borra de inmediato, como compromete la política v0.9.

### 4.4 Responsable del tratamiento durante el piloto académico

Durante el semestre, el responsable es el equipo del proyecto, Jorge Espinoza y Martín Henríquez, como personas naturales.

- Contacto: [PENDIENTE, correo del proyecto]
- Qué trata: cuentas de prueba y registros técnicos de la demostración. Ningún dato real de salud ni de dependencia.
- Rol de la institución: [PENDIENTE, confirmar con el ramo si la institución tiene algún rol respecto de los datos del piloto]
- Las entrevistas de validación se rigen por su propio protocolo y no por este documento.

## 5. Cómo encaja con el débito (plan B del ADR-006)

La aplicación no debe limitar las formas de pago. Por eso se acepta el débito con el plan B del ADR-006 (decisión del 24/10/2026, registrada en `docs/pruebas-concepto/transbank.md`).

- **Con crédito:** se autoriza el monto estimado con margen y se captura el monto real.
- **Con débito:** se cobra el monto estimado, y cuando el pedido sale por menos se devuelve la diferencia y se emite la nota de crédito.
- La persona elige crédito o débito en MATU antes de ir a Webpay, porque el comercio de captura diferida solo ofrece crédito. [PENDIENTE, el código de comercio para débito se confirma en el diseño del módulo de pagos]
- Antes de pagar con débito, la pantalla informa el monto que se cobra en ese momento, que la diferencia se devuelve si el pedido sale por menos, y el medio y el plazo de la devolución. [PENDIENTE, medio y plazo]
- [PENDIENTE, verificar en integración cómo se devuelve la diferencia con débito antes del sprint 4]
- Ninguna de las dos rutas mueve dinero real durante el semestre. Después del semestre, el alta comercial debe cubrir las dos modalidades.

## 6. Qué se hace después del semestre

Antes de tratar datos reales o cobrar dinero real, en este orden:

1. Constituir la persona jurídica. Tipo, plazo y costo: [PENDIENTE]
2. Alta comercial en Transbank a nombre de la persona jurídica, con las dos modalidades de la sección 5.
3. Resolver la consulta legal: cuidador de hecho, registro escrito por una cuidadora remunerada y el plan B del débito.
4. Política de privacidad 1.0 revisada por un abogado, con la persona jurídica como responsable. `POLITICA_VERSION` pasa a 1.0, y los consentimientos otorgados con versiones 0.x no sirven para datos reales.
5. Registro de tratamientos y contratos con los encargados de tratamiento: infraestructura y comercios.
6. Clave maestra en un servicio de custodia, fuera del servidor de aplicación (arquitectura, sección 11.4 y ADR-016).
7. El aviso de piloto académico se retira solo cuando los puntos 1 a 6 están cumplidos.

## 7. Cómo se declara en el informe

Texto propuesto:

> Durante el semestre, MATU operó como piloto académico. Todos los datos de personas cuidadas, familias y pedidos fueron sintéticos. Los pagos se demostraron en el ambiente de integración de Transbank, con tarjetas de prueba y sin cobros reales. MATU no recibe ni guarda datos de tarjetas. El proyecto no cuenta con persona jurídica, y por eso no inició el alta comercial en Transbank. Operar con familias reales exige constituirla, completar el alta comercial, resolver la consulta legal sobre quién autoriza el tratamiento de los datos de una persona sin capacidad para consentir y publicar una política de privacidad revisada por un abogado.

## 8. Cuándo se revisa esta decisión

- Si aparece la necesidad de operar con una familia real durante el semestre. Esta decisión no lo permite, así que se reabre.
- Si un comercio acepta un convenio con dinero real.
- Si el ramo exige operación real.
