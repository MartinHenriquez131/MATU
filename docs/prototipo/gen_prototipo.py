"""
MATU · Generador del prototipo navegable.

Una sola fuente de pantallas produce dos archivos:
  prototipo-v1.1.html    versión documentada: todas las pantallas a la vista, con la decisión de diseño de cada una
  prototipo-pruebas.html versión para pruebas con usuarios: una pantalla a la vez, sin texto explicativo

    python gen_prototipo.py
"""
import pathlib

SALIDA = pathlib.Path(__file__).resolve().parents[1] / "docs"

# ---------------------------------------------------------------- iconos (SVG en línea)
def ico(nombre, tam=22):
    trazos = {
        "atras": '<path d="M15 5l-7 7 7 7"/>',
        "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "enlace": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
        "alerta": '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17.5v.01"/>',
        "impresora": '<path d="M7 9V4h10v5"/><rect x="4" y="9" width="16" height="7" rx="2"/><path d="M7 14h10v6H7z"/>',
        "doc": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>',
        "candado": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
        "ojo": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
        "camara": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
        "lista": '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
        "reloj": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
        "tienda": '<path d="M4 9l1.5-5h13L20 9M4 9v11h16V9M4 9h16"/><path d="M10 20v-5h4v5"/>',
    }[nombre]
    return (f'<svg class="ico" width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{trazos}</svg>')


def logo(tam=40):
    """Logo MATU: círculo blanco con un corazón turquesa simple."""
    return (f'<svg class="logo" width="{tam}" height="{tam}" viewBox="0 0 48 48" role="img" aria-label="MATU">'
            '<circle cx="24" cy="24" r="24" fill="#fff"/>'
            '<path d="M24 35.5s-11-6.6-11-14.2A6.2 6.2 0 0 1 24 17.6a6.2 6.2 0 0 1 11 3.7c0 7.6-11 14.2-11 14.2z" '
            'fill="#14b8a6"/></svg>')


# ---------------------------------------------------------------- piezas de interfaz
def hdr(titulo, atras=None, tipo="app"):
    b = f'<button class="back" data-go="{atras}" aria-label="Volver">{ico("atras")}</button>' if atras else ""
    return f'<div class="hdr {tipo}">{b}<div class="hi">{titulo}</div></div>'


def opciones(items, sel):
    return '<div class="opts">' + "".join(
        f'<button class="opt{" on" if i == sel else ""}" role="radio" aria-checked="{"true" if i == sel else "false"}">'
        f'<span class="dot"></span><span>{t}</span></button>' for i, t in enumerate(items)) + "</div>"


def chips(items, sel):
    return '<div class="chips">' + "".join(
        f'<button class="chip{" on" if i in sel else ""}">{t}</button>' for i, t in enumerate(items)) + "</div>"


def stepper(valor):
    return (f'<div class="stepper"><button class="st" data-d="-1" aria-label="Menos">−</button>'
            f'<span class="sv">{valor}</span><button class="st" data-d="1" aria-label="Más">+</button></div>')


def fila(principal, secundario="", etiqueta="", clase=""):
    sec = f'<span class="t2">{secundario}</span>' if secundario else ""
    tag = f'<span class="tag {clase}">{etiqueta}</span>' if etiqueta else ""
    return f'<div class="li {clase}"><span class="li-tx"><span class="t1">{principal}</span>{sec}</span>{tag}</div>'


def barra(pct):
    return f'<div class="bar" role="img" aria-label="{pct}% listo"><i style="width:{pct}%"></i></div>'


def btn(texto, go=None, sec=False):
    d = f' data-go="{go}"' if go else ""
    return f'<button class="{"btn2" if sec else "btn"}"{d}>{texto}</button>'


# ---------------------------------------------------------------- pantallas
# (id, recorrido, título corto, html, explicación para la versión documentada)
P = []


def pantalla(id_, recorrido, titulo, cuerpo, nota, tipo="app"):
    P.append(dict(id=id_, rec=recorrido, titulo=titulo, html=cuerpo, nota=nota, tipo=tipo))


R0, R1, R2, R3, R4, R5, R6 = ("0 · Bienvenida y alta", "1 · Ficha de relevo", "2 · Consumo y reposición",
                              "3 · Reparto y pago", "4 · Vista de comercio", "5 · Repartidor",
                              "6 · Errores y casos borde")

# ---- 0 · Bienvenida y alta
pantalla("f0-0", R0, "Bienvenida", f"""
<div class="splash-in">
  {logo(88)}
  <div class="wordmark">MATU</div>
  <p class="splash-tx">Que el cuidado no dependa de una sola persona.</p>
</div>
{btn("Empezar", "f0-1")}
<button class="link" data-go="f1-1">Ya tengo cuenta</button>
""", "Primera pantalla. Una promesa en una línea y una sola acción. La marca aparece completa solo aquí y en el inicio.", "splash")

pantalla("f0-1", R0, "A quién cuidas", hdr("¿A quién cuidas?", "f0-0") + f"""
<div class="body">
  <label class="q">¿Cómo se llama?</label>
  <input value="María Soto">
  <label class="q">¿Cuánto apoyo necesita en el día a día?</label>
  {opciones(["Se maneja sola, con supervisión", "Necesita apoyo en varias cosas", "Necesita apoyo en todo"], 1)}
  <label class="q">¿Dónde vive?</label>
  <input value="Los Aromos 123, La Reina">
  <p class="hint">No te preguntamos su diagnóstico. No lo necesitamos y no lo guardamos.</p>
</div>
{btn("Continuar", "f0-2")}
""", "Pide lo mínimo: nombre, nivel de apoyo y dirección. No pregunta diagnóstico, y lo dice (sección 11.3). MATU-07.")

pantalla("f0-2", R0, "Permiso", hdr("Un permiso necesario", "f0-1") + f"""
<div class="body">
  <p class="t2">Lo que anotes sobre el cuidado de María es información sensible. Para guardarla necesitamos saber en qué calidad nos das permiso.</p>
  {opciones(["Soy María y lo autorizo yo", "Soy su representante legal", "La cuido, sin representación legal"], 2)}
  <div class="note">
    <b>Qué significa lo que elegiste</b>
    Guardaremos la información con tu permiso de cuidadora. Podrás borrarla cuando quieras y te lo volveremos a preguntar en un año.
  </div>
</div>
{btn("Acepto y continúo", "f1-1")}
""", "Ley 21.719. Como la persona cuidada muchas veces no puede consentir, el sistema registra en qué calidad lo hace quien cuida y no lo disimula (sección 11.5). La persona y su consentimiento se guardan juntos o no se guarda nada (MATU-07).")

