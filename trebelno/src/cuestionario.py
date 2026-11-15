# Cuestionario comercial para Trebelno Recepciones (mismo sistema visual "Claqueta").
import pathlib
AQUI = pathlib.Path(__file__).parent
CSS = (AQUI / "estilo.css").read_text(encoding="utf-8")

# (pregunta, ayuda, lineas, opciones, critica)
BLOQUES = [
 ("A","El salón y los eventos","Para presentar el lugar con datos concretos.",[
  ("¿Qué tipos de evento hacen y cuál es el que más venden?","Ordenar de más a menos: 15 años, casamientos, cumpleaños, egresados, empresas, otros.",2,None,True),
  ("¿Cuál es la capacidad del salón (mínimo y máximo de invitados)? ¿Tienen más de un salón o espacio?","",2,None,True),
  ("¿Qué tiene el salón que no tenga otro de la zona?","Parque, estacionamiento, pista con pantallas, ubicación, años de trayectoria, cocina propia…",3,None,True),
  ("¿Dirección exacta y desde qué zonas viene la mayoría de los clientes?","Sirve para definir el radio de la campaña.",2,None,False),
  ("¿Hace cuántos años está el salón y cuántos eventos hicieron?","Solo números que puedan sostener.",1,None,False),
 ]),
 ("B","Los paquetes: qué incluye cada uno","Con esto armamos el creativo 03 y el texto de los anuncios.",[
  ("¿Qué paquetes ofrecen? Nombre de cada uno y para cuántos invitados.","Ej.: Clásico / Premium / Full.",3,None,True),
  ("En el paquete más vendido, ¿qué está incluido?","Marcar lo que corresponda y aclarar el detalle.",0,["Salón","Catering (menú)","Barra (tragos / sin alcohol)","Mesa dulce","DJ y sonido","Luces y pantallas","Ambientación / centros de mesa","Coordinación","Fotografía / video","Cotillón","Otro"],True),
  ("¿Qué se cobra aparte y qué cuesta?","Ej.: barra libre premium, fotógrafo, hora extra, menores.",2,None,True),
  ("¿Tienen proveedores propios o el cliente puede traer los suyos?","",1,None,False),
 ]),
 ("C","Precios y financiación","Es el corazón del ángulo ganador. Si no hay número cerrado, un rango sirve para avanzar.",[
  ("Precio total del paquete más vendido para un evento de 2027 (y para cuántos invitados).","",1,None,True),
  ("¿Cuánto hay que dejar para reservar la fecha? (monto o %)","",1,None,True),
  ("¿En cuántas cuotas se puede pagar el resto? ¿Hasta cuándo antes del evento?","",1,None,True),
  ("¿Las cuotas son fijas o se ajustan? Si se ajustan: ¿con qué índice y cada cuánto?","",1,["Fijas","Ajuste mensual","Ajuste trimestral","Otro"],True),
  ("¿Se puede congelar el precio? ¿Con qué condición y hasta qué fecha?","Ej.: «reservando antes del 31/12 se mantiene el precio de 2026».",2,None,True),
  ("¿Medios de pago? ¿Hay descuento por pago contado o con transferencia?","",1,["Efectivo","Transferencia","Tarjeta (cuotas)","Dólares"],False),
  ("¿Cambia el precio según el día (viernes, sábado, domingo, día de semana) o según el mes?","",2,None,True),
  ("La venta del test 1 ($13.000.000 en 12 cuotas): ¿qué paquete era, qué tipo de evento y para qué fecha?","Nos sirve de ejemplo real para los números.",2,None,True),
 ]),
 ("D","Agenda 2027 y disponibilidad","Para el creativo 06: la escasez tiene que ser real.",[
  ("¿Cuántas fechas de 2027 ya están reservadas? ¿Cuáles? (aunque sea por mes)","Las vamos a tachar en el calendario del video.",2,None,True),
  ("¿Qué meses o sábados se piden más? ¿Cuántos sábados libres quedan en esos meses?","",2,None,True),
  ("¿Con cuánta anticipación reserva normalmente un cliente de 15 años? ¿Y uno de casamiento?","",1,None,False),
  ("¿Cuántos eventos pueden hacer por día o por fin de semana?","",1,None,False),
 ]),
 ("E","Promociones y beneficios","Bonos que empujan la decisión sin bajar el precio.",[
  ("¿Tienen alguna promoción para quien reserve 2027 antes de una fecha? ¿Cuál y hasta cuándo?","",2,None,True),
  ("¿Qué beneficio podrían regalar sin que les cueste mucho?","Ej.: hora extra, mesa dulce, cabina de fotos, prueba de menú, cotillón, upgrade de barra.",2,None,False),
  ("¿Hay cupo para esa promoción? (ej.: «las primeras 10 reservas»)","",1,None,False),
 ]),
 ("F","Garantías y condiciones","Lo que da tranquilidad a alguien que va a poner millones.",[
  ("¿Qué pasa si el cliente necesita cambiar la fecha o cancelar?","",2,None,True),
  ("¿Qué pasa si se atrasa con una cuota?","",1,None,False),
  ("¿Firman contrato? ¿Qué garantiza el salón por escrito?","",1,None,False),
 ]),
 ("G","Prueba social","Para el creativo 04 (testimonio).",[
  ("¿Qué cliente de los últimos meses pagó en cuotas y quedaría contento de contarlo en un video?","Nombre, evento, fecha y si autoriza imagen.",2,None,True),
  ("¿Tienen videos o fotos de eventos reales (del fotógrafo) que podamos usar con permiso?","",1,["Sí","No","Algunos"],True),
  ("¿Reseñas en Google? ¿Cuántas y con qué puntaje?","",1,None,False),
 ]),
 ("H","Visitas y proceso de venta","Donde se gana o se pierde el lead que trae la pauta.",[
  ("¿Se puede visitar el salón? ¿Qué días y horarios? ¿Hacen jornadas abiertas o degustaciones?","Para el creativo 05.",2,None,True),
  ("¿Quién responde el WhatsApp, en qué horarios y en cuánto tiempo?","",1,None,True),
  ("¿Cuáles son las 3 preguntas u objeciones que más reciben por WhatsApp?","",3,None,True),
  ("De cada 10 personas que visitan el salón, ¿cuántas reservan?","",1,None,False),
  ("¿Dónde registran hoy las consultas? (planilla, CRM, etiquetas de WhatsApp Business)","",1,None,False),
 ]),
 ("I","Competencia","",[
  ("¿Con qué salones los comparan los clientes? ¿Por qué los eligen a ustedes y por qué no?","",3,None,False),
 ]),
 ("J","Logística de la grabación","Una jornada con el salón armado.",[
  ("¿Qué día podemos grabar con el salón armado como para un evento (luces, humo, mesas)?","",1,None,True),
  ("¿Quién pone la cara? (dueño/a, coordinador/a, organizador/a) ¿Se siente cómodo/a a cámara?","",1,None,True),
  ("¿El técnico de luces y sonido puede estar durante el rodaje?","",1,["Sí","No"],False),
  ("¿Podemos grabar algunos minutos de un evento real (con permiso de los anfitriones)?","",1,["Sí","No","A consultar"],False),
 ]),
]

