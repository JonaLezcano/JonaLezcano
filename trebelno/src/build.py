# Genera los 4 documentos de la campaña Agenda 2027 de Trebelno Recepciones:
# 00 Estrategia y campaña · 01 Guiones · 02 Plan de grabación · 03 Plan de edición
import re, pathlib
from datos import CREATIVOS, VARIABLES

AQUI = pathlib.Path(__file__).parent
CSS = (AQUI / "estilo.css").read_text(encoding="utf-8")
FECHA = "v3 · 15 de noviembre de 2026"
SRC = {"G": "GRABAR", "A": "ARCHIVO", "IA": "IA"}

def v(t):
    t = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="var">\1</span>', t)
    return t.replace("[VALIDAR]", '<span class="validar">[VALIDAR]</span>')

def chips(f):
    return "".join(f'<span class="src {p}">{SRC[p]}</span>' for p in f.split("+"))

DOCS = [("00","Estrategia y campaña","Para Jona y el cliente"),("01","Guiones","Para quien pone la cara"),
        ("02","Plan de grabación","Para Javi · filmmaker"),("03","Plan de edición","Para Javi · editor")]

def cabecera(n, titulo, bajada, para):
    idx = "".join(f'<div class="{"on" if d==n else ""}"><span class="mini">{d}</span><b>{t}</b><span class="mini">{p}</span></div>' for d,t,p in DOCS)
    return f"""<div class="doc"><div class="num"><small>Trebelno · Agenda 2027</small><b>{n}</b><small>{DOCS[int(n)][1]}</small></div>
    <div class="tit"><span class="chip eco">Campaña Meta Ads · Agenda 2027</span><h1>{titulo}</h1><p>{bajada}</p>
    <div class="meta"><span>Para: <b>{para}</b></span><span>Versión: <b>{FECHA}</b></span><span>Dirección: <b>Jona</b></span><span>Rodaje y edición: <b>Javi</b></span></div></div></div>
    <div class="indice">{idx}</div>"""

def pagina(*partes):
    return '<section class="page">' + "".join(partes) + "</section>"

def documento(titulo, cuerpo):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{titulo}</title><style>{CSS}</style></head><body>{cuerpo}</body></html>'