# ---- 1 · Ficha de relevo
pantalla("f1-1", R1, "Inicio", f"""
<div class="home-top">{logo(36)}<div><div class="hello">Hola, Carmen</div><div class="hello2">Cuidado de María</div></div></div>
<div class="body">
  <div class="card">
    <div class="row"><span class="t1">Ficha de relevo</span><span class="pill">1 de 3</span></div>
    {barra(33)}
    <p class="t2">Con lo que ya escribiste, alguien podría reemplazarte unas horas.</p>
    {btn("Completar la ficha", "f1-2")}
    {btn("Compartir con un relevo", "f1-5", True)}
  </div>
  <div class="card alert">
    <div class="row"><span class="t1">{ico("alerta", 20)} Se acaban los pañales</span></div>
    <p class="t2">Quedan para <b>6 días</b>. Te avisamos antes para que no te pille.</p>
    {btn("Ver qué reponer", "f2-2")}
  </div>
</div>
""", "<b>Cambia en v1.1:</b> el plan de cuidado pasa a ser la <b>ficha de relevo de tres campos</b> (ADR-023). Lo primero que ve la cuidadora es la ficha, no el catálogo. El avance se cuenta por campos: 1 de 3, no un porcentaje abstracto.")

pantalla("f1-2", R1, "Completar un campo", hdr("Ficha de María", "f1-1") + f"""
<div class="body">
  <p class="step">Campo 2 de 3</p>
  {barra(67)}
  <label class="q big-q">Si se altera</label>
  <p class="t2">¿Qué la calma cuando se angustia o se desorienta?</p>
  <textarea rows="4">Bajar las persianas y poner la radio bajito. No hablarle fuerte.</textarea>
  <p class="hint">Por ejemplo: «Le hace bien que le tomen la mano y le hablen de su pueblo».</p>
  <button class="mic">{ico("mic", 20)} Dictar en vez de escribir</button>
</div>
<div class="two">{btn("Después", "f1-1", True)}{btn("Guardar", "f1-3")}</div>
""", "<b>Cambia en v1.1:</b> de ocho preguntas a tres campos, con nombres tomados de las entrevistas: <b>Su día</b>, <b>Si se altera</b> y <b>A quién llamar</b>. Cada campo trae una pregunta guía y un ejemplo. Dictado por voz disponible. Hasta 500 caracteres (MATU-12).")

pantalla("f1-3", R1, "Guardado", hdr("Ficha de María", "f1-2") + f"""
<div class="body center">
  <div class="okmark">{ico("check", 34)}</div>
  <div class="t1 lg">Guardado</div>
  <p class="t2">Vas en 2 de 3. Puedes seguir cuando quieras, no se pierde nada.</p>
  {barra(67)}
</div>
<div class="two">{btn("Volver al inicio", "f1-1", True)}{btn("Ver mi ficha", "f1-4")}</div>
""", "Nada obligatorio de una sola vez. Salir a mitad de camino no pierde nada y no genera culpa (ADR-018).")

pantalla("f1-4", R1, "Tu ficha", hdr("Ficha de María", "f1-1") + f"""
<div class="body">
  {fila("Su día", "Despierta a las 8, desayuno a las 8:30...", "Listo", "done")}
  {fila("Si se altera", "Bajar las persianas y poner la radio...", "Listo", "done")}
  {fila("A quién llamar", "Todavía sin completar", "Falta")}
  <p class="hint">{ico("candado", 16)} Cada campo se guarda protegido. Puedes compartir solo algunos.</p>
</div>
{btn("Compartir con un relevo", "f1-5")}
<div class="two">{btn("Quién la vio", "f1-9", True)}{btn("Imprimir", "f1-11", True)}</div>
""", "<b>Cambia en v1.1:</b> tres filas en vez de seis secciones. El estado se dice con palabra (Listo, Falta) y no solo con color. El modo completo de ocho secciones queda anotado como <b>Podría</b>, para quien quiera escribir más.")

pantalla("f1-5", R1, "Compartir", hdr("Compartir la ficha", "f1-4") + f"""
<div class="body">
  <label class="q">¿Quién te va a reemplazar?</label>
  <input value="Rosa">
  <input value="+56 9 8765 4321" class="mt">
  <label class="q">¿Qué puede ver?</label>
  {chips(["Su día", "Si se altera", "A quién llamar"], {0, 1, 2})}
  <label class="q">¿Hasta cuándo?</label>
  {chips(["24 horas", "Fin de semana", "Otra fecha"], {0})}
</div>
{btn("Crear enlace", "f1-6")}
""", "<b>Cambia en v1.1:</b> se eligen los campos, quién reemplaza y hasta cuándo. <b>24 horas</b> viene marcado por defecto, con un máximo de 30 días. El acceso se puede crear aunque la ficha esté incompleta (MATU-18).")

pantalla("f1-6", R1, "Enlace y PIN", hdr("Enlace listo", "f1-5") + f"""
<div class="body center">
  <div class="okmark">{ico("enlace", 30)}</div>
  <div class="t1 lg">Listo para Rosa</div>
  <p class="t2">Vence mañana a las 14:30.</p>
  <div class="pinbox">
    <div class="t2">PIN para abrir la ficha</div>
    <div class="pin">4 8 2 1</div>
    <div class="t2"><b>Díctaselo por teléfono.</b> No lo mandes junto con el enlace. Solo lo verás ahora.</div>
  </div>
</div>
{btn("Enviar enlace por WhatsApp", "f1-7")}
""", "<b>Nuevo en v1.1:</b> el PIN de cuatro dígitos se muestra una sola vez para que la cuidadora lo dicte. Como viaja por un canal distinto del enlace, funciona como segundo factor sin depender de SMS (MATU-18).")

pantalla("f1-7", R1, "Relevo: PIN", hdr("Ficha de cuidado", tipo="web") + f"""
<div class="body center">
  <div class="okmark soft">{ico("candado", 28)}</div>
  <div class="t1 lg">Carmen te compartió la ficha de María</div>
  <p class="t2">Escribe el PIN que te dio por teléfono.</p>
  <input class="pin-in" value="4821" inputmode="numeric" aria-label="PIN">
</div>
{btn("Ver la ficha", "f1-8")}
""", "<b>Nuevo en v1.1:</b> página web sin cuenta y sin instalar nada. El enlace se canjea por una sesión corta y el token no queda en el historial del teléfono prestado (MATU-19 y MATU-23).", "web")