def bloque(letra, titulo, sub, preguntas, inicio):
    out = [f'<div class="sec avoid" style="margin-top:12px"><span class="n">{letra}</span><h2 style="font-size:15pt">{titulo}</h2><span class="r">{sub}</span></div>']
    n = inicio
    for q,h,lineas,opts,crit in preguntas:
        n += 1
        star = ' <span class="star">★</span>' if crit else ''
        hh = f'<div class="qh">{h}</div>' if h else ''
        oo = ('<div class="opts">' + "".join(f'<span><i class="box"></i>{o}</span>' for o in opts) + '</div>') if opts else ''
        ll = ('<div class="lineas">' + "<i></i>"*lineas + '</div>') if lineas else ''
        if opts and lineas == 0:
            ll = '<div class="lineas"><i></i><i></i></div>'
        out.append(f'<div class="q"><div class="qn">{n:02d}</div><div><div class="qt">{q}{star}</div>{hh}{oo}{ll}</div></div>')
    return "".join(out), n

cuerpo, n = [], 0
for b in BLOQUES:
    h, n = bloque(*b, n)
    cuerpo.append(h)

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Trebelno · Cuestionario comercial</title><style>{CSS}</style></head><body>
<section class="page">
  <div class="cab eco" style="grid-template-columns:30mm 1fr">
    <div class="num"><small>Cuestionario</small><b>Q</b><small>Oferta 2027</small></div>
    <div class="tit"><span class="chip eco">Trebelno Recepciones</span><span class="chip neutro">Campaña Agenda 2027</span>
      <h2>Lo que necesitamos saber para armar la oferta y los guiones</h2>
      <div class="idea">Son {n} preguntas en 10 bloques y llevan unos 20 minutos. Las marcadas con ★ son las que necesitamos antes de grabar. Si algún número no está cerrado, un rango sirve: el resto del trabajo avanza igual y el dato final se pone el día de la grabación.</div></div>
  </div>
  <div class="grid g3" style="margin-bottom:4px">
    <div class="card oro"><span class="lbl">Por qué preguntamos</span>El test 1 vendió con la oferta económica. Para renovar ese ángulo necesitamos los números reales: precio, anticipo, cuotas y condiciones.</div>
    <div class="card"><span class="lbl">Cómo responder</span>A mano sobre esta hoja, por audio de WhatsApp o en una llamada de 20 minutos con nosotros.</div>
    <div class="card"><span class="lbl">Material para mandar</span><ul class="check one"><li>Lista de precios 2027</li><li>Fotos y videos de eventos</li><li>Logo en alta calidad</li></ul></div>
  </div>
  {''.join(cuerpo)}
  <div class="sep"></div>
  <div class="grid g2 avoid">
    <div class="card"><span class="lbl">Respondió</span><div style="height:14mm"></div><div class="escribir"></div><span class="mini">Nombre, cargo y fecha</span></div>
    <div class="card"><span class="lbl">Algo más que quieras contarnos</span><div style="height:20mm"></div></div>
  </div>
</section>
</body></html>"""
(AQUI / "cuestionario.html").write_text(html, encoding="utf-8")
print("ok cuestionario.html", n, "preguntas")