# ======================================================================
# 00 · ESTRATEGIA Y CAMPAÑA
# ======================================================================
def doc00():
    filas = "".join(f"""<tr><td class="n">{c['n']}</td><td><span class="chip {'eco' if c['tipo']=='eco' else 'nuevo'}">{'Ganador' if c['tipo']=='eco' else 'Nuevo'}</span><br>{c['angulo']}</td>
      <td><b>{v(c['titulo'])}</b></td><td>{v(c['gancho'][1])}</td><td>{'A' if c['tipo']=='eco' else 'B'}</td></tr>""" for c in CREATIVOS)
    p1 = pagina(cabecera("00","De dónde partimos, qué está funcionando y cómo invertimos USD 20 por día",
        "Resumen de la estrategia, la investigación de la competencia y la estructura de la campaña. Los guiones, el plan de grabación y el de edición van en documentos aparte.","Jona · cliente"),
    """<div class="sec"><span class="n">1</span><h2>Punto de partida</h2><span class="r">Test 1</span></div>
    <div class="grid g4">
      <div class="card"><span class="lbl">Invertido</span><span class="big" style="font-size:17pt">≈ USD 156</span><br><span class="mini">52% de ≈ USD 300 · a confirmar</span></div>
      <div class="card"><span class="lbl">Mensajes</span><span class="big">325</span><br><span class="mini">≈ USD 0,48 por conversación</span></div>
      <div class="card"><span class="lbl">Venta cerrada</span><span class="big">$13M</span><br><span class="mini">pagadera en 12 cuotas</span></div>
      <div class="card oro"><span class="lbl">Ángulo ganador</span><span class="serif" style="font-size:12.5pt">Oferta económica</span><br><span class="mini">cuotas · precio accesible</span></div>
    </div>
    <p class="mini" style="margin-top:4px">Con un presupuesto de USD 20 por día, lo más probable es que los ≈ USD 300 fueran el total del test (unos 15 días) y que se haya invertido el 52%. Si en cambio se invirtieron USD 300, el costo fue ≈ USD 0,92 por conversación. Lo confirmamos en el Administrador de anuncios: ese costo es la vara de las reglas de la página siguiente.</p>
    <div class="grid g3" style="margin-top:6px">
      <div class="card"><span class="lbl">Lo que funcionó</span>Hablar de plata sin vueltas. Una fiesta de $13M se vende cuando se la piensa como cuota y con la fecha asegurada.</div>
      <div class="card"><span class="lbl">Lo que renovamos</span>El contenido, que ahora producimos nosotros: persona a cámara, archivo de fiestas reales, testimonios de madres y quinceañeras, y oferta all inclusive en <b>hasta 24 cuotas fijas</b>.</div>
      <div class="card"><span class="lbl">Lo que sumamos</span>Dos ángulos nuevos: <b>visita al salón</b> (lo que Jano's sostiene con «Open Jano's») y <b>empatía</b>: el anfitrión/a le habla a quien sabe que la cosa está difícil.</div>
    </div>
    <div class="sec" style="margin-top:12px"><span class="n">2</span><h2>Qué está funcionando hoy</h2><span class="r">Competencia · nov 2026</span></div>
    <div class="grid g2">
      <div class="card"><span class="lbl">Jano's Eventos · el líder local</span><ul class="lim">
        <li>≈ 226 anuncios activos en tres páginas con el nombre Jano's/Janos (más una página aparte para empresas).</li>
        <li>Suben tandas de 15 a 20 anuncios el mismo día: prueban por volumen y dejan los que ganan.</li>
        <li>Todos llevan a conversación: «Escribinos y conocé el paquete ideal para vos», «Consultá por disponibilidad HOY».</li>
        <li>Paquetes por niveles (All inclusive, VIP y Ultra VIP) y jornadas «Open Jano's» para conocer el salón.</li>
        <li>Financiación con anticipo y cuotas, con la fecha y el valor fijados al contratar (según notas de años anteriores).</li></ul></div>
      <div class="card"><span class="lbl">Mercado y tendencias</span><ul class="lim">
        <li>Los salones chicos pautan placas con precio y «fechas disponibles», casi sin personas a cámara: <b>esa es nuestra ventaja</b>.</li>
        <li>Argentina: los 15 se reservan hasta con 3 años de anticipación, y lo más usado es congelar el precio con un anticipo.</li>
        <li>Afuera: video vertical de recorrido para atraer y testimonio para retargeting (caso de Meta Wedding Park: +90% de conversiones); paquete con precio cerrado y carrusel (caso Hermozo: 4 veces más reservas por mes).</li>
        <li>Renovar los creativos cada 2 a 4 semanas.</li></ul></div>
    </div>
    <p class="fuente" style="margin-top:5px">Fuentes: Biblioteca de anuncios de Meta (15/11/2026) · janoseventos.com · cronista.com (congelar precios de 15 y casamientos) · viapais.com.ar · iprofesional.com · casestudies.com (Facebook: Wedding Park, Hermozo) · tripleseat.com · eventtemple.com. Las páginas de Jano's y El Cronista se leyeron por los resultados de búsqueda.</p>""")

    p2 = pagina("""<div class="sec"><span class="n">3</span><h2>Los seis creativos</h2><span class="r">4 del ángulo ganador + 2 nuevos</span></div>""",
    f"""<table><tr><th>#</th><th>Ángulo</th><th>Creativo</th><th>Gancho en pantalla</th><th>Conjunto</th></tr>{filas}</table>
    <div class="sec" style="margin-top:12px"><span class="n">4</span><h2>Estructura con USD 20 por día</h2><span class="r">≈ USD 600 por mes</span></div>
    <div class="grid g3">
      <div class="card tinta"><span class="lbl">Campaña</span><span class="serif" style="font-size:12.5pt">Interacción · Mensajes a WhatsApp</span><br>Semanas 1 y 2: presupuesto por conjunto, para que los ángulos nuevos reciban inversión. Pocos anuncios activos: con USD 20 por día, más anuncios no aprenden.</div>
      <div class="card"><span class="lbl">Conjunto A · USD 13 por día</span><b>Ángulo ganador</b><br>Creativos 01, 02, 03 y 04 (versión A de cada uno) + el mejor anuncio del test 1 como control. Máximo 5 anuncios.</div>
      <div class="card"><span class="lbl">Conjunto B · USD 7 por día</span><b>Ángulos nuevos</b><br>Creativos 05 y 06 (versión A). Mismo público que A, para comparar en igualdad.</div>
    </div>
    <div class="grid g3" style="margin-top:6px">
      <div class="card"><span class="lbl">Público</span>Amplio, con Advantage+ y un radio de <span class="var">KM</span> km alrededor del salón. Edad según el evento: padres de 15 años y parejas. Sin intereses al principio.</div>
      <div class="card"><span class="lbl">Ubicaciones</span>Advantage+, con prioridad en Reels e Historias (9:16). En el feed, la versión 4:5 de 01 y 03.</div>
      <div class="card"><span class="lbl">Versiones B, C y D</span>No arrancan activas. Entran de a una para reemplazar al anuncio que pierde: así se renueva sin gastar presupuesto en aprendizaje.</div>
    </div>
    <h3>Reglas de decisión</h3>
    <table>
      <tr><th>Momento</th><th>Qué miramos</th><th>Qué hacemos</th></tr>
      <tr><td>Día 3</td><td>Tasa de gancho (reproducciones de 3 s ÷ impresiones) mayor a 25%</td><td>Si un anuncio queda abajo, se reemplaza por su versión B.</td></tr>
      <tr><td>Día 5 a 7 (≈ USD 10–15 por anuncio)</td><td>Costo por conversación contra el del test 1</td><td>Si es más de 1,5 veces el del test 1, se pausa. Si está por debajo, se deja correr.</td></tr>
      <tr><td>Día 14</td><td>Conversaciones calificadas (dieron fecha e invitados), visitas y señas</td><td>Una sola campaña con presupuesto de campaña (CBO) de USD 20 y los 3 o 4 mejores anuncios.</td></tr>
      <tr><td>Día 21 a 28</td><td>Frecuencia mayor a 3 o costo en subida</td><td>Renovación: ganchos C y D, nuevas frases de testimonios y una variante con IA.</td></tr>
    </table>
    <p class="mini" style="margin-top:4px">Si el cliente quiere crecer, se suma un 20% de presupuesto cada 3 días y nunca sobre un anuncio que empeora. Con USD 20 por día y el costo del test 1 se esperan entre 20 y 40 conversaciones por día.</p>
""")

    p3 = pagina("""    <div class="sec" style="margin-top:0"><span class="n">5</span><h2>WhatsApp: donde se gana la venta</h2><span class="r">Para el cliente</span></div>
    <div class="grid g2">
      <div class="card"><ul class="lim">
        <li>Etiquetas en WhatsApp Business: Nuevo · Calificado (dio fecha e invitados) · Visita agendada · Presupuesto enviado · Seña · Perdido.</li>
        <li>Con esas etiquetas medimos el costo por conversación calificada y el costo por seña, no solo por mensaje.</li></ul></div>
      <div class="card"><ul class="lim">
        <li>Responder en menos de 5 minutos, con respuestas rápidas por ángulo: /cuotas, /congelar, /incluye, /visita, /fecha.</li>
        <li>La primera pregunta siempre es «¿para qué fecha y cuántos invitados?».</li></ul></div>
    </div>
    <div class="nota roja" style="margin-top:6px">Meta pide que las promociones con fecha límite sean reales: la fecha del creativo 02 se confirma por escrito con el cliente antes de publicar. Las escenas hechas con IA llevan rótulo, como en Menutti.</div><div class="sec" style="margin-top:12px"><span class="n">6</span><h2>Calendario de trabajo</h2><span class="r">Del cuestionario al lanzamiento</span></div>
    <table>
      <tr><th>Semana</th><th>Qué pasa</th><th>Quién</th><th>Listo</th></tr>
      <tr><td>Semana 0</td><td>Cuestionario al cliente · Javi revisa el archivo de fiestas y testimonios (lo que ya tenemos)</td><td>Jona · Javi</td><td><span class="box"></span></td></tr>
      <tr><td>Semana 1</td><td>Números confirmados · jornada de grabación · tomas para IA</td><td>Cliente · Javi</td><td><span class="box"></span></td></tr>
      <tr><td>Semana 2</td><td>Edición de las versiones A (6 videos + cortes de 15 s) · revisión · textos de los anuncios cargados</td><td>Javi · Jona</td><td><span class="box"></span></td></tr>
      <tr><td>Semana 2</td><td>Lanzamiento: conjuntos A y B · respuestas rápidas en WhatsApp listas</td><td>Jona · cliente</td><td><span class="box"></span></td></tr>
      <tr><td>Semana 3</td><td>Primeras decisiones (día 3 y día 7) · edición de las versiones B</td><td>Jona · Javi</td><td><span class="box"></span></td></tr>
      <tr><td>Semana 4</td><td>Paso a CBO con los ganadores · informe al cliente</td><td>Jona</td><td><span class="box"></span></td></tr>
    </table>
    <div class="sep"></div>
    <div class="grid g2">
      <div class="card"><span class="lbl">Lo que entra con cada documento</span><ul class="lim">
        <li><b>01 Guiones</b>: gancho, variantes, guion segundo a segundo, texto del anuncio y datos a reemplazar.</li>
        <li><b>02 Plan de grabación</b>: qué se graba, qué sale del archivo, tomas para transformar con IA, jornada y equipo.</li>
        <li><b>03 Plan de edición</b>: reglas como en Menutti (subtítulos, rótulos, sonido, exportación), flujo de IA y mapa de cada video.</li></ul></div>
      <div class="card oro"><span class="lbl">Confirmado / a confirmar</span><ul class="lim">
        <li>✔ Financiación en <b>hasta 24 cuotas fijas</b>, paquete all inclusive.</li>
        <li>✔ Archivo de fiestas reales y testimonios de quinceañeras y madres.</li>
        <li>✔ Presupuesto: hasta USD 20 por día.</li>
        <li>? Precio «desde», mínimo de invitados, anticipo, si se congela el precio y las 3 cosas para mostrar en la visita.</li>
        <li>? Inversión real del test 1.</li></ul></div>
    </div>""")
    return documento("Trebelno · 00 Estrategia y campaña", p1 + p2 + p3)