pantalla("f1-8", R1, "Relevo: ficha", hdr("Ficha de María", tipo="web") + f"""
<div class="body">
  <p class="hint">Compartida por Carmen · disponible hasta mañana 14:30</p>
  <div class="card">
    <div class="t1">Su día</div>
    <p class="t2"><b>08:00</b> Despierta sola. Le gusta que abran la cortina primero.<br>
    <b>08:30</b> Desayuno. Té con leche tibio, nunca caliente.<br>
    <b>16:00</b> Siesta corta, máximo una hora.</p>
  </div>
  <div class="card">
    <div class="t1">Si se altera</div>
    <p class="t2">Bajar las persianas y poner la radio bajito. No hablarle fuerte. Si pregunta por su marido, no corregirla: decirle que salió y ya vuelve.</p>
  </div>
  <div class="card muted">
    <div class="t1">A quién llamar</div>
    <p class="t2">Sin completar</p>
  </div>
  <p class="hint">Solo Carmen puede cambiar esta ficha.</p>
</div>
""", "<b>Cambia en v1.1:</b> se ven solo los campos habilitados y el nombre de pila. Un campo vacío dice «Sin completar» en vez de esconderse, para que el relevo sepa que falta. Texto escalable al 200% sin desplazamiento horizontal.", "web")

pantalla("f1-9", R1, "Quién la vio", hdr("Quién vio la ficha", "f1-4") + f"""
<div class="body">
  {fila("Rosa abrió la ficha", "Hoy, 14:20")}
  {fila("Rosa escribió mal el PIN", "Hoy, 14:18")}
  {fila("Enlace del fin de semana", "Venció el domingo")}
  <p class="hint">Nadie de MATU puede abrir la ficha. Si alguna vez pasara, aparecería aquí.</p>
</div>
{btn("Ver enlaces activos", "f1-10")}
""", "<b>Cambia en v1.1:</b> una línea por apertura, en lenguaje simple. En las entrevistas 5 de 10 dijeron que no mirarían esta pantalla, y quienes sí lo harían la ven como respaldo, no como seguridad. Se mantiene por cumplimiento (RF-08), simplificada.")

pantalla("f1-10", R1, "Cortar un acceso", hdr("Enlaces activos", "f1-9") + f"""
<div class="body">
  <div class="card">
    <div class="row"><span class="t1">Rosa</span><span class="pill">{ico("reloj", 14)} vence en 22 h</span></div>
    <p class="t2">Ve Su día, Si se altera y A quién llamar.</p>
    {btn("Cortar este enlace ahora", "f1-9", True)}
  </div>
  <p class="hint">Al cortarlo, el enlace deja de abrir de inmediato. Rosa no recibe aviso.</p>
</div>
""", "RF-07. La revocación es de un toque y tiene efecto en la siguiente apertura. La cuidadora no necesita entender qué es un token: el enlace deja de abrir (MATU-20).")

pantalla("f1-11", R1, "Para imprimir", hdr("Para imprimir", "f1-4") + f"""
<div class="body center">
  <div class="okmark">{ico("impresora", 30)}</div>
  <div class="t1 lg">La ficha de María en una hoja</div>
  <p class="t2">Su día, qué hacer si se altera y a quién llamar. Sin conexión y sin aplicación.</p>
  <p class="hint">Útil para dejarla en el refrigerador cuando llega alguien nuevo.</p>
</div>
{btn("Descargar", "f1-4", True)}
""", "RF-09, Debería. Varias cuidadoras ya tienen su propia hoja en el refrigerador o una pizarra. Esta pantalla respeta esa costumbre en vez de competir con ella.")

# ---- 2 · Consumo y reposición
pantalla("f2-1", R2, "Declarar consumo", hdr("¿Qué usa María?", "f2-2") + f"""
<div class="body">
  <div class="t1">Pañal adulto talla M</div>
  <label class="q">¿Cuántos usa al día?</label>
  {stepper(4)}
  <label class="q">¿Cuántos le quedan, más o menos?</label>
  {stepper(24)}
  <p class="hint">Te avisamos <b>7 días antes</b> de que se acaben. Puedes cambiarlo después.</p>
</div>
{btn("Guardar", "f2-2")}
""", "Dos números por producto y nada más (ADR-003). La capa 2 es la que más valor percibido tuvo en las entrevistas: tres personas condicionaron el pago a que resolviera los insumos.")

pantalla("f2-2", R2, "Qué se está acabando", hdr("Qué se está acabando", "f1-1") + f"""
<div class="body">
  {fila("Pañal adulto talla M", "Quedan 6 días", "Pronto", "urg")}
  {fila("Toallitas húmedas", "Quedan 11 días", "Atenta", "amb")}
  {fila("Suplemento vainilla", "Quedan 15 días", "Tranquila")}
  {fila("Crema protectora", "Quedan 40 días", "Tranquila")}
  <button class="link" data-go="f2-1">+ Agregar un producto</button>
</div>
<div class="two">{btn("Ya lo compré", "f2-4", True)}{btn("Qué reponer", "f2-3")}</div>
""", "Responde la pregunta de todas las semanas. Ordenada por urgencia, con lenguaje llano: «6 días», no «stock proyectado». El estado se dice con palabra además de color.")

pantalla("f2-3", R2, "Lista de reposición", hdr("Qué reponer", "f2-2") + f"""
<div class="body">
  {fila("Pañal adulto talla M x30", "", "2 paquetes", "done")}
  {fila("Toallitas húmedas x80", "", "1 paquete", "done")}
  <p class="hint">Con esto María queda cubierta unos 15 días.</p>
</div>
{btn("Pedir a domicilio · $48.990 aprox.", "f3-1")}
{btn("Enviar la lista por WhatsApp", "f2-5", True)}
""", "Decisión 2 de cabecera: la lista funciona sin ningún comercio en convenio. Si nunca hay convenio, MATU sigue siendo útil todos los meses (ADR-002).")

pantalla("f2-4", R2, "Ya lo compré", hdr("Ya lo compré", "f2-2") + f"""
<div class="body">
  <div class="t1">Pañal adulto talla M</div>
  <label class="q">¿Cuántos paquetes compraste?</label>
  {stepper(2)}
  <p class="hint">Ajustamos la cuenta: ahora te alcanza hasta el <b>8 de noviembre</b>.</p>
</div>
{btn("Guardar", "f2-2")}
""", "Sin esto el cálculo se desalinea y las alertas pierden credibilidad (RF-13).")

