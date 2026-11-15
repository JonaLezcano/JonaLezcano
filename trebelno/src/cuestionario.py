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
  ("¿Cuál es el paquete all inclusive más vendido? ¿Desde cuántos invitados y qué incluye?","",1,["Salón","Catering","Barra","Mesa dulce","DJ, sonido y luces","Ambientación","Coordinación","Foto / video","Otro"]),
  ("¿Desde qué precio total sale ese paquete para una fiesta en 2027?","",1,None),
  ("¿Cuánto hay que dejar para reservar la fecha? (monto o %)","",1,None),
  ("¿Se puede congelar el precio reservando antes de una fecha? ¿Hasta cuándo?","",1,["Sí","No"]),
  ("¿Qué se cobra aparte?","",1,None),
 ]),
 ("B","Visitas y WhatsApp","Donde se cierra la venta.",[
  ("¿Qué días y horarios se puede visitar el salón? ¿Hacen jornadas abiertas o degustaciones?","",1,None),
  ("¿Qué 3 cosas del salón conviene mostrar en una visita? Marcá las más fuertes y contanos el dato de cada una.","",1,["Cocina propia","Grupo electrógeno","Estacionamiento","Climatización","Habilitación","Baños","Accesibilidad","Plan para lluvia","Otra"]),
  ("¿Quién responde el WhatsApp de la pauta y en qué horario?","",1,None),
  ("¿Cuáles son las 3 preguntas o dudas que más reciben?","",2,None),
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
      <div class="idea">Son {n} preguntas y llevan unos 5 minutos. Ya sabemos que la fiesta es all inclusive y se financia en <b>hasta 24 cuotas fijas</b>: acá va solo lo que falta. Si un número todavía no está cerrado, alcanza con un rango; el dato final se pone el día de la grabación.</div></div>
  </div>
  {''.join(cuerpo)}
</section>
</body></html>"""
(AQUI / "cuestionario.html").write_text(html, encoding="utf-8")
print("ok cuestionario.html", n, "preguntas")