# ======================================================================
# 01 · GUIONES
# ======================================================================
def ficha_creativo(c):
    cls = "nuevo" if c["tipo"]=="nuevo" else "eco"
    ficha = "".join(f'<div><span class="lbl">{k}</span>{v(x)}</div>' for k,x in c["ficha"])
    vars_ = "".join(f'<li class="{"rec" if r else ""}"><b class="l">{l}{" ★" if r else ""}</b><span>{v(d)}</span><span class="scr">{v(s)}</span></li>' for l,d,s,r in c["variantes"])
    beats = '<div class="beat h"><div class="tc">Tiempo</div><div class="pl">Plano · fuente</div><div>Qué se dice</div><div>Texto en pantalla</div></div>'
    beats += "".join(f'<div class="beat avoid"><div class="tc">{t}</div><div class="pl">{chips(f)}<br>{v(p)}</div><div class="dice">{v(d)}</div><div class="lee">{v(l)}</div></div>' for t,p,f,d,l in c["beats"])
    ad = c["ad"]
    h1 = f"""<section class="page {cls}-sec">
  <div class="cab {cls}">
    <div class="num"><small>Creativo</small><b>{c['n']}</b><small>{'Ganador' if cls=='eco' else 'Nuevo'}</small></div>
    <div class="tit"><span class="chip {cls}">{'Ángulo ganador' if cls=='eco' else 'Ángulo nuevo'}</span><span class="chip neutro">{c['angulo']}</span>
      <h2>{v(c['titulo'])}</h2><div class="idea">{v(c['idea'])}</div></div>
    <div class="estado"><span><i class="box"></i>Guion OK</span><span><i class="box"></i>Grabado</span><span><i class="box"></i>Editado A</span><span><i class="box"></i>Editado B</span><span><i class="box"></i>En Meta</span></div>
  </div>
  <div class="ficha">{ficha}</div>
  <div class="gancho-tit"><h3>El gancho · 0 a 3 s</h3><span class="mini">Lo que decide si el anuncio se mira o se pasa</span></div>
  <div class="gancho avoid">
    <div><span class="lbl">Se dice</span><div class="t">{v(c['gancho'][0])}</div></div>
    <div><span class="lbl">Se lee en pantalla</span><div class="pantalla">{v(c['gancho'][1])}</div></div>
    <div><span class="lbl">Se ve</span>{v(c['gancho'][2])}</div>
  </div>
  <span class="lbl">Cuatro ganchos · se graban todos, se editan A y B</span>
  <ul class="variantes">{vars_}</ul>
  <p class="mini">★ {v(c['rec'])}</p>
  <h3>Guion</h3>
  <div class="riel">{beats}</div>
</section>"""
    h2 = f"""<section class="page {cls}-sec">
  <div class="sec"><span class="n">{c['n']}</span><h2 style="font-size:15pt">{v(c['titulo'])}</h2><span class="r">El anuncio en Meta</span></div>
  <div class="ad avoid">
    <div class="row"><div>Texto principal</div><div>{v(ad['principal'])}</div></div>
    <div class="row"><div>Título</div><div><b>{v(ad['titulo'])}</b></div></div>
    <div class="row"><div>Descripción</div><div>{v(ad['desc'])}</div></div>
    <div class="row"><div>Botón</div><div>Enviar mensaje de WhatsApp</div></div>
    <div class="row"><div>Mensaje precargado</div><div>{v(ad['wsp'])}</div></div>
  </div>
  <p class="mini" style="margin-top:3px">El mismo texto va en las versiones A y B. La primera línea funciona como gancho: es lo único que se lee antes de «ver más».</p>
  <div class="sep"></div>
  <div class="grid g2 avoid">
    <div class="nota"><b>Por qué funciona.</b> {v(c['porque'])}</div>
    <div class="nota roja"><b>Notas y plan B.</b> {v(c['notas'])}</div>
  </div>
  <h3>Cómo lo medimos</h3>
  <table class="avoid"><tr><th>Indicador</th><th>Objetivo</th><th>Versión A</th><th>Versión B</th></tr>
    <tr><td>Tasa de gancho (3 s ÷ impresiones)</td><td>&gt; 25%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Retención al 50% del video</td><td>&gt; 15%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Costo por conversación</td><td>≤ test 1</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Conversaciones calificadas (fecha + invitados)</td><td>&gt; 40%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Visitas agendadas / señas</td><td>—</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
  </table>
</section>"""
    return h1 + h2