pantalla("f2-5", R2, "Lista enviada", hdr("Lista lista", "f2-3") + f"""
<div class="body center">
  <div class="okmark">{ico("doc", 30)}</div>
  <div class="t1 lg">Lista de María</div>
  <p class="t2">Pañal adulto talla M x30 · 2 paquetes<br>Toallitas húmedas x80 · 1 paquete</p>
  <p class="hint">Puedes mandársela a quien vaya a comprar.</p>
</div>
{btn("Volver al inicio", "f1-1", True)}
""", "Plan B del ADR-002 completo en una pantalla.")

# ---- 3 · Reparto y pago
pantalla("f3-1", R3, "Repartir el gasto", hdr("¿Quién paga?", "f2-3") + f"""
<div class="body">
  <div class="row"><span class="t1">Total estimado</span><span class="t1">$48.990</span></div>
  {chips(["Partes iguales", "Pago yo todo", "Personalizar"], {0})}
  {fila("Carmen (tú)", "", "$16.330")}
  {fila("Rodrigo", "", "$16.330")}
  {fila("Sofía", "", "$16.330")}
  <label class="check"><input type="checkbox" checked> Si alguien no paga a tiempo, lo cubro yo</label>
  <p class="hint">Les avisamos por la app. Tienen 2 horas para pagar su parte.</p>
</div>
{btn("Confirmar y pagar mi parte", "f3-2")}
""", "Nunca una pantalla en blanco: se parte de partes iguales. El respaldo viene marcado en quien crea el pedido. Ojo: H5 quedó no concluyente en las entrevistas, y este flujo depende de las cuatro entrevistas adicionales.")

pantalla("f3-2", R3, "La reserva", hdr("Tu parte", "f3-1") + f"""
<div class="body">
  <div class="row"><span class="t1">Tu parte</span><span class="t1">$16.330</span></div>
  <div class="note">
    <b>Vamos a reservar $18.780 en tu tarjeta.</b>
    Reservamos un poco más por si algún precio cambió. Se te cobrará solo lo que realmente cueste y el resto se libera solo.
  </div>
</div>
{btn("Pagar con tarjeta", "f3-3")}
""", "Momento difícil (a) de la sección 10.4: sin esta frase, la reserva mayor al cobro genera reclamos. Sin la palabra «autorización».")

pantalla("f3-3", R3, "Esperando a los demás", hdr("Pedido de María") + f"""
<div class="body">
  <div class="t1">Falta que pague 1 de 3</div>
  {fila("Carmen (tú)", "", "Pagado", "done")}
  {fila("Rodrigo", "", "Pagado", "done")}
  {fila("Sofía", "", "Esperando", "amb")}
  <p class="hint">Si Sofía no paga antes de las 16:40, <b>lo cubres tú</b> y el pedido sale igual.</p>
</div>
{btn("Ver el pedido", "f3-4", True)}
""", "El estado de la recaudación es visible y honesto, y el respaldo explica por qué el pedido no está en riesgo.")

pantalla("f3-4", R3, "Entregado", hdr("Pedido entregado") + f"""
<div class="body">
  <div class="card ok center"><div class="okmark">{ico("check", 30)}</div><div class="t1">Entregado a las 18:42</div></div>
  <div class="row"><span class="t2">Estimado</span><span class="t2">$48.990</span></div>
  <div class="row"><span class="t2">Reservado</span><span class="t2">$56.340</span></div>
  <div class="row"><span class="t1">Cobrado de verdad</span><span class="t1">$51.340</span></div>
  <p class="hint">Los $5.000 que sobraban de la reserva <b>ya se liberaron</b>. Tu parte fue de $17.114.</p>
  {fila("Toallitas x80", "Cambiada por otra marca", "Cambio", "amb")}
</div>
{btn("Volver al inicio", "f1-1", True)}
""", "La segunda mitad de la promesa de la reserva. Es la notificación que construye confianza.")

# ---- 4 · Comercio
pantalla("f4-1", R4, "Pedidos del día", hdr("Farmacia Los Aromos · Hoy", tipo="web") + f"""
<div class="body">
  {fila("#4821 · 6 productos", "Retiro entre 17:00 y 18:00", "Por preparar", "urg")}
  {fila("#4822 · 3 productos", "Retiro entre 18:00 y 19:00", "Preparando", "amb")}
  {fila("#4819 · 4 productos", "Retirado 15:20", "Listo", "done")}
</div>
{btn("Abrir pedido #4821", "f4-2")}
""", "Una pantalla, sin navegación ni aprendizaje previo, para un computador compartido en el local.", "web")

pantalla("f4-2", R4, "Preparar", hdr("Pedido #4821 · para María", "f4-1", "web") + f"""
<div class="body">
  <div class="row"><span class="t2">Tope autorizado</span><span class="t1">$56.340</span></div>
  {fila("Pañal adulto M x30 · 2 un.", "", "$27.980", "done")}
  {fila("Toallitas húmedas x80", "Acepta equivalente hasta +10%", "Sin stock", "urg")}
</div>
<div class="two">{btn("No disponible", "f4-3", True)}{btn("Reemplazar", "f4-3")}</div>
""", "El comercio resuelve los faltantes contra las reglas que dejó la familia. Ve el nombre de pila, nunca la dirección.", "web")

pantalla("f4-3", R4, "Monto real", hdr("Cerrar pedido #4821", "f4-2", "web") + f"""
<div class="body">
  <label class="q">Total de la boleta</label><input value="$51.340">
  <label class="q">N° de boleta</label><input value="0084512">
  <p class="hint">Dentro del tope autorizado ($56.340). Se carga a la cuenta de MATU.</p>
</div>
{btn("Listo para retiro", "f4-4")}
""", "El monto real se conoce antes del retiro, así el tiempo en el local es de minutos.", "web")

pantalla("f4-4", R4, "Validar código", hdr("Entregar #4821", "f4-3", "web") + f"""
<div class="body">
  <label class="q">Código que muestra quien retira</label>
  <input class="pin-in" value="4729">
  <div class="card ok center"><div class="okmark">{ico("check", 28)}</div><div class="t1">Código válido</div></div>
</div>
{btn("Volver a los pedidos", "f4-1", True)}
""", "Credencial de un solo uso que vence en 90 minutos. En el MVP el retiro y la entrega se marcan desde esta vista (recorte de la sección 15.3).", "web")

