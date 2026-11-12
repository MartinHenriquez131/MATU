# ADR-029 · La ficha de relevo no se imprime ni se exporta

**Estado:** Aceptado
**Fecha de decisión:** 3 de noviembre de 2026
**Decisor:** Jorge Espinoza (Product Owner). Martín Henríquez (Scrum Master) revisa en el PR
**Reemplaza:** RF-09 tal como estaba en la arquitectura v1.1 y la historia MATU-52 («La hoja del refrigerador: ficha imprimible»). **Ajusta:** el ADR-028 (la hoja imprimible incluía las secciones)

---

## Contexto

RF-09 decía: «El plan de cuidado se exporta como documento imprimible para el relevo sin conexión». MATU-52 lo llevaba a la app como una hoja para pegar en el refrigerador, con los tres campos y las secciones que la familia eligiera, incluida «Sus remedios».

La revisión previa del analista normativo de MATU-52 (03-11) mostró el problema de fondo:
- La ficha guarda datos sensibles de la persona cuidada, y MATU la comparte **solo con un enlace con PIN, que vence y se puede cortar**. Esa es la promesa de la capa 1.
- Una hoja en papel **no vence, no se corta y la lee cualquiera** que entre a la casa. MATU no sabe quién la lee ni puede borrarla, y retirar la autorización no alcanza a las hojas ya impresas.
- Imprimir «Sus remedios» quedaba para consulta legal: la autorización dice «compartirla con el relevo que elija el grupo», no dejarla a la vista de cualquiera.

## Decisión

1. **La ficha de relevo no se imprime ni se exporta.** Ni los tres campos ni las secciones complementarias. Se comparte solo con el acceso de relevo (enlace con PIN).
2. **RF-09 se redefine:** lo que se exporta y se imprime es **la lista de reposición de insumos** (objetivo específico 5, ADR-027). Esa lista no lleva datos de la ficha.
3. **MATU-52 sale del alcance.** La tarjeta queda en el Product Backlog marcada como quitada, con la revisión del analista como antecedente.
4. **La hoja del refrigerador sigue siendo la metáfora visual de la ficha en pantalla** (DISENO.md, principio 1): el papel con renglones y el imán de miel. Lo que se quita es imprimirla, no su aspecto.

## Consecuencias

- **Se pierde el plan B sin internet del relevo.** Si se corta internet o el teléfono se queda sin batería, el relevo depende de lo que anotó o fotografió de la página del relevo. Es una consecuencia aceptada: la protección de la ficha pesa más. No se reabre este punto sin una decisión nueva.
- MATU no puede impedir que el relevo o la familia impriman la página con el navegador o le saquen una captura. MATU no lo ofrece ni lo facilita: no hay botón, vista ni estilo de impresión para la ficha. El aviso que ve quien comparte (lenguaje.md, sección 9) ya dice que el relevo puede anotar o fotografiar.
- **No es una excepción a los derechos del titular.** «Mis datos» (MATU-54, sprint 4) entrega a quien corresponde todo lo que MATU guarda de la persona, incluida la ficha, porque es el derecho de acceso y de portabilidad (Ley 21.719). Esa descarga no es una hoja para pegar ni para entregar a un relevo, y su formato lo revisa el analista en MATU-54.
- No hay ruta `GET …/plan/exportar` ni acción de auditoría `plan.imprimir`.

**En la arquitectura:** RF-09 con el texto nuevo, sin la ruta de exportación de la ficha, y sin «versión imprimible» en el alcance ni en el calendario. Se consolida en la v1.2 (MATU-43).

**En el backlog:** la fila de RF-09 queda como quitada.

**En el ADR-028:** las secciones no se imprimen.

**En `lenguaje.md`:** salen los textos de la hoja impresa (sección 5.4).

**En `DISENO.md` (repositorio MATU_PROYECTO):** sale la pestaña «Para imprimir» de la ficha. La pestaña de la lista de reposición la especifica el diseñador en su historia.