def doc01():
    intro = pagina(cabecera("01","Guiones de los seis creativos",
        "Cada creativo ocupa dos hojas: en la primera, el gancho, sus variantes y el guion segundo a segundo; en la segunda, el texto del anuncio y cómo lo medimos. Los datos en amarillo se reemplazan por los números reales del salón el día de la grabación.","quien pone la cara · Javi · Jona"),
    """<div class="sec"><span class="n">★</span><h2>Lo que se repite en los seis</h2><span class="r">Leer antes de grabar</span></div>
    <div class="grid g3">
      <div class="card oro"><span class="lbl">La oferta</span><span class="serif" style="font-size:13pt">All inclusive · hasta 24 cuotas fijas</span><br>Desde <span class="var">INVITADOS</span> invitados, desde <span class="var">TOTAL</span>. Reservás la fecha con <span class="var">ANTICIPO</span>.</div>
      <div class="card"><span class="lbl">El cierre</span>Siempre a WhatsApp, con una palabra clave por creativo: FECHA, CONGELAR, DETALLE, VISITA, ESCRIBIME. Se graban 2 cierres: uno para 15 años y otro para casamientos.</div>
      <div class="card"><span class="lbl">Cómo se habla</span>Una persona del salón le habla a una sola persona. Frases cortas, con voseo, sin leer. Si se traba, se repite la frase entera.</div>
    </div>
    <div class="nota" style="margin-top:8px">En cada guion, la fuente del plano: <span class="src G">GRABAR</span> se graba en la jornada · <span class="src A">ARCHIVO</span> sale del material de fiestas reales y testimonios · <span class="src IA">IA</span> se transforma con IA (ver 03 Plan de edición).</div>
    <h3>Índice</h3>
    <table><tr><th>#</th><th>Creativo</th><th>Ángulo</th><th>Palabras clave del subtítulo</th></tr>""" +
    "".join(f"<tr><td class='n'>{c['n']}</td><td><b>{v(c['titulo'])}</b></td><td>{c['angulo']}</td><td>{c['claves']}</td></tr>" for c in CREATIVOS) + "</table>")
    filas = "".join(f'<tr><td><span class="var" style="white-space:normal">{k}</span></td><td>{d}</td><td>{w}</td><td><div class="escribir" style="min-width:0;height:20px"></div></td><td><span class="box"></span></td></tr>' for k,d,w in VARIABLES)
    datos = pagina("""<div class="sec"><span class="n">D</span><h2>Datos a reemplazar</h2><span class="r">Completar antes de grabar</span></div>
    <p class="lead">Cada casilla amarilla es un dato del salón. Se completa acá una sola vez y se usa el mismo valor en los guiones, los textos del anuncio y las respuestas de WhatsApp.</p>
    <div class="nota">Confirmado: <b>all inclusive en hasta 24 cuotas fijas</b>. Referencia del test 1: $13.000.000 en 12 cuotas = $1.083.333 por mes; en 24 cuotas fijas serían $541.667 por mes.</div>""",
    f"""<table style="table-layout:fixed"><colgroup><col style="width:46mm"><col><col style="width:20mm"><col style="width:46mm"><col style="width:9mm"></colgroup>
    <tr><th>Dato</th><th>Qué es</th><th>Dónde</th><th>Valor real</th><th>OK</th></tr>{filas}</table>
    <div class="sep"></div>
    <div class="card" style="width:50%"><span class="lbl">Datos aprobados por el cliente</span><div style="height:16mm"></div><div class="escribir"></div><span class="mini">Nombre y fecha</span></div>""")
    return documento("Trebelno · 01 Guiones", intro + "".join(ficha_creativo(c) for c in CREATIVOS) + datos)