# ---- 5 · Repartidor
pantalla("f5-1", R5, "Oferta", hdr("Nueva oferta", tipo="dark") + f"""
<div class="body">
  <div class="card dark">
    <span class="timer">58 s</span>
    <div class="t1">Farmacia Los Aromos</div>
    <p class="t2">Retirar preparado · 6 productos</p>
    <div class="row"><span class="t2">Distancia</span><span class="t1">2,4 km</span></div>
    <div class="row"><span class="t2">Pagas</span><span class="t1">nada</span></div>
    <div class="row"><span class="t2">Ganas</span><span class="t1">$3.200</span></div>
  </div>
</div>
<div class="two">{btn("Rechazar", "f5-1", True)}{btn("Aceptar", "f5-2")}</div>
""", "<b>Debería</b> tras el recorte de la sección 15.3: se construye solo si hay holgura. Se ofrece con 60 segundos, no se adjudica (ADR-010).", "dark")

pantalla("f5-2", R5, "Código de retiro", hdr("Pedido #4821", tipo="dark") + f"""
<div class="body">
  <div class="card dark center"><p class="t2">Muestra este código en caja</p><div class="pin light">4 7 2 9</div><p class="t2">Vence en 74 minutos</p></div>
  <div class="card dark"><div class="t1">Farmacia Los Aromos</div><p class="t2">Av. Larraín 1450 · caja 3</p></div>
</div>
{btn("Ya lo retiré", "f5-3")}
""", "Quien reparte no compra ni paga: solo muestra el código (ADR-009).", "dark")

pantalla("f5-3", R5, "Entrega", hdr("Entregar", "f5-2", "dark") + f"""
<div class="body">
  <div class="card dark"><div class="t1">María · Depto 402</div><p class="t2">Los Cerezos 233 · timbre 402</p><p class="t2">Contacto: +56 9 •••• 4412</p></div>
  <div class="two">{btn(ico("camara", 18) + " Boleta", None, True)}{btn(ico("camara", 18) + " Entrega", None, True)}</div>
</div>
{btn("Confirmar entrega", "f5-1")}
""", "Evidencia con foto. Quien reparte no ve nada de la ficha, y eso lo garantiza el modelo de datos, no un permiso.", "dark")

# ---- 6 · Errores y casos borde
pantalla("f6-1", R6, "Todavía no hay nada", hdr("Qué se está acabando", "f1-1") + f"""
<div class="body center">
  <div class="okmark soft">{ico("lista", 30)}</div>
  <div class="t1 lg">Aún no sabemos qué usa María</div>
  <p class="t2">Cuéntanos de un solo producto, el que más te preocupa. Con eso ya te podemos avisar antes de que se acabe.</p>
</div>
{btn("Empezar por los pañales", "f2-1")}
{btn("Después", "f1-1", True)}
""", "Estado vacío: propone la acción más barata y dice qué gana la persona si la hace.")

pantalla("f6-2", R6, "Alguien más editó", hdr("Dos versiones", "f1-2") + f"""
<div class="body">
  <div class="card alert"><div class="t1">{ico("alerta", 20)} Rodrigo editó esto mientras escribías</div><p class="t2">No queremos borrar lo de nadie. Elige cuál dejar.</p></div>
  <div class="card"><div class="t2">Lo de Rodrigo · 14:20</div><p class="t1n">Bajar las persianas. Si sigue inquieta, llamar a la nieta.</p>{btn("Dejar esta", "f1-3", True)}</div>
  <div class="card"><div class="t2">Lo tuyo · ahora</div><p class="t1n">Bajar las persianas y poner la radio bajito. No hablarle fuerte.</p>{btn("Dejar la mía", "f1-3")}</div>
</div>
""", "El 412 del bloqueo optimista hecho pantalla (RF-04, MATU-13). No se fusiona texto automáticamente.")

pantalla("f6-3", R6, "El pago no pasó", hdr("Tu parte", "f3-2") + f"""
<div class="body">
  <div class="card alert center"><div class="okmark warn">{ico("alerta", 28)}</div><div class="t1">El banco no aprobó el pago</div><p class="t2">Puede ser el cupo o un bloqueo del banco. No se te cobró nada.</p></div>
  <p class="hint">Si nadie paga antes de las 16:40, el pedido se cancela solo y se libera lo reservado. Nadie pierde dinero.</p>
</div>
{btn("Probar con otra tarjeta", "f3-2")}
{btn("Que lo cubra Rodrigo", "f3-3", True)}
""", "Error de pago sin culpar a la persona ni usar jerga de pasarela.")

pantalla("f6-4", R6, "Relevo: PIN incorrecto", hdr("Ficha de cuidado", tipo="web") + f"""
<div class="body center">
  <div class="okmark warn">{ico("candado", 28)}</div>
  <div class="t1 lg">Ese PIN no es</div>
  <p class="t2">Revisa los cuatro números que te dio Carmen. Te quedan <b>3 intentos</b>.</p>
  <input class="pin-in err" value="4812" aria-invalid="true" aria-label="PIN">
</div>
{btn("Intentar de nuevo", "f1-7")}
""", "<b>Nuevo en v1.1:</b> el error dice cuántos intentos quedan. Después de cinco el enlace se bloquea (MATU-19).", "web")

pantalla("f6-5", R6, "Relevo: enlace no disponible", hdr("Ficha de cuidado", tipo="web") + f"""
<div class="body center">
  <div class="okmark soft">{ico("reloj", 30)}</div>
  <div class="t1 lg">Este enlace ya no está disponible</div>
  <p class="t2">Puede que haya vencido, que lo hayan cortado o que el PIN se haya escrito mal varias veces.</p>
  <div class="note left"><b>¿Qué hago?</b>Pídele a quien te envió el enlace uno nuevo.</div>
</div>
""", "<b>Nuevo en v1.1:</b> vencido, revocado y bloqueado comparten pantalla y acción. Para el relevo la causa da igual: lo que necesita es saber qué hacer.", "web")

pantalla("f6-6", R6, "Texto al 200%", hdr("Se acaban", "f2-2") + f"""
<div class="body xl">
  <div class="card"><div class="t1">Pañales</div><p class="t2">Quedan 6 días</p>{btn("Ver qué reponer", "f2-3")}</div>
  <p class="hint">Los botones siguen siendo tocables y el texto no se corta.</p>
</div>
""", "Criterio de la sección 10.3: todo funciona con el texto al doble.")


