# Cuestionario comercial para Trebelno Recepciones · paleta rojo/bordó del salón.
# Solo lo necesario para cerrar la oferta, los guiones y la grabación.
import pathlib
AQUI = pathlib.Path(__file__).parent
CSS = (AQUI / "estilo.css").read_text(encoding="utf-8")

PALETA = """
:root{ --bordo:#7a0f1c; --bordo-claro:#f8e6e8; --oro:#c4161c; --oro-claro:#fcecec; --papel-2:#f7eeef; --linea:#ead6d8; --tinta-3:#8c6f72; }
.q .qt .star{ color:#c4161c; }
.q .lineas i{ border-bottom-color:#d9b9bc; }
.cab.eco .num{ background:linear-gradient(160deg,#c4161c 0%,#7a0f1c 100%); }
.sec{ border-bottom-color:#7a0f1c; }
.sec h2{ color:#7a0f1c; }
.card.oro{ border-color:#f0c9cc; }
.box{ border-color:#7a0f1c; }
"""

# (pregunta, ayuda, líneas, opciones)
BLOQUES = [
 ("A","La oferta","Con esto armamos los números de los anuncios.",[
  ("¿Cuál es el paquete más vendido? Nombre, cantidad de invitados y qué incluye.","",1,["Salón","Catering","Barra","Mesa dulce","DJ, sonido y luces","Ambientación","Coordinación","Foto / video","Otro"]),
  ("Precio total de ese paquete para una fiesta en 2027.","",1,None),
  ("¿Cuánto hay que dejar para reservar la fecha? (monto o %)","",1,None),
  ("Las hasta 24 cuotas, ¿son fijas o se ajustan? Si se ajustan: ¿con qué índice y cada cuánto?","",1,["Fijas","Ajuste mensual","Ajuste trimestral"]),
  ("¿Se puede congelar el precio reservando antes de una fecha? ¿Hasta cuándo?","",1,["Sí","No"]),
  ("¿Qué se cobra aparte?","",1,None),
 ]),
 ("B","Agenda 2027","Para el anuncio de fechas: la escasez tiene que ser real.",[
  ("¿Qué sábados de 2027 ya están reservados? (alcanza con la lista por mes)","",2,None),
  ("¿Qué meses se piden más y cuántos sábados libres quedan en ellos?","",1,None),
 ]),
 ("C","Visitas y WhatsApp","Donde se cierra la venta.",[
  ("¿Qué días y horarios se puede visitar el salón? ¿Hacen jornadas abiertas o degustaciones?","",1,None),
  ("¿Quién responde el WhatsApp de la pauta y en qué horario?","",1,None),
  ("¿Cuáles son las 3 preguntas o dudas que más reciben?","",2,None),
 ]),
 ("D","Grabación y material","",[
  ("¿Qué día podemos grabar con el salón armado, con luces y humo (y el técnico presente)?","",1,None),
  ("¿Quién pone la cara? ¿Autoriza que hagamos su avatar y su voz con IA para nuevas versiones?","",1,["Sí","No","A charlar"]),
  ("Los videos de fiestas y los testimonios que tenemos, ¿están autorizados para publicidad paga?","",1,["Sí","No","Algunos"]),
  ("Logo en PNG y colores exactos de la marca (código o manual de marca).","",1,None),
 ]),
]

def bloque(letra, titulo, sub, preguntas, inicio):
    out = [f'<div class="sec avoid" style="margin-top:10px"><span class="n">{letra}</span><h2 style="font-size:14pt">{titulo}</h2><span class="r">{sub}</span></div>']
    n = inicio
    for q,h,lineas,opts in preguntas:
        n += 1
        hh = f'<div class="qh">{h}</div>' if h else ''
        oo = ('<div class="opts">' + "".join(f'<span><i class="box"></i>{o}</span>' for o in opts) + '</div>') if opts else ''
        ll = '<div class="lineas">' + "<i></i>"*lineas + '</div>'
        out.append(f'<div class="q"><div class="qn">{n:02d}</div><div><div class="qt">{q}</div>{hh}{oo}{ll}</div></div>')
    return "".join(out), n

cuerpo, n = [], 0
for b in BLOQUES:
    h, n = bloque(*b, n)
    cuerpo.append(h)

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Trebelno · Cuestionario comercial</title><style>{CSS}{PALETA}</style></head><body>
<section class="page">
  <div class="cab eco" style="grid-template-columns:30mm 1fr">
    <div class="num"><small>Cuestionario</small><b>Q</b><small>Agenda 2027</small></div>
    <div class="tit"><span class="chip eco">Trebelno Recepciones</span><span class="chip eco">Campaña Agenda 2027</span>
      <h2>Lo que necesitamos para armar la oferta y los guiones</h2>
      <div class="idea">Son {n} preguntas y llevan unos 10 minutos. Ya sabemos que se financia en <b>hasta 24 cuotas</b> y ya tenemos material de fiestas y testimonios: acá va solo lo que falta. Si un número todavía no está cerrado, alcanza con un rango; el dato final se pone el día de la grabación.</div></div>
  </div>
  {''.join(cuerpo)}
  <div class="sep"></div>
  <div class="grid g2 avoid">
    <div class="card"><span class="lbl">Respondió</span><div style="height:10mm"></div><div class="escribir"></div><span class="mini">Nombre y fecha</span></div>
    <div class="card oro"><span class="lbl">Cómo responder</span>A mano sobre esta hoja, por audio de WhatsApp o en una llamada de 10 minutos con nosotros.</div>
  </div>
</section>
</body></html>"""
(AQUI / "cuestionario.html").write_text(html, encoding="utf-8")
print("ok cuestionario.html", n, "preguntas")