# ======================================================================
# 02 · PLAN DE GRABACIÓN
# ======================================================================
ARCHIVO = [
 ("Entrada de la quinceañera / de los novios","01 04"),("Vals y ceremonia de velas","04 06"),("Pista llena, carioca, humo y luces","01 02 03"),
 ("Sector salón: mesas armadas (general y detalles)","01 02 03"),("Sector cocina: platos que salen y se sirven","03"),("Sector barra en acción","02 03"),
 ("Sector DJ, luces y pantallas","03"),("Sector ambientación: centros de mesa y mesa dulce","01 03"),("Sector coordinación en acción","03"),
 ("Testimonios de quinceañeras","04 06"),("Testimonios de madres (y la frase sobre el pago)","04 06"),("Madres emocionadas durante la fiesta","06"),
]
TOMAS = {
 "01":[("G","Gancho A, B y C, 3 tomas de cada uno, en la pista con luces"),("G","Primer plano de la calculadora con el número real (celular en modo no molestar)"),("G","Cierre a cámara: versión 15 años y versión casamiento")],
 "02":[("G","Frapera con hielo y etiqueta (5 tomas: el hielo nunca cae igual)"),("G","Plano medio en la barra: fecha límite y cierre"),("G","Detalle de la etiqueta escrita a mano"),("IA","Foto fija de la frapera, para el hielo en cámara lenta (gancho C)")],
 "03":[("A","Del archivo: 1 clip de 3–5 s por sector (salón, cocina, barra, DJ, ambientación, coordinación y pista)"),("G","Solo si falta algún sector en el archivo: grabarlo en la jornada"),("G","Cierre en la pista, 2 versiones"),("G","Fotos fijas de cada sector, para el carrusel")],
 "04":[("G","Oferta y cierre del anfitrión/a en la pista (17–30 s), 2 versiones"),("A","Todo lo demás sale del archivo: no se graban testimonios nuevos")],
 "05":[("G","Walk & talk completo con gimbal, del gancho al cierre (3 tomas)"),("G","Detalle de cada una de las 3 cosas (2 o 3 planos por cosa)"),("G","Gancho con los 3 dedos, 3 tomas"),("G","Cierre en la pista a cámara, 2 versiones")],
 "06":[("G","3 tomas largas seguidas del guion completo, sin cortar (se elige la más natural)"),("G","Gancho A, B, C y D sueltos"),("G","Planos de escucha: mira la mesa, piensa, sonríe (para tapar cortes)"),("G","Cierre inclinándose hacia cámara")],
}
IA_TOMAS = [
 ("Salón vacío · 3 encuadres fijos","Durante el armado: general, pista y una mesa. Trípode marcado con cinta en el piso.","Repetir los mismos 3 encuadres con el salón armado → transición vacío → armado y ambientaciones creadas con IA (15, casamiento, temática) para la renovación.","03"),
 ("Anfitrión/a para avatar y voz","2 min a cámara en plano medio, mirando a lente, luz pareja y fondo quieto + 3 min de lectura en voz alta (el texto de esta misma hoja).","Avatar y voz clonada (ElevenLabs) para hacer ganchos C y D y versiones nuevas sin volver a grabar. Requiere autorización escrita.","Todos"),
 ("Mano con celular · pantalla verde","Celular con imagen verde a pantalla completa; la mano toca y desliza. 3 tomas de 8 s.","Reemplazo de pantalla por una conversación de WhatsApp de ejemplo: «mandás tu fecha y te respondemos».","01 06"),
 ("Frapera · foto fija","Foto en alta calidad, de cerca, con luz de la barra.","Hielo cayendo en cámara lenta (imagen a video).","02"),
 ("Mesa · cenital fija","Una mesa armada vista de arriba, 10 s.","Variantes de centros de mesa y mantelería para el carrusel.","03"),
]