# ---------------------------------------------------------------- estilos comunes
CSS_BASE = """
:root{--tq:#0f766e;--tq-marca:#14b8a6;--tq-claro:#e8f6f4;--sup:#f4faf9;--tinta:#13292c;--suave:#475b5f;
--linea:#dbe7e5;--rojo:#b42318;--rojo-f:#fdecea;--ambar:#8a5200;--ambar-f:#fff4e0;--radio:14px}
*{box-sizing:border-box;margin:0;padding:0}
body{color:var(--tinta);font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
button{font:inherit;cursor:pointer}
.ico{flex:0 0 auto;vertical-align:-4px}
.phone{background:#fff;display:flex;flex-direction:column;overflow:hidden}
.phone>.btn,.phone>.btn2,.phone>.two,.phone>.link{margin:0 18px;width:auto;flex:0 0 auto}
.phone>.btn:last-child,.phone>.btn2:last-child,.phone>.two:last-child,.phone>.link:last-child{margin-bottom:18px}
.phone>*+.btn,.phone>*+.btn2,.phone>*+.two,.phone>*+.link{margin-top:10px}
.phone .body{padding:16px 18px;display:flex;flex-direction:column;gap:10px;flex:1}
.phone .body.center{text-align:center;align-items:center;justify-content:center}
.sbar{display:flex;justify-content:space-between;font-size:12px;font-weight:600;padding:8px 20px 2px;color:var(--tinta)}
.phone.splash .sbar,.phone.dark .sbar{color:#fff}
.hdr{display:flex;align-items:center;gap:4px;min-height:56px;padding:4px 10px 4px 18px;border-bottom:1px solid var(--linea)}
.hdr .back+.hi{margin-left:-4px}
.hdr.web{background:var(--sup)}
.hdr.dark{background:#10201f;border-color:#10201f}
.hdr.dark .hi{color:#fff}
.hi{font-weight:650;font-size:17px;letter-spacing:-.01em}
.back{background:none;border:0;color:var(--tq);min-width:44px;min-height:48px;margin-left:-10px;display:flex;align-items:center;justify-content:center}
.home-top{display:flex;align-items:center;gap:12px;background:var(--tq);color:#fff;padding:14px 18px 18px}
.hello{font-weight:700;font-size:20px;letter-spacing:-.02em}
.hello2{font-size:14px;opacity:.92}
.splash-in{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:30px;text-align:center}
.phone.splash{background:var(--tq)}
.phone.dark{background:#10201f;color:#fff}
.phone.splash .btn{background:#fff;color:var(--tq)}
.phone.splash .link{color:#fff}
.wordmark{color:#fff;font-size:34px;font-weight:800;letter-spacing:.14em}
.splash-tx{color:#fff;font-size:18px;max-width:240px}
.card{background:var(--sup);border:1px solid var(--linea);border-radius:var(--radio);padding:14px;display:flex;flex-direction:column;gap:6px}
.card.alert{background:var(--rojo-f);border-color:#f5c2bc}
.card.ok{background:var(--tq-claro);border-color:#bfe6e1}
.card.muted{background:#fff;border-style:dashed}
.card.dark{background:#1b2e2d;border-color:#1b2e2d;color:#fff}
.card.dark .t2{color:#cfe0de}
.card.center,.center{text-align:center;align-items:center}
.t1{font-weight:650;font-size:16px;display:flex;align-items:center;gap:6px}
.card.center .t1,.body.center .t1{justify-content:center}
.t1.lg{font-size:20px;letter-spacing:-.02em}
.t1n{font-size:15.5px}
.t2{color:var(--suave);font-size:15px}
.row{display:flex;justify-content:space-between;align-items:center;gap:8px}
.pill{background:var(--tq-claro);color:var(--tq);font-size:13px;font-weight:700;padding:3px 10px;border-radius:20px;display:inline-flex;gap:4px;align-items:center}
.bar{height:8px;background:var(--linea);border-radius:6px;overflow:hidden;width:100%}
.bar i{display:block;height:100%;background:var(--tq-marca);border-radius:6px}
.btn,.btn2{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;min-height:50px;border-radius:12px;font-size:16px;font-weight:650;padding:12px 14px}
.btn{background:var(--tq);color:#fff;border:0}
.btn2{background:#fff;color:var(--tq);border:1.5px solid var(--tq)}
.card .btn,.card .btn2{margin-top:4px}
.card.dark .btn2,.phone.dark .btn2{background:transparent;color:#7ee0d4;border-color:#7ee0d4}
.link{background:none;border:0;color:var(--tq);font-weight:650;min-height:48px;width:100%}
.two{display:flex;gap:10px}
.two>*{flex:1}
.q{display:block;font-size:15px;font-weight:650;margin-top:4px}
.q.big-q{font-size:20px;letter-spacing:-.02em;margin-top:0}
input,textarea{width:100%;border:1.5px solid var(--linea);border-radius:12px;padding:12px;font:inherit;font-size:16px;min-height:50px;background:#fff;color:var(--tinta)}
input:focus,textarea:focus{outline:3px solid var(--tq-claro);border-color:var(--tq)}
textarea{resize:none}
.mt{margin-top:-2px}
.mic{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;background:var(--tq-claro);border:0;border-radius:12px;color:var(--tq);font-weight:650;font-size:15px}
.step{font-size:14px;color:var(--suave);font-weight:600}
.hint{font-size:14px;color:var(--suave);line-height:1.45;display:block}
.note{background:var(--tq-claro);border-radius:12px;padding:12px 14px;font-size:15px;color:var(--tinta)}
.note b{display:block;margin-bottom:3px}
.note.left{text-align:left}
.li{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 14px;background:#fff;border:1px solid var(--linea);border-radius:12px;min-height:52px}
.li-tx{display:flex;flex-direction:column;min-width:0}
.li .t1{font-size:15.5px}
.li .t2{font-size:14px}
.li.urg{border-left:4px solid var(--rojo)}
.li.amb{border-left:4px solid #e0a100}
.li.done{border-left:4px solid var(--tq-marca)}
.tag{flex:0 0 auto;background:#eef3f2;color:var(--suave);font-size:13px;font-weight:650;padding:4px 10px;border-radius:20px}
.tag.urg{background:var(--rojo-f);color:var(--rojo)}
.tag.amb{background:var(--ambar-f);color:var(--ambar)}
.tag.done{background:var(--tq-claro);color:var(--tq)}
.opts{display:flex;flex-direction:column;gap:8px}
.opt{display:flex;align-items:center;gap:12px;text-align:left;background:#fff;border:1.5px solid var(--linea);border-radius:12px;padding:12px 14px;min-height:52px;font-size:15.5px;color:var(--tinta)}
.opt .dot{width:20px;height:20px;border-radius:50%;border:2px solid #9bb0ad;flex:0 0 auto}
.opt.on{border-color:var(--tq);background:var(--tq-claro)}
.opt.on .dot{border:6px solid var(--tq)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{background:#fff;border:1.5px solid var(--linea);border-radius:24px;padding:8px 14px;min-height:44px;font-size:15px;font-weight:600;color:var(--suave)}
.chip.on{background:var(--tq);border-color:var(--tq);color:#fff}
.check{display:flex;gap:10px;align-items:center;font-size:15px;min-height:48px}
.check input{width:22px;height:22px;min-height:22px;accent-color:var(--tq)}
.stepper{display:flex;align-items:center;gap:14px}
.stepper .st{width:50px;height:50px;border-radius:12px;border:1.5px solid var(--tq);background:#fff;color:var(--tq);font-size:24px;font-weight:700}
.stepper .sv{font-size:24px;font-weight:700;min-width:44px;text-align:center}
.okmark{width:64px;height:64px;border-radius:50%;background:var(--tq);color:#fff;display:flex;align-items:center;justify-content:center;margin:4px auto}
.okmark.soft{background:var(--tq-claro);color:var(--tq)}
.okmark.warn{background:var(--rojo-f);color:var(--rojo)}
.pinbox{background:var(--sup);border:1.5px dashed var(--tq);border-radius:var(--radio);padding:14px;margin-top:6px;display:flex;flex-direction:column;gap:6px;width:100%}
.pin{font-size:38px;font-weight:800;letter-spacing:.18em;color:var(--tq)}
.pin.light{color:#fff}
.pin-in{font-size:30px;font-weight:700;letter-spacing:.4em;text-align:center;max-width:220px}
.pin-in.err{border-color:var(--rojo);color:var(--rojo)}
.timer{align-self:flex-start;background:var(--rojo);color:#fff;font-weight:700;font-size:13px;padding:4px 12px;border-radius:20px}
.body.xl{font-size:170%}
.body.xl .t1{font-size:28px}.body.xl .t2{font-size:24px}.body.xl .btn{font-size:24px;min-height:64px}
"""

JS_INTERACCION = """
document.addEventListener('click',function(e){
  var o=e.target.closest('.opt');if(o){o.parentNode.querySelectorAll('.opt').forEach(function(x){x.classList.remove('on');x.setAttribute('aria-checked','false')});o.classList.add('on');o.setAttribute('aria-checked','true')}
  var c=e.target.closest('.chip');if(c){c.classList.toggle('on')}
  var s=e.target.closest('.st');if(s){var v=s.parentNode.querySelector('.sv');v.textContent=Math.max(0,parseInt(v.textContent,10)+parseInt(s.dataset.d,10))}
});
"""


def sbar(tipo):
    return '<div class="sbar"><span>9:41</span><span>●●● ▮</span></div>'


def telefono(p):
    return f'<div class="phone {p["tipo"]}" aria-label="{p["titulo"]}">{sbar(p["tipo"])}{p["html"]}</div>'


# ---------------------------------------------------------------- versión documentada
def version_documentada():
    css = CSS_BASE + """
body{background:#f6f8f8;padding:0 0 80px}
.top{background:var(--tq);color:#fff;padding:28px 24px 30px}
.top-in{max-width:1360px;margin:0 auto;display:flex;gap:18px;align-items:center}
.top h1{font-size:30px;letter-spacing:-.03em}
.top p{opacity:.92;font-size:15px}
.wrap{max-width:1360px;margin:0 auto;padding:0 24px}
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:24px 0 8px}
.lg-c{background:#fff;border:1px solid var(--linea);border-radius:16px;padding:16px 18px;font-size:14.5px;color:var(--suave)}
.lg-c h3{font-size:15px;color:var(--tinta);margin-bottom:6px}
.lg-c ul{margin-left:18px}
.lg-c li{margin:3px 0}
.lg-c b{color:var(--tinta)}
.sw{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-1px;margin-right:4px}
h2{font-size:21px;letter-spacing:-.02em;margin:36px 0 14px;display:flex;align-items:center;gap:10px}
h2 span{font-size:13px;font-weight:600;color:var(--tq);background:var(--tq-claro);padding:3px 10px;border-radius:20px}
.grid{display:flex;gap:22px;overflow-x:auto;padding:4px 2px 14px}
.unit{flex:0 0 auto;width:320px}
.scr-t{font-size:12.5px;text-transform:uppercase;letter-spacing:.09em;color:var(--suave);font-weight:700;margin-bottom:8px}
.unit .phone{width:320px;min-height:600px;border-radius:30px;border:1px solid #d5e2e0;box-shadow:0 10px 30px rgba(15,118,110,.08)}
.cap{font-size:13.5px;color:var(--suave);margin-top:12px;line-height:1.5}
.cap b{color:var(--tinta)}
.pend{border:1.5px dashed #9bb0ad;border-radius:16px;padding:14px 16px;margin-top:10px;font-size:14px;color:var(--suave);background:#fff}
@media(max-width:640px){.grid{flex-direction:column;align-items:center}}
"""
    recorridos = []
    for p in P:
        if p["rec"] not in recorridos:
            recorridos.append(p["rec"])
    secciones = []
    for r in recorridos:
        ps = [p for p in P if p["rec"] == r]
        unidades = "".join(
            f'<div class="unit" id="{p["id"]}"><div class="scr-t">{p["titulo"]}</div>{telefono(p)}'
            f'<div class="cap">{p["nota"]}</div></div>' for p in ps)
        extra = ""
        if r == R1:
            extra = ('<div class="pend"><b>Anotado como Podría, sin pantalla todavía:</b> modo completo de ocho secciones '
                     'para quien quiera escribir más, y modo asistido, en que otra persona lee las preguntas y escribe '
                     '(pedido en la entrevista E64).</div>')
        secciones.append(f'<h2>{r} <span>{len(ps)} pantallas</span></h2><div class="grid">{unidades}</div>{extra}')

    leyenda = f"""
<div class="legend">
 <div class="lg-c"><h3>Cómo leer esto</h3>Cada tarjeta es una pantalla. Los botones navegan de verdad: haz clic y el
 prototipo te lleva a la pantalla siguiente. Bajo cada pantalla está la decisión de diseño que la explica, con la
 historia o el requisito que la respalda.</div>
 <div class="lg-c"><h3>Qué cambia en la v1.1</h3><ul>
  <li><b>Plan de cuidado → ficha de relevo de tres campos</b> (ADR-023, H1 refutada con 3 de 10)</li>
  <li>Compartir con PIN que se dicta por teléfono, vigencia de 24 h por defecto</li>
  <li>Vista del relevo con PIN, campos vacíos visibles y tres estados de error</li>
  <li>«Quién vio la ficha» simplificado a una línea por apertura</li>
  <li>Alta con dirección y sin edad ni diagnóstico</li>
  <li>Identidad visual nueva: blanco y turquesa, logo MATU</li></ul></div>
 <div class="lg-c"><h3>Criterios en todas las pantallas</h3><ul>
  <li>Área táctil de 48 × 48 px o más, texto base de 17 px</li>
  <li>Contraste medido: tinta 15,2:1 · texto secundario 7,2:1 · turquesa <code>#0f766e</code> 5,5:1 sobre blanco y con texto blanco · rojo 6,6:1</li>
  <li>El turquesa de marca <code>#14b8a6</code> solo decora (logo y barras), nunca lleva texto: daría 2,5:1</li>
  <li>Ningún estado se marca solo con color, y el lenguaje no usa jerga clínica ni de expediente</li></ul></div>
 <div class="lg-c"><h3>Lo que este prototipo no es</h3>No es el diseño final ni tiene estado: define estructura,
 lenguaje y recorridos. Para las pruebas con usuarios existe <b>prototipo-pruebas.html</b>, la misma interfaz sin
 este texto. Las pruebas de usabilidad con usuarios reales <b>no se han ejecutado</b>.</div>
</div>"""

    js = JS_INTERACCION + """
document.addEventListener('click',function(e){var b=e.target.closest('[data-go]');if(!b)return;
var t=document.getElementById(b.dataset.go);if(!t)return;
t.scrollIntoView({behavior:'smooth',block:'center',inline:'center'});
t.querySelector('.phone').animate([{boxShadow:'0 0 0 0 rgba(20,184,166,.6)'},{boxShadow:'0 0 0 14px rgba(20,184,166,0)'}],{duration:900});});
"""
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>MATU — Prototipo navegable v1.1</title>
<style>{css}</style></head><body>
<header class="top"><div class="top-in">{logo(56)}<div><h1>MATU · Prototipo navegable v1.1</h1>
<p>{len(P)} pantallas en siete recorridos · ajustado al cierre del ADR-023 y a las 10 entrevistas · Jorge Espinoza y Martín Henríquez · octubre 2026</p></div></div></header>
<div class="wrap">{leyenda}{''.join(secciones)}</div>
<script>{js}</script></body></html>"""
    (SALIDA / "prototipo-v1.1.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- versión para pruebas
def version_pruebas():
    css = CSS_BASE + """