def doc02():
    arch = "".join(f'<tr><td><span class="box"></span></td><td>{m}</td><td>{c}</td><td><div class="escribir" style="min-width:0"></div></td></tr>' for m,c in ARCHIVO)
    p1 = pagina(cabecera("02","Plan de grabación",
        "Qué se graba, qué sale del archivo de fiestas reales y qué tomas se dejan listas para transformar con IA. Una jornada de unas 6 horas con el salón armado.","Javi · filmmaker"),
    f"""<div class="sec"><span class="n">1</span><h2>Antes de la jornada: revisar el archivo</h2><span class="r">Semana 0</span></div>
    <p class="lead">Ya tenemos fiestas reales en distintos momentos y testimonios de quinceañeras y madres. Primero se revisa y se clasifica; en la jornada se graba solo lo que falta.</p>
    <table><tr><th>Tengo</th><th>Momento</th><th>Creativos</th><th>Archivo · minuto · calidad</th></tr>{arch}</table>
    <div class="grid g2" style="margin-top:8px">
      <div class="card"><span class="lbl">Testimonios: qué marcar</span><ul class="check one">
        <li>Transcribir todos en Premiere (Transcribir secuencia, español)</li>
        <li>Marcar las 5 frases más fuertes de madres y las 3 de quinceañeras</li>
        <li>Encontrar la frase que habla del pago o de las cuotas: abre el creativo 04</li><li>Elegir 1 clip de 3–5 s por sector para el creativo 03</li>
        <li>Pasarle las frases a Jona para cerrar el guion del 04</li></ul></div>
      <div class="card"><span class="lbl">Permisos</span><ul class="check one">
        <li>Confirmar que esas familias autorizaron el uso en publicidad paga</li>
        <li>Sin caras de menores que no sean la quinceañera, salvo que estén autorizadas</li>
        <li>Autorización escrita del anfitrión/a para avatar y voz con IA</li></ul></div>
    </div>""")
    bloques = [
     ("0","Durante el armado","Tomas fijas del salón vacío para IA (3 encuadres marcados con cinta)","03"),
     ("1","Salón armado","Los mismos 3 encuadres + sectores que falten en el archivo","03"),
     ("2","Recorrido","Walk & talk de las 3 cosas + detalles de cada una","05"),
     ("3","Pista con luces","Anfitrión/a: ganchos y cierres de 01, 03, 04 y 05 (versiones 15 años y casamiento)","01 03 04 05"),
     ("4","Barra","Frapera con hielo, plano medio, detalle de la etiqueta, foto fija","02"),
     ("5","Mesa con luz baja","Charla sentada: 3 tomas largas, ganchos sueltos y planos de escucha","06"),
     ("6","Rincón con buena luz","Anfitrión/a para avatar (2 min) y voz (3 min de lectura)","Todos"),
     ("7","Cierre","Celular con pantalla verde · cenital de mesa · fotos fijas para el carrusel","01 03"),
    ]
    filas = "".join(f'<tr><td class="n">{b}</td><td><b>{d}</b></td><td>{q}</td><td>{c}</td><td><span class="box"></span></td></tr>' for b,d,q,c in bloques)
    tomas = "".join(f'<div class="card avoid"><span class="lbl">Creativo {n}</span><ul class="check one">' + "".join(f'<li>{chips(f)} {v(t)}</li>' for f,t in TOMAS[n]) + "</ul></div>" for n in TOMAS)
    p2 = pagina(f"""<div class="sec"><span class="n">2</span><h2>La jornada, en bloques</h2><span class="r">Ordenada por luz y armado, no por número de creativo</span></div>
    <table><tr><th>#</th><th>Dónde</th><th>Qué se graba</th><th>Creativos</th><th>Listo</th></tr>{filas}</table>
    <div class="sec" style="margin-top:12px"><span class="n">3</span><h2>Lista de tomas por creativo</h2><span class="r">Tildar en el set</span></div>
    <div class="grid g3">{tomas}</div>""")
    ia = "".join(f'<tr><td><b>{t}</b></td><td>{c}</td><td>{p}</td><td>{n}</td><td><span class="box"></span></td></tr>' for t,c,p,n in IA_TOMAS)
    p3 = pagina(f"""<div class="sec"><span class="n">4</span><h2>Tomas para transformar con IA</h2><span class="r">Se graban pensando en la IA</span></div>
    <p class="lead">Estas tomas no se usan tal cual: son la materia prima para generar variantes sin volver al salón. Con USD 20 por día no podemos grabar seguido; la IA nos da los ganchos nuevos para la renovación de la semana 3–4.</p>
    <table><tr><th>Toma</th><th>Cómo se graba</th><th>Para qué</th><th>Creativo</th><th>OK</th></tr>{ia}</table>
    <div class="grid g2" style="margin-top:8px">
      <div class="card salvia"><span class="lbl">Reglas para que la IA funcione</span><ul class="lim">
        <li>Trípode, 10 s quieto, sin nadie que cruce el cuadro.</li>
        <li>Exposición, foco y balance de blancos bloqueados (AE/AF lock).</li>
        <li>4K. La toma fija también en horizontal: de ahí se recorta o se expande.</li>
        <li>Una foto del mismo encuadre: la mayoría de las herramientas parten de una imagen.</li>
        <li>Sin marcas ajenas a la vista (botellas, logos de proveedores).</li></ul></div>
      <div class="card"><span class="lbl">Texto para la grabación de voz (bloque 6)</span>
        <p style="font-size:8.3pt">«Hola, soy <span class="var">NOMBRE</span>, de Trebelno Recepciones. Sé que la cosa está difícil. Tu fiesta 2027 la podés pagar en hasta 24 cuotas fijas. Reservás tu fecha con <span class="var">ANTICIPO</span> y el resto lo vas pagando mes a mes. ¿Cuánto sale tu fiesta por mes? Escribinos tu fecha por WhatsApp. Vení a conocer el salón antes de decidir.»</p>
        <p class="mini">Leerlo 3 veces: tranquilo, con energía y como en una charla. Rincón sin eco, micrófono corbatero, 30 s de silencio del ambiente al final.</p></div>
    </div>
    <div class="sec" style="margin-top:12px"><span class="n">5</span><h2>Técnica, equipo y checklist</h2><span class="r">Lo mismo que en Menutti</span></div>
    <div class="grid g3">
      <div class="card"><span class="lbl">Técnica</span><ul class="lim"><li>Vertical 9:16 nativo, 4K a 30 cuadros por segundo.</li><li>Corbatero en todas las tomas habladas + 30 s de ambiente por locación.</li><li>Dejar 2 s antes y después de cada frase.</li></ul></div>
      <div class="card"><span class="lbl">Equipo</span><ul class="check one"><li>Celular/cámara 4K + respaldo</li><li>Gimbal</li><li>Trípode y cinta para marcar</li><li>2 corbateros</li><li>LED con difusor</li><li>Luz cálida para la mesa del 06</li><li>Frapera, hielo y etiqueta</li><li>Celular con pantalla verde</li></ul></div>
      <div class="card"><span class="lbl">Antes de arrancar</span><ul class="check one"><li>Números confirmados (01 Guiones · Datos)</li><li>Salón armado y técnico de luces</li><li>Las 3 cosas de la visita (05) confirmadas</li><li>Vestuario liso, sin logos, que contraste con el salón</li><li>Autorizaciones impresas</li><li>Lista de sectores que faltan en el archivo</li></ul></div>
    </div>""")
    return documento("Trebelno · 02 Plan de grabación", p1 + p2 + p3)