html,body{height:100%}
body{background:#dfeeec;display:flex;align-items:center;justify-content:center;min-height:100vh}
.stage{width:390px;height:800px;max-height:calc(100vh - 32px);border-radius:40px;overflow:hidden;
 box-shadow:0 20px 60px rgba(15,60,56,.25);background:#fff;position:relative}
.stage .phone{position:absolute;inset:0;display:none;overflow-y:auto}
.stage .phone.vis{display:flex}
@media(max-width:500px){body{display:block;background:#fff}.stage{width:100%;height:100vh;max-height:none;border-radius:0;box-shadow:none}}
#menu{position:fixed;top:12px;left:12px;background:#fff;border-radius:14px;box-shadow:0 8px 30px rgba(0,0,0,.18);
 padding:12px;width:250px;font-size:14px;display:none;z-index:9;max-height:90vh;overflow:auto}
#menu.vis{display:block}
#menu b{display:block;margin:8px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--suave)}
#menu button{display:block;width:100%;text-align:left;background:none;border:0;padding:6px 8px;border-radius:8px;color:var(--tinta);font-size:14px}
#menu button:hover{background:var(--tq-claro)}
"""
    pantallas = "".join(f'<div id="{p["id"]}" class="phone {p["tipo"]}">{sbar(p["tipo"])}{p["html"]}</div>' for p in P)
    tareas = [("Inicio de la app", "f0-0"), ("Tarea 1 · Completar la ficha", "f1-1"),
              ("Tarea 2 · Compartir con un relevo", "f1-4"), ("Tarea 3 · Declarar consumo", "f6-1"),
              ("Tarea 4 · Pedido desde la lista", "f2-2"), ("Vista del relevo", "f1-7"),
              ("Vista de comercio", "f4-1"), ("Repartidor", "f5-1")]
    menu = ("<div id='menu' role='dialog' aria-label='Menú de facilitación'><b>Ir a</b>"
            + "".join(f"<button data-go='{g}'>{t}</button>" for t, g in tareas)
            + "<b>Pantallas</b>" + "".join(f"<button data-go='{p['id']}'>{p['id']} · {p['titulo']}</button>" for p in P)
            + "</div>")
    js = JS_INTERACCION + """
var ids=[].map.call(document.querySelectorAll('.stage .phone'),function(x){return x.id});
var original=document.querySelector('.stage').innerHTML;
function mostrar(id){if(ids.indexOf(id)<0)id='f0-0';
 document.querySelectorAll('.stage .phone').forEach(function(x){x.classList.toggle('vis',x.id===id)});
 var v=document.getElementById(id);v.scrollTop=0;if(location.hash!=='#'+id)history.replaceState(null,'','#'+id)}
document.addEventListener('click',function(e){var b=e.target.closest('[data-go]');if(!b)return;
 mostrar(b.dataset.go);document.getElementById('menu').classList.remove('vis')});
document.addEventListener('keydown',function(e){if(e.key==='m'&&!/input|textarea/i.test(e.target.tagName))
 document.getElementById('menu').classList.toggle('vis');
 if(e.key==='r'&&!/input|textarea/i.test(e.target.tagName)){document.querySelector('.stage').innerHTML=original;mostrar('f0-0')}});
window.addEventListener('hashchange',function(){mostrar(location.hash.slice(1))});
if(/facilitador/.test(location.search))document.getElementById('menu').classList.add('vis');
mostrar(location.hash.slice(1));
"""
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>MATU</title>
<style>{css}</style></head><body>
<div class="stage">{pantallas}</div>{menu}
<script>{js}</script></body></html>"""
    (SALIDA / "prototipo-pruebas.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    version_documentada()
    version_pruebas()
    print(f"{len(P)} pantallas · prototipo-v1.1.html y prototipo-pruebas.html escritos")