# ======================================================================
# 03 · PLAN DE EDICIÓN
# ======================================================================
IA_FLUJO = [
 ("Animar fotos de fiestas","Fotos del fotógrafo","Firefly (Kling 3.0 / Veo 3.1): imagen a video, movimiento suave de 5 s","Imagen animada con IA"),
 ("Salón vacío → ambientado","Toma fija del salón vacío (bloque 0)","Firefly relleno generativo / Gemini Image: 3 estilos, y después imagen a video","Escena generada con IA"),
 ("Horizontal → vertical","Archivo 16:9","Expandir generativo de Firefly o reencuadre automático de Premiere","—"),
 ("Mejorar resolución","Archivo de baja calidad","Escalado con IA (Firefly / el que use Javi)","—"),
 ("Avatar y voz del anfitrión/a","Bloque 6 (2 min a cámara + 3 min de voz)","ElevenLabs para la voz + sincronización de labios para ganchos nuevos","Presentador generado con IA"),
 ("Pantalla del celular","Toma con pantalla verde (bloque 7)","Ultra Key + seguimiento, o el clip ya reemplazado como en Menutti","Conversación de ejemplo"),
 ("Hielo en cámara lenta","Foto de la frapera","Imagen a video","Imagen animada con IA"),
]

def doc03():
    p1 = pagina(cabecera("03","Plan de edición",
        "Las reglas son las mismas que en la pauta de Menutti con el avatar de Diego: subtítulos, rótulos, zona segura, sonido y exportación. Después vienen el flujo de IA y el mapa de cada video.","Javi · editor"),
    """<div class="sec"><span class="n">1</span><h2>Lo que vale para los seis videos</h2><span class="r">Igual que Menutti</span></div>
    <div style="display:flex; gap:12px; align-items:flex-start">
      <div class="phone"><div class="luz"></div><div class="persona"></div><div class="zs"></div>
        <span class="etq" style="top:12%">y 270</span><span class="etq" style="top:65.5%">y 1250</span>
        <div class="pill">Presentador generado con IA</div>
        <div class="oferta">HASTA 24 CUOTAS FIJAS<br><span style="font-weight:500;font-size:5.6pt">Reservá tu fecha 2027</span></div>
        <div class="sub">Tu fiesta 2027 en hasta<br><em>24 CUOTAS FIJAS</em></div>
        <div class="botones"><i></i><i></i><i></i></div><div class="cap"></div></div>
      <div style="flex:1">
        <h3 style="margin-top:0">Subtítulos (como en Menutti, no los de motion graphics)</h3>
        <ul class="lim">
          <li>En Premiere: panel Texto → <b>Transcribir secuencia</b> (español) → <b>Crear subtítulos</b>. Corregir «Trebelno», «WhatsApp» y los montos.</li>
          <li>Una o dos líneas, <b>Montserrat Bold</b>, blancos con sombra.</li>
          <li>Las <b>palabras clave en el rojo de Trebelno</b> (<span class="var">ROJO MARCA</span>; si sobre la imagen oscura no se lee, usar la versión más clara del rojo).</li>
          <li>Abajo, sin pasar de y = 1250. Sin animaciones por palabra, sin emojis y sin cajas de color.</li>
        </ul>
        <h3>Zona segura</h3>
        <p>Textos, subtítulos y logo entre <b>y = 270</b> (el 14% de arriba) e <b>y = 1250</b> (el 35% de abajo), y a más de 65 px de cada costado. Confirmar con la vista previa de Ads Manager.</p>
        <h3>Rótulos (los armás vos)</h3>
        <ul class="lim">
          <li>Avisos: píldora negra al 60% con texto blanco, Montserrat Medium 24 px, arriba a la izquierda (desde x 72, y 352).</li>
          <li><b>Tarjeta de oferta</b> (la que en Menutti era la de 72 hs): fondo rojo de marca, texto blanco: «HASTA 24 CUOTAS FIJAS · Reservá tu fecha 2027». Va desde el CTA hasta el final, arriba de la cabeza (y 470 a 625).</li>
          <li>Placa final de 1 a 1,5 s: <span class="var">FONDO PLACA</span>, logo en PNG y «Agenda 2027 · Escribinos por WhatsApp».</li>
        </ul>
      </div>
    </div>
    <div class="grid g3" style="margin-top:8px">
      <div class="card"><span class="lbl">Cómo se arma</span><ul class="lim"><li>Secuencia de 1080 × 1920 a 30 cuadros por segundo.</li><li>Carpetas: Voz, Anfitrión, Archivo, IA, Gráficos y Música.</li><li><b>Voz primero</b>: las frases habladas en A1; los cortes caen en las pausas.</li><li>Tomas de archivo: acercamiento suave del 100 al 108%.</li></ul></div>
      <div class="card"><span class="lbl">Sonido y color</span><ul class="lim"><li>Voz adelante, música entre 20 y 25 dB por debajo, con atenuación automática.</li><li>El sonido real de las fiestas puede quedar debajo de la voz: le da vida.</li><li>Música con licencia para publicidad paga.</li><li>Una sola corrección de color por video; igualar la temperatura de las distintas fiestas.</li></ul></div>
      <div class="card"><span class="lbl">Reglas fijas</span><ul class="lim"><li>Rótulo de IA siempre que haya una escena o persona generada.</li><li>Ninguna marca ajena en pantalla.</li><li>Ningún número que el cliente no haya confirmado.</li><li>Frases de testimonios textuales, sin cambiar palabras.</li><li>El mismo cierre en todos: WhatsApp + tarjeta de 24 cuotas.</li></ul></div>
    </div>""")
    flujo = "".join(f'<tr><td><b>{t}</b></td><td>{e}</td><td>{h}</td><td>{r}</td></tr>' for t,e,h,r in IA_FLUJO)
    mapas = []
    for c in CREATIVOS:
        filas = "".join(f'<tr><td class="n" style="width:42px;color:var(--tinta)">{t}</td><td>{chips(f)} {v(p)}</td><td>{v(l)}</td></tr>' for t,p,f,d,l in c["beats"])
        mapas.append(f"""<div class="card avoid" style="padding:6px 8px">
          <div style="display:flex;justify-content:space-between;align-items:baseline"><b class="serif" style="font-size:10.5pt">{c['n']} · {v(c['titulo'])}</b><span class="mini">Clave en rojo: <b>{c['claves']}</b></span></div>
          <table style="font-size:7.8pt;margin-top:3px"><tr><th>Tiempo</th><th>Imagen y fuente</th><th>Texto en pantalla</th></tr>{filas}</table>
          <p class="mini" style="margin:3px 0 0"><b>Corte de 15 s:</b> {c['corte15']} · <b>Archivo:</b> Trebelno_C{c['n']}A_{c['corto']}_30s.mp4</p></div>""")
    p2 = pagina(f"""<div class="sec"><span class="n">2</span><h2>Flujo de IA</h2><span class="r">Con las tomas del bloque 0, 6 y 7</span></div>
    <table><tr><th>Tarea</th><th>Entrada</th><th>Herramienta y proceso</th><th>Rótulo en pantalla</th></tr>{flujo}</table>
    <p class="mini" style="margin-top:4px">Las herramientas son las del flujo de Menutti; si Javi tiene otra que dé mejor resultado, se usa esa. Cada clip generado se revisa cuadro por cuadro (caras, manos, textos que se deforman) antes de editarlo.</p>
    <div class="sec" style="margin-top:12px"><span class="n">3</span><h2>Mapa de cada video</h2><span class="r">01 y 02</span></div>
    <div class="grid" style="gap:6px">{''.join(mapas[:2])}</div>""")
    p3 = pagina(f"""<div class="sec"><span class="n">3</span><h2>Mapa de cada video</h2><span class="r">03 a 05</span></div>
    <div class="grid" style="gap:6px">{''.join(mapas[2:5])}</div>""")
    p4 = pagina(f"""<div class="sec"><span class="n">3</span><h2>Mapa de cada video</h2><span class="r">06</span></div>{mapas[5]}
    <div class="sec" style="margin-top:12px"><span class="n">4</span><h2>Exportación y entrega</h2><span class="r">Para pautar</span></div>
    <div class="grid g2">
      <div class="card"><span class="lbl">Exportación</span><ul class="lim">
        <li>H.264, 1080 × 1920, 30 cuadros por segundo, audio AAC.</li>
        <li>Nombres: Trebelno_C01A_cuotas_30s.mp4 y Trebelno_C01A_cuotas_15s.mp4; la versión B, C01B. Sin música: _sin_musica.</li>
        <li>4:5 (1080 × 1350) solo para 01 y 03.</li>
        <li>Guardar el proyecto completo para hacer las variantes del que funcione mejor.</li></ul></div>
      <div class="card"><span class="lbl">Orden de entrega</span><ul class="check one">
        <li>Semana 2: las 6 versiones A + sus cortes de 15 s</li>
        <li>Semana 3: las versiones B de los que sigan activos</li>
        <li>Semana 3–4: ganchos C/D y variantes con IA para la renovación</li></ul></div>
    </div>
    <div class="sec" style="margin-top:12px"><span class="n">5</span><h2>Antes de entregar</h2><span class="r">Revisar en cada video</span></div>
    <ul class="check one" style="font-size:9pt">
      <li>9:16 y 1080 × 1920</li>
      <li>El gancho se entiende en los primeros 1 a 3 s, sin sonido</li>
      <li>Queda claro que habla un salón de fiestas y que la fiesta all inclusive se paga en hasta 24 cuotas fijas</li>
      <li>Ningún número sin confirmar (los amarillos del guion ya reemplazados)</li>
      <li>Subtítulos al estilo Menutti, legibles y dentro de la zona segura; palabras clave en rojo</li>
      <li>La voz se escucha clara en el parlante del celular</li>
      <li>Rótulos de IA donde corresponde y ninguna marca ajena</li>
      <li>Tarjeta de 24 cuotas en el cierre y placa final con el logo</li>
      <li>El corte de 15 s dura 15 s o menos</li>
      <li>Exportado con y sin música, con los nombres de esta guía</li>
    </ul>
    <div class="nota" style="margin-top:8px">Cuando tengas cada exportación, mandásela a Jona: se revisa cuadro por cuadro (caras, labios, manos, números y tiempos) antes de subirla a Meta.</div>""")
    return documento("Trebelno · 03 Plan de edición", p1 + p2 + p3 + p4)

for nombre, fn in [("00_estrategia", doc00), ("01_guiones", doc01), ("02_grabacion", doc02), ("03_edicion", doc03)]:
    (AQUI / f"{nombre}.html").write_text(fn(), encoding="utf-8")
    print("ok", nombre)
