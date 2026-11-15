# Genera el kit de rodaje de la campaña Agenda 2027 de Trebelno Recepciones.
# Los datos que el cliente tiene que confirmar se escriben como [[VARIABLE]]
# y se imprimen resaltados en amarillo para reemplazarlos el día de la grabación.
import re, pathlib

AQUI = pathlib.Path(__file__).parent
CSS = (AQUI / "estilo.css").read_text(encoding="utf-8")

def v(t):
    t = re.sub(r"\[\[([A-Z0-9_ ]+)\]\]", r'<span class="var">\1</span>', t)
    t = t.replace("[VALIDAR]", '<span class="validar">[VALIDAR]</span>')
    return t

# --------------------------------------------------------------------------
CREATIVOS = [
 dict(
  n="01", tipo="eco", angulo="Oferta económica · cuota mensual",
  titulo="Hacé la cuenta: tu fiesta 2027 por mes",
  idea="Bajamos el precio total a una cuota. El que mira deja de pensar en «cuánto sale» y pasa a pensar en «cuánto por mes»: es la misma lógica que ya vendió en el test 1.",
  ficha=[("Objetivo","Mensaje por WhatsApp pidiendo presupuesto en cuotas"),("Duración","25–30 s"),("Quién","Anfitrión/a de Trebelno a cámara"),("Dónde","Pista del salón, luces encendidas"),
         ("Audio","Tecleo real de la calculadora + golpe de música en el número"),("CTA","Escribinos tu fecha"),("Destino","Clic a WhatsApp"),("Exportar","9:16 · 4:5 · 1:1 (estático)")],
  gancho=("«¿Cuánto sale por mes una fiesta en 2027? Hacé la cuenta conmigo.»","¿CUÁNTO SALE TU FIESTA 2027 POR MES?","Anfitrión/a en la pista vacía con luces de color; gira el celular hacia cámara con la calculadora: [[TOTAL]] ÷ [[CUOTAS]]"),
  variantes=[
   ("A","«¿Cuánto sale por mes una fiesta en 2027? Hacé la cuenta conmigo.»","¿Cuánto sale tu fiesta 2027 por mes?",True),
   ("B","«Tu fiesta 2027, completa, desde [[CUOTA]] por mes.»","Tu fiesta 2027 desde [[CUOTA]]/mes",False),
   ("C","Dolor: «¿Postergaste la fiesta porque pensaste que no llegabas con la plata?»","¿Pensaste que no llegabas?",False),
   ("D","Resultado primero: plano de la fiesta llena + «Esto, en [[CUOTAS]] cuotas.»","Esto, en [[CUOTAS]] cuotas",False)],
  rec="A: la pregunta obliga a hacer la cuenta propia y la calculadora retiene hasta el número.",
  beats=[
   ("0–3 s","Pista vacía, gira el celular","Gancho A","¿CUÁNTO SALE TU FIESTA 2027 POR MES?"),
   ("3–8 s","Plano medio, camina hacia las mesas","«Una fiesta completa para [[INVITADOS]] invitados: [[INCLUYE 1]], [[INCLUYE 2]] y [[INCLUYE 3]].»","PAQUETE COMPLETO · [[INVITADOS]] INVITADOS"),
   ("8–14 s","Primer plano de la calculadora","«Son [[TOTAL]]. Dividido en [[CUOTAS]] cuotas: [[CUOTA]] por mes.»","[[CUOTAS]] CUOTAS DE [[CUOTA]]"),
   ("14–21 s","B-roll: salón armado, pista con luces (VO)","«Reservás tu fecha con [[ANTICIPO]] y el resto lo vas pagando mes a mes, hasta el día de la fiesta.»","RESERVÁS CON [[ANTICIPO]]"),
   ("21–28 s","Primer plano del anfitrión/a","«Escribinos por WhatsApp tu fecha y la cantidad de invitados, y te pasamos el presupuesto exacto.»","ESCRIBINOS TU FECHA 2027 →")],
  tomas=["Gancho A, B y C (3 tomas cada uno)","Calculadora en primer plano con el número real","Caminata pista → mesas","Cierre a cámara (2 versiones: 15 años y casamiento)","Salón armado: plano general fijo 10 s","Luces de pista encendiéndose"],
  utileria=["Celular con calculadora en pantalla grande","Salón armado como para evento (mesas, centros)","Luces de pista y humo"],
  ad=dict(principal="¿Cuánto sale tu fiesta 2027 por mes? 🎉 En Trebelno Recepciones la armás completa —[[INCLUYE 1]], [[INCLUYE 2]] y [[INCLUYE 3]]— y la pagás en [[CUOTAS]] cuotas de [[CUOTA]]. Reservás la fecha con [[ANTICIPO]]. Escribinos tu fecha y cantidad de invitados y hoy mismo te mandamos el presupuesto exacto.",
          titulo="Tu fiesta 2027 en [[CUOTAS]] cuotas", desc="Reservá tu fecha con [[ANTICIPO]]", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! Quiero el presupuesto en cuotas para mi fiesta 2027. Mi fecha es: ___"),
  porque="Es el ángulo que ya trajo 325 mensajes y la venta de $13.000.000 en 12 cuotas. Lo renovamos con persona a cámara (casi nadie en el rubro lo hace) y con un número que el que mira puede verificar en pantalla.",
  notas="El número de cuota tiene que ser el real del paquete de referencia. Si el salón ajusta las cuotas, decirlo en pantalla («cuotas con ajuste [[AJUSTE]]»): un número que después cambia genera mensajes que no cierran.",
 ),
 dict(
  n="02", tipo="eco", angulo="Oferta económica · congelar el precio",
  titulo="Congelá hoy el precio de tu fiesta 2027",
  idea="Contra la inflación, la decisión de hoy ahorra plata. La urgencia es real y tiene fecha: el precio de hoy vale hasta [[FECHA LIMITE]].",
  ficha=[("Objetivo","Que pidan reservar la fecha con el precio de hoy"),("Duración","22–28 s"),("Quién","Anfitrión/a a cámara"),("Dónde","Barra del salón"),
         ("Audio","Hielo real cayendo en la frapera; voz seca los primeros 2 s"),("CTA","Escribí CONGELAR"),("Destino","Clic a WhatsApp"),("Exportar","9:16 · 4:5")],
  gancho=("«Tu fiesta de 2027 no va a costar lo mismo que hoy. Salvo que la congeles.»","CONGELÁ EL PRECIO DE TU FIESTA 2027","Primer plano: el anfitrión/a hunde una etiqueta de precio en la frapera con hielo de la barra y levanta la vista a cámara"),
  variantes=[
   ("A","«Tu fiesta de 2027 no va a costar lo mismo que hoy. Salvo que la congeles.»","Congelá el precio de tu fiesta 2027",True),
   ("B","«Todo aumenta. Tu fiesta no tiene por qué.»","Todo aumenta. Tu fiesta, no.",False),
   ("C","«Si tu fiesta es en 2027, el mejor momento para pagarla es ahora.»","Fiesta 2027, precio de hoy",False),
   ("D","Cuenta regresiva: «Quedan [[DIAS]] días para reservar 2027 con precio de hoy.»","Quedan [[DIAS]] días",False)],
  rec="A + frapera con hielo: la metáfora se entiende sin sonido y usa un objeto propio del salón.",
  beats=[
   ("0–3 s","Frapera con hielo, etiqueta de precio","Gancho A","CONGELÁ EL PRECIO DE TU FIESTA 2027"),
   ("3–9 s","Plano medio en la barra","«Si reservás antes del [[FECHA LIMITE]], tu fiesta 2027 queda con el precio de hoy.» [VALIDAR]","PRECIO DE HOY HASTA EL [[FECHA LIMITE]]"),
   ("9–16 s","B-roll: salón armado, mesa dulce (VO)","«Pagás [[ANTICIPO]] para reservar y el resto en [[CUOTAS]] cuotas [[AJUSTE]].»","[[ANTICIPO]] + [[CUOTAS]] CUOTAS"),
   ("16–22 s","B-roll: pista llena de una fiesta real","«Mientras todo sube, tu fiesta ya está pagándose.»","TU FIESTA, YA EN MARCHA"),
   ("22–28 s","Primer plano en la barra","«Escribinos CONGELAR por WhatsApp y te reservamos la fecha.»","ESCRIBÍ «CONGELAR» →")],
  tomas=["Gancho con la frapera (5 tomas: el hielo nunca cae igual)","Plano medio en la barra, 2 lecturas","Detalle: etiqueta con el precio escrito a mano","Mesa dulce armada","Pista llena (material de eventos, con permiso)"],
  utileria=["Frapera con hielo real","Etiqueta de precio de cartulina con [[TOTAL]]","Barra iluminada"],
  ad=dict(principal="¿Tu fiesta es en 2027? Congelá hoy el precio 🧊 Si reservás antes del [[FECHA LIMITE]] en Trebelno Recepciones, tu fecha queda con el precio de hoy: [[ANTICIPO]] para reservar y el resto en [[CUOTAS]] cuotas. Escribinos «CONGELAR» y te pasamos disponibilidad y presupuesto.",
          titulo="Fiesta 2027 con precio de hoy", desc="Válido hasta el [[FECHA LIMITE]]", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! Quiero CONGELAR el precio de mi fiesta 2027. Mi fecha es: ___"),
  porque="En Argentina la estrategia más usada en salones es reservar con un anticipo y congelar el valor (lo cubrió El Cronista). Le pone un costo concreto a esperar y suma una fecha límite real, lo que acelera los mensajes.",
  notas="Solo si el salón congela el precio o lo mantiene hasta una fecha. Plan B si no congela: «Precio de lanzamiento Agenda 2027 hasta el [[FECHA LIMITE]]» con el mismo guion. Nunca prometer precio fijo si las cuotas se ajustan.",
 ),
 dict(
  n="03", tipo="eco", angulo="Oferta económica · todo lo que incluye",
  titulo="Todo esto entra en [[CUOTA]] por mes",
  idea="Le mostramos al que mira todo lo que está pagando, ítem por ítem. El precio se justifica antes de que lo pregunte y bajan las consultas de curiosos.",
  ficha=[("Objetivo","Mensajes de gente que ya entendió qué incluye"),("Duración","28–35 s"),("Quién","Anfitrión/a caminando + VO"),("Dónde","Recorrido completo del salón armado"),
         ("Audio","Sonido de «check» en cada ítem; música de fiesta de fondo"),("CTA","Pedí el detalle del paquete"),("Destino","Clic a WhatsApp"),("Exportar","9:16 · carrusel 4:5 de 7 placas")],
  gancho=("«Esto es todo lo que incluye una fiesta de [[CUOTA]] por mes.»","TODO ESTO POR [[CUOTA]]/MES","Las puertas del salón se abren hacia la pista iluminada; el anfitrión/a entra y señala hacia adentro"),
  variantes=[
   ("A","«Esto es todo lo que incluye una fiesta de [[CUOTA]] por mes.»","Todo esto por [[CUOTA]]/mes",True),
   ("B","«Sin sorpresas: esto incluye y esto no.»","Sin letra chica",False),
   ("C","«Lo que te cobran aparte en otros salones, acá ya está incluido.» [VALIDAR]","Ya incluido",False),
   ("D","«7 cosas que tu fiesta 2027 ya tiene resueltas.»","7 cosas ya resueltas",False)],
  rec="A: el contador 1/7 → 7/7 retiene hasta el final y el número de cuota queda en pantalla todo el video.",
  beats=[
   ("0–3 s","Apertura de puertas a la pista","Gancho A","TODO ESTO POR [[CUOTA]]/MES"),
   ("3–8 s","Salón con mesas armadas","«Uno: el salón para [[INVITADOS]] invitados, con [[DATO SALON]].»","1/7 · SALÓN"),
   ("8–13 s","Detalle del plato / cocina","«Dos: catering completo, [[MENU]].»","2/7 · CATERING"),
   ("13–17 s","Barra en acción","«Tres: barra [[BARRA]].»","3/7 · BARRA"),
   ("17–21 s","Cabina del DJ y luces","«Cuatro: DJ, sonido y luces.» «Cinco: [[AMBIENTACION]].»","4/7 · DJ · 5/7 AMBIENTACIÓN"),
   ("21–26 s","Coordinador/a con la planilla","«Seis: coordinación el día del evento. Siete: [[ITEM EXTRA]].»","6/7 · COORDINACIÓN · 7/7"),
   ("26–33 s","Primer plano en la pista","«Todo eso en [[CUOTAS]] cuotas de [[CUOTA]]. Pedí el detalle por WhatsApp.»","PEDÍ EL DETALLE →")],
  tomas=["Apertura de puertas (desde adentro y desde afuera)","1 plano detalle por ítem (7)","Coordinador/a real con la planilla del evento","Cierre en la pista, 2 versiones","Fotos fijas de cada ítem para el carrusel"],
  utileria=["Salón armado completo","Plato del menú emplatado","Planilla/tablet de coordinación"],
  ad=dict(principal="¿Qué incluye una fiesta en Trebelno Recepciones? ✔️ Salón para [[INVITADOS]] invitados ✔️ Catering completo ✔️ Barra ✔️ DJ, sonido y luces ✔️ Ambientación ✔️ Coordinación ✔️ [[ITEM EXTRA]]. Todo en [[CUOTAS]] cuotas de [[CUOTA]]. Escribinos y te mandamos el detalle del paquete para tu fecha 2027.",
          titulo="Todo incluido en [[CUOTAS]] cuotas", desc="Pedí el detalle del paquete", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! Quiero el detalle de lo que incluye el paquete para mi fiesta 2027."),
  porque="Jano's vende «paquetes» por niveles (All inclusive, VIP, Ultra VIP) y sus anuncios llevan a «conocé el paquete ideal para vos». Mostrar el contenido del paquete antes que el precio hace que la cuota se lea como barata.",
  notas="Los 7 ítems salen del cuestionario (bloque B). Si hay paquetes por niveles, grabar el del medio y nombrar los otros en el caption. Va bien también como carrusel estático para el feed.",
 ),
 dict(
  n="04", tipo="eco", angulo="Oferta económica · prueba social",
  titulo="«Lo pagamos en 12 cuotas»: una fiesta real",
  idea="Una familia (o pareja) cuenta que su fiesta se pagó en cuotas. El que duda escucha a alguien como él, no al salón.",
  ficha=[("Objetivo","Bajar la duda «¿se puede de verdad?» y generar mensajes"),("Duración","30–40 s"),("Quién","Cliente real (madre/padre de quinceañera o pareja)"),("Dónde","Salón vacío + material de su fiesta"),
         ("Audio","Voz del cliente en seco; música de su fiesta debajo"),("CTA","Escribinos y armamos el tuyo"),("Destino","Clic a WhatsApp"),("Exportar","9:16 · 4:5")],
  gancho=("(Cliente) «Hicimos los 15 de [[NOMBRE]] y lo pagamos en [[CUOTAS]] cuotas.»","LO PAGAMOS EN [[CUOTAS]] CUOTAS","Clip de la entrada de la quinceañera (o de la pareja) en su fiesta → corte seco al cliente sentado en el salón vacío"),
  variantes=[
   ("A","«Hicimos los 15 de [[NOMBRE]] y lo pagamos en [[CUOTAS]] cuotas.»","Lo pagamos en [[CUOTAS]] cuotas",True),
   ("B","«Pensábamos que no llegábamos. Llegamos.»","Pensábamos que no llegábamos",False),
   ("C","«Un año antes de la fiesta, empezamos a pagarla así.»","Así la pagamos",False),
   ("D","Anfitrión/a: «Esta familia reservó con [[ANTICIPO]]. Esta fue su fiesta.» (Plan B)","Reservaron con [[ANTICIPO]]",False)],
  rec="A: arranca con la emoción de la fiesta y la frase del cliente resume la oferta.",
  beats=[
   ("0–3 s","Clip de la entrada en su fiesta → cliente","Gancho A","LO PAGAMOS EN [[CUOTAS]] CUOTAS"),
   ("3–10 s","Plano medio del cliente","Respuesta a: ¿Qué pensaban antes de averiguar? (en sus palabras)","[[FRASE CLIENTE 1]]"),
   ("10–18 s","Plano medio, otro ángulo","Respuesta a: ¿Cómo la fueron pagando?","RESERVAMOS CON [[ANTICIPO]]"),
   ("18–27 s","Material de la fiesta (VO del cliente)","Respuesta a: ¿Qué es lo que más recordás de ese día?","[[FRASE CLIENTE 2]]"),
   ("27–35 s","Anfitrión/a primer plano","«¿Tu fiesta es en 2027? Escribinos y la armamos en cuotas.»","ESCRIBINOS · AGENDA 2027 →")],
  tomas=["Entrevista al cliente (10 min, 2 cámaras)","Planos de manos/fotos de la fiesta en la mesa","Cliente caminando el salón donde fue la fiesta","Cierre del anfitrión/a","Selección de 6–8 clips de la fiesta del cliente"],
  utileria=["Material de la fiesta del cliente (video del fotógrafo, con permiso)","Autorización de imagen firmada"],
  ad=dict(principal="«Pensábamos que no llegábamos con la plata, y lo pagamos en [[CUOTAS]] cuotas.» 💛 Así fueron los 15 de [[NOMBRE]] en Trebelno Recepciones. Si tu fiesta es en 2027, reservás con [[ANTICIPO]] y la vas pagando mes a mes. Escribinos tu fecha y te pasamos el presupuesto.",
          titulo="Ellos lo pagaron en cuotas", desc="Agenda 2027 abierta", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! Vi la fiesta de [[NOMBRE]] y quiero presupuesto en cuotas para 2027."),
  porque="En una compra de $13 millones el miedo es «¿será cierto?». Un cliente real que pagó en cuotas responde esa duda mejor que cualquier texto. Los estudios de caso de Meta para salones muestran que el testimonio en video es la prueba social que más funciona.",
  notas="Nada guionado en boca del cliente: se graba con las preguntas guía y se edita. Autorización escrita para redes y pauta. Si la venta del test 1 cierra con fiesta antes del rodaje, es la candidata ideal. Plan B: variante D con el anfitrión/a.",
 ),
 dict(
  n="05", tipo="nuevo", angulo="Ángulo nuevo · visita al salón",
  titulo="Entrá a tu fiesta 2027 antes de reservarla",
  idea="Recorrido en primera persona (POV) como si fueras el invitado de honor, y como cierre, una invitación a recorrer el salón en persona. Adaptamos «Open Jano's» (conocé el salón por dentro antes de decidir) a un salón propio.",
  ficha=[("Objetivo","Visitas agendadas al salón (leads de más calidad)"),("Duración","30–35 s"),("Quién","POV + anfitrión/a al final"),("Dónde","Entrada → recepción → salón → pista"),
         ("Audio","Ambiente real de la puerta; la música sube al llegar a la pista"),("CTA","Escribí VISITA"),("Destino","Clic a WhatsApp"),("Exportar","9:16 (estabilizado) · 4:5")],
  gancho=("(Texto, sin voz) «Así es llegar a tu fiesta 2027.»","ENTRÁ A TU FIESTA 2027","POV desde la vereda: se abre la puerta y las luces del salón se encienden de golpe"),
  variantes=[
   ("A","Texto: «Así es llegar a tu fiesta 2027.»","Entrá a tu fiesta 2027",True),
   ("B","«Antes de reservar, vení a verlo en persona.»","Conocelo antes de decidir",False),
   ("C","«Las fotos no le hacen justicia. Mirá.»","Las fotos no le hacen justicia",False),
   ("D","«El [[DIA VISITA]] abrimos el salón para vos.»","Salón abierto · [[DIA VISITA]]",False)],
  rec="A: el POV pone al que mira adentro de la fiesta y funciona sin sonido, que es como se ve la mayoría de los Reels pagos.",
  beats=[
   ("0–3 s","POV: puerta y luces","Sin voz. Sonido de la puerta","ENTRÁ A TU FIESTA 2027"),
   ("3–8 s","POV: recepción / hall","(VO) «Llegás y tus invitados ya te están esperando.»","LA RECEPCIÓN"),
   ("8–14 s","POV: travelling entre mesas armadas","(VO) «[[INVITADOS]] invitados, con [[DATO SALON]].»","EL SALÓN · [[INVITADOS]] INVITADOS"),
   ("14–20 s","POV: llegada a la pista, humo y luces","La música sube. Sin voz","LA PISTA"),
   ("20–25 s","Detalle: mesa dulce / barra","(VO) «Y todo lo demás, ya resuelto.»","TODO INCLUIDO"),
   ("25–33 s","Anfitrión/a en la pista, a cámara","«Vení a verlo en persona. Escribinos VISITA y te reservamos un horario para recorrerlo.»","ESCRIBÍ «VISITA» →")],
  tomas=["POV continuo con gimbal (3 tomas completas sin cortes)","Encendido de luces sincronizado (con el técnico)","Travelling entre mesas a la altura de los ojos","Pista con humo y luces móviles","Cierre del anfitrión/a, 2 versiones (visita / jornada abierta)"],
  utileria=["Gimbal o celular con estabilizador","Técnico de luces durante el rodaje","Salón armado completo, con humo"],
  ad=dict(principal="Antes de reservar tu fiesta 2027, entrá a verla ✨ Recorré Trebelno Recepciones en persona: el salón, la pista, la barra y todo lo que incluye tu paquete. Escribinos «VISITA» y te reservamos un horario. [[DIA VISITA]]",
          titulo="Conocé el salón antes de decidir", desc="Reservá tu horario de visita", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! Quiero agendar una VISITA al salón. Mi fiesta sería en 2027."),
  porque="Jano's tiene un formato fijo («Open Jano's») para que la gente recorra el salón antes de decidir. En un ticket alto la visita es el paso que más acerca a la seña, y el POV es el formato de recorrido que más se usa hoy en salones de afuera.",
  notas="Si el salón no hace jornadas abiertas, el CTA es una visita individual con turno. En WhatsApp hay que tener una respuesta rápida con los días y horarios de visita: si no, el lead se enfría.",
 ),
 dict(
  n="06", tipo="nuevo", angulo="Ángulo nuevo · fechas disponibles 2027",
  titulo="Agenda 2027: estos sábados ya no están",
  idea="Mostramos un calendario 2027 real con las fechas reservadas tachadas. La urgencia sale de la agenda, no de una promoción. Toma el «Consultá disponibilidad HOY» de Jano's y lo hace visible.",
  ficha=[("Objetivo","Que manden su fecha para consultar disponibilidad"),("Duración","20–28 s"),("Quién","Anfitrión/a a cámara"),("Dónde","Calendario 2027 grande en la pared del salón"),
         ("Audio","Fibrón real raspando el papel; sin música los primeros 2 s"),("CTA","Mandanos tu fecha"),("Destino","Clic a WhatsApp"),("Exportar","9:16 · 4:5 · estático del calendario")],
  gancho=("«Estos sábados de 2027 ya no están.»","AGENDA 2027 · YA SE ESTÁ LLENANDO","Primer plano: fibrón tachando un sábado en un calendario 2027 impreso; abre el plano y aparece el anfitrión/a"),
  variantes=[
   ("A","«Estos sábados de 2027 ya no están.»","Agenda 2027 · ya se está llenando",True),
   ("B","«¿Tu fecha 2027 sigue libre? Fijate acá.»","¿Tu fecha sigue libre?",False),
   ("C","«En [[MES PICO]] nos quedan [[N FECHAS]] sábados.»","Quedan [[N FECHAS]] sábados en [[MES PICO]]",False),
   ("D","«Los 15 se reservan con [[MESES]] meses de anticipación. Y los sábados se van primero.»","Los sábados se van primero",False)],
  rec="A + fibrón: el gesto de tachar se entiende al instante y genera la pregunta «¿y la mía?».",
  beats=[
   ("0–3 s","Fibrón tachando un sábado","Gancho A","AGENDA 2027 · YA SE ESTÁ LLENANDO"),
   ("3–9 s","Plano medio junto al calendario","«Las fiestas se reservan con [[MESES]] meses de anticipación, y los sábados son los primeros en irse.»","LOS SÁBADOS SE VAN PRIMERO"),
   ("9–15 s","Primer plano del calendario","«En [[MES PICO]] nos quedan [[N FECHAS]] sábados.» [VALIDAR]","[[MES PICO]] · QUEDAN [[N FECHAS]]"),
   ("15–21 s","B-roll: fiesta real en la pista (VO)","«Si ya tenés la fecha en mente, este es el momento de reservarla.»","TU FECHA, TU FIESTA"),
   ("21–27 s","Primer plano del anfitrión/a","«Mandanos tu fecha por WhatsApp y te decimos al toque si está libre. La reservás con [[ANTICIPO]].»","MANDANOS TU FECHA →")],
  tomas=["Tachado de fechas (3 fechas distintas, 3 tomas cada una)","Plano general: anfitrión/a + calendario","Primer plano del mes pico","Cierre a cámara","Foto del calendario completo para el estático"],
  utileria=["Calendario 2027 impreso grande (A1 o A0) con las fechas REALES ocupadas","Fibrón grueso bordó","Cinta para pegarlo en la pared"],
  ad=dict(principal="📅 Agenda 2027: los sábados se están reservando. Si tu fiesta de 15, casamiento o cumpleaños es en 2027, mandanos tu fecha y te decimos al toque si está libre en Trebelno Recepciones. La reservás con [[ANTICIPO]] y pagás el resto en cuotas.",
          titulo="¿Tu fecha 2027 sigue libre?", desc="Consultá disponibilidad hoy", boton="Enviar mensaje de WhatsApp",
          wsp="¡Hola! ¿Tienen disponible esta fecha en 2027? ___"),
  porque="Los anuncios de Jano's que siguen activos llevan a «Consultá por disponibilidad HOY». La fecha es la primera pregunta de cualquier cliente y el sábado es escaso de verdad: la escasez se puede mostrar sin inventar nada.",
  notas="Solo fechas que estén reservadas de verdad (Meta y la credibilidad del salón lo exigen). Actualizar el calendario y regrabar el primer plano cada 4–6 semanas: se convierte en una serie («Agenda 2027 · actualización»).",
 ),
]

VARIABLES = [
 ("TOTAL","Precio total del paquete de referencia (el más vendido)","01 02 03"),
 ("CUOTAS","Cantidad de cuotas (en el test 1 fueron 12)","01–06"),
 ("CUOTA","Valor de cada cuota del paquete de referencia","01 03 04"),
 ("ANTICIPO","Monto o % para reservar la fecha","01 02 04 06"),
 ("AJUSTE","Cuotas fijas o con ajuste (índice y frecuencia)","01 02"),
 ("INVITADOS","Cantidad de invitados del paquete de referencia","01 03 05"),
 ("INCLUYE 1-3 / MENU / BARRA / AMBIENTACION / ITEM EXTRA","Lo que incluye el paquete","01 03"),
 ("DATO SALON","Dato diferencial del salón (m², capacidad, parque, estacionamiento)","03 05"),
 ("FECHA LIMITE / DIAS","Hasta cuándo vale el precio de hoy o la promoción","02"),
 ("NOMBRE / FRASE CLIENTE","Cliente que da testimonio y sus frases textuales","04"),
 ("DIA VISITA","Días y horarios de visita o de jornada abierta","05"),
 ("MESES","Anticipación promedio con la que reservan","06"),
 ("MES PICO / N FECHAS","Mes más pedido y sábados que quedan libres","06"),
]

# --------------------------------------------------------------------------
def portada():
    return f"""
<section class="page"><div class="portada">
  <div>
    <div class="claqueta"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
    <div style="margin-top:12mm" class="kicker">Kit de rodaje · Meta Ads · Campaña 02</div>
    <h1>Agenda 2027,<br><em>en cuotas</em> y con<br>fecha propia.</h1>
    <p class="sub">Seis creativos con guion, lista de tomas, texto del anuncio y mensaje de WhatsApp. Los datos en amarillo se reemplazan por los números reales del salón el día de la grabación.</p>
  </div>
  <div>
    <div class="grid g3" style="margin-bottom:10mm">
      <div class="card tinta"><span class="lbl">Test 1</span><span class="big">325</span><br>mensajes</div>
      <div class="card tinta"><span class="lbl">Venta cerrada</span><span class="big">$13M</span><br>en 12 cuotas</div>
      <div class="card tinta"><span class="lbl">Esta campaña</span><span class="big">4 + 2</span><br>creativos</div>
    </div>
    <div class="pie">
      <div><b>Cliente</b><span>Trebelno Recepciones</span></div>
      <div><b>Campaña</b><span>Agenda 2027</span></div>
      <div><b>Versión</b><span>v1 · Noviembre 2026</span></div>
      <div><b>Dirección</b><span>JFL IT</span></div>
    </div>
  </div>
</div></section>"""

def estrategia():
    filas = "".join(f"""<tr><td class="n">{c['n']}</td><td><span class="chip {'eco' if c['tipo']=='eco' else 'nuevo'}">{'Ganador' if c['tipo']=='eco' else 'Nuevo'}</span> {v(c['angulo'].split('·')[1].strip())}</td>
      <td><b>{v(c['titulo'])}</b></td><td>{v(c['gancho'][1])}</td><td>{v(c['ad']['boton'].replace('Enviar mensaje de WhatsApp','WhatsApp'))} · {v(c['ficha'][5][1])}</td></tr>""" for c in CREATIVOS)
    return f"""
<section class="page">
  <div class="sec"><span class="n">01</span><h2>De dónde partimos y qué cambiamos</h2><span class="r">Estrategia</span></div>
  <div class="grid g4" style="margin-bottom:8px">
    <div class="card"><span class="lbl">Inversión test 1</span><span class="big" style="font-size:18pt">USD 300</span><br><span class="mini">52% del presupuesto total</span></div>
    <div class="card"><span class="lbl">Mensajes</span><span class="big">325</span><br><span class="mini">≈ USD 0,92 por conversación</span></div>
    <div class="card"><span class="lbl">Ventas</span><span class="big">1</span><br><span class="mini">$13.000.000 · 12 cuotas</span></div>
    <div class="card oro"><span class="lbl">Ángulo ganador</span><span class="serif" style="font-size:13pt">Oferta económica</span><br><span class="mini">cuotas · precio accesible</span></div>
  </div>
  <p class="mini">Costo por conversación calculado sobre USD 300; si los USD 300 eran el total y se usó el 52% (≈ USD 156), el costo baja a ≈ USD 0,48. Lo confirmamos en el Administrador de anuncios antes del lanzamiento.</p>
  <h3>La lectura</h3>
  <div class="grid g3">
    <div class="card"><span class="lbl">Lo que funcionó</span>Hablar de plata sin vueltas. Una fiesta de $13M se vende cuando se la ve como cuota mensual y con la fecha asegurada.</div>
    <div class="card"><span class="lbl">Lo que renovamos</span>El contenido. Mantenemos el ángulo y la estructura, pero grabamos nosotros: persona a cámara, números en pantalla y CTA a WhatsApp con mensaje precargado.</div>
    <div class="card"><span class="lbl">Lo que sumamos</span>Dos ángulos que la competencia sostiene en pauta: <b>visita al salón</b> (Open Jano's) y <b>fechas disponibles</b> («Consultá disponibilidad HOY»).</div>
  </div>
  <h3>Los seis creativos</h3>
  <table><tr><th>#</th><th>Ángulo</th><th>Creativo</th><th>Gancho en pantalla</th><th>CTA</th></tr>{filas}</table>
  <div class="sep"></div>
  <div class="nota">Cada creativo se graba con <b>4 ganchos</b>. Se editan el A (recomendado) y el B como anuncios separados: 6 creativos = 12 anuncios. Los ganchos C y D quedan grabados para la primera renovación (semana 3–4).</div>
</section>"""

def benchmark():
    return """
<section class="page">
  <div class="sec"><span class="n">02</span><h2>Qué está funcionando hoy</h2><span class="r">Competencia · Nov 2026</span></div>
  <p class="lead">Relevamiento en la Biblioteca de anuncios de Meta (Argentina, anuncios activos al 15/11/2026) y en fuentes del rubro en Argentina y afuera.</p>
  <h3>Jano's Eventos · el líder local</h3>
  <div class="grid g2">
    <div class="card">
      <span class="lbl">Lo que vimos en su pauta</span>
      <ul class="lim">
        <li>≈ 226 anuncios activos entre sus páginas (Jano's Eventos, János, Janos Eventos y Jano's Corporativos).</li>
        <li>Suben <b>tandas de 10 a 20 variantes el mismo día</b>: testean por volumen y dejan correr las que ganan.</li>
        <li>Todo va a <b>conversación</b>: «Escribinos y conocé el paquete ideal para vos», «Consultá por disponibilidad HOY», «Chateá con nosotros».</li>
        <li>Segmentan por tipo de evento («Tus 15 Únicos») y tienen una línea aparte para empresas (coffee break).</li>
      </ul>
    </div>
    <div class="card">
      <span class="lbl">Su oferta</span>
      <ul class="lim">
        <li>Paquetes por niveles: <b>All inclusive, VIP y Ultra VIP</b>, con salón, catering, barra, ambientación, sonido, luces y coordinación.</li>
        <li><b>Open Jano's</b>: jornadas para conocer el salón por dentro y recibir una propuesta en el momento.</li>
        <li>Financiación con anticipo (≈ 30%) y el resto en cuotas, con la fecha y el valor fijados al contratar (datos de notas de años anteriores).</li>
      </ul>
    </div>
  </div>
  <h3>Mercado local · salones pymes</h3>
  <div class="card">
    ≈ 2.900 anuncios activos con «salón de eventos» en Argentina. La mayoría son placas con precio y «fechas disponibles», sin persona a cámara ni recorrido. <b>Ahí está nuestra ventaja:</b> una cara del salón, números claros y un video que muestra el lugar armado. También se ve el uso de días de semana más baratos («de lunes a jueves»): conviene preguntarle al cliente si tiene precios por día (cuestionario, bloque C).
  </div>
  <h3>Tendencias del rubro</h3>
  <div class="grid g2">
    <div class="card"><span class="lbl">Argentina</span><ul class="lim">
      <li>Los 15 años se reservan con hasta <b>3 años de anticipación</b>.</li>
      <li>La estrategia más usada es <b>congelar el precio</b> con un anticipo y pagar el resto antes del evento.</li></ul></div>
    <div class="card"><span class="lbl">Internacional</span><ul class="lim">
      <li>Video vertical de recorrido para captar y testimonio para retargeting: un caso de Meta (Wedding Park) reporta +90% de conversiones.</li>
      <li>Paquete con precio cerrado + carrusel + públicos similares: un salón (Hermozo, caso de Meta) multiplicó por 4 sus reservas mensuales.</li>
      <li>Renovar creativos cada 2–4 semanas para que la campaña no se estanque.</li></ul></div>
  </div>
  <h3>Lo que tomamos</h3>
  <table>
    <tr><th>Señal del mercado</th><th>Cómo la usamos</th></tr>
    <tr><td>Volumen de variantes (Jano's)</td><td>4 ganchos por creativo y 2 editados por creativo desde el día 1.</td></tr>
    <tr><td>«Conocé el paquete ideal»</td><td>Creativo 03: todo lo que incluye, ítem por ítem.</td></tr>
    <tr><td>Open Jano's</td><td>Creativo 05: recorrido POV + invitación a visitar.</td></tr>
    <tr><td>«Consultá disponibilidad HOY»</td><td>Creativo 06: calendario 2027 con fechas reales tachadas.</td></tr>
    <tr><td>Congelamiento de precio</td><td>Creativo 02: precio de hoy con fecha límite.</td></tr>
    <tr><td>Testimonio en retargeting</td><td>Creativo 04: va a quienes ya interactuaron (videos al 50% y conversaciones).</td></tr>
  </table>
  <div class="sep"></div>
  <p class="fuente">Fuentes: Biblioteca de anuncios de Meta (consulta 15/11/2026) · janoseventos.com/15-anos · janoseventos.com/open-janos-conoce-el-salon-por-dentro-antes-de-tomar-la-decision · cronista.com/negocios/la-estrategia-mas-usada-para-congelar-precios-de-cumpleanos-de-15-y-casamientos · viapais.com.ar (costos Jano's) · iprofesional.com/actualidad/377462 · casestudies.com (Facebook: Wedding Park, Hermozo) · tripleseat.com/blog · eventtemple.com/blog</p>
</section>"""

def estructura():
    return """
<section class="page">
  <div class="sec"><span class="n">03</span><h2>Estructura de campaña</h2><span class="r">Meta Ads · Mensajes</span></div>
  <div class="grid g3">
    <div class="card tinta"><span class="lbl">Campaña</span><span class="serif" style="font-size:13pt">Interacción · Mensajes</span><br>Destino WhatsApp. Presupuesto por conjunto (ABO) las 2 primeras semanas para que los ángulos nuevos reciban inversión.</div>
    <div class="card"><span class="lbl">Conjunto A · 65%</span><b>Oferta económica</b><br>Creativos 01, 02 y 03 (A y B) + el mejor anuncio del test 1 como control.</div>
    <div class="card"><span class="lbl">Conjunto B · 25%</span><b>Ángulos nuevos</b><br>Creativos 05 y 06 (A y B). Mismo público que A para comparar parejo.</div>
  </div>
  <div class="grid g3" style="margin-top:8px">
    <div class="card"><span class="lbl">Conjunto C · 10%</span><b>Retargeting</b><br>Creativo 04 (testimonio) + 06. Público: video visto al 50%, interacción con la cuenta y conversaciones de los últimos 60 días.</div>
    <div class="card"><span class="lbl">Público</span>Amplio con Advantage+ y radio de <span class="var">KM</span> km alrededor del salón. Edad <span class="var">EDAD</span> según tipo de evento (padres de 15 años / parejas). Sin intereses al inicio.</div>
    <div class="card"><span class="lbl">Ubicaciones</span>Advantage+. Prioridad Reels e Historias de Instagram y Facebook (9:16); Feed con 4:5.</div>
  </div>
  <h3>Reglas de decisión</h3>
  <table>
    <tr><th>Momento</th><th>Mirar</th><th>Decisión</th></tr>
    <tr><td>Día 3–4 (≈ USD 15 por anuncio)</td><td>Tasa de gancho (reproducciones de 3 s ÷ impresiones) &gt; 25%</td><td>Si está por debajo, se pausa ese gancho y entra el C o el D.</td></tr>
    <tr><td>Día 7</td><td>Costo por conversación vs. test 1 (≈ USD 0,92)</td><td>Más de 1,5× → pausar. Por debajo → +20% de presupuesto cada 72 h.</td></tr>
    <tr><td>Día 14</td><td>Conversaciones calificadas (dieron fecha e invitados) y visitas agendadas</td><td>Pasar a CBO con los 4–5 mejores anuncios. El ángulo nuevo que gane suma 2 creativos en la renovación.</td></tr>
    <tr><td>Día 21–28</td><td>Frecuencia &gt; 3 o costo en subida</td><td>Renovación: ganchos C/D + actualización del calendario 2027.</td></tr>
  </table>
  <h3>WhatsApp: donde se gana la venta</h3>
  <div class="grid g2">
    <div class="card"><span class="lbl">Etiquetas en WhatsApp Business</span><ul class="lim">
      <li>Nuevo · Calificado (dio fecha + invitados) · Visita agendada · Presupuesto enviado · Seña · Perdido.</li>
      <li>Con estas etiquetas medimos <b>costo por conversación calificada</b> y <b>costo por seña</b>, no solo por mensaje.</li></ul></div>
    <div class="card"><span class="lbl">Respuesta en menos de 5 minutos</span><ul class="lim">
      <li>Respuestas rápidas por ángulo: /cuotas, /congelar, /incluye, /visita, /fecha.</li>
      <li>Primera pregunta siempre: «¿Para qué fecha y cuántos invitados?»</li>
      <li>Si se puede, cargar la seña como evento de compra (API de conversiones) para que Meta optimice hacia ventas.</li></ul></div>
  </div>
  <div class="sep"></div>
  <div class="nota roja">Política de Meta: la escasez y el congelamiento tienen que ser reales. Las fechas tachadas del creativo 06 y la fecha límite del 02 se confirman con el cliente por escrito antes de publicar.</div>
</section>"""

def rodaje():
    return """
<section class="page">
  <div class="sec"><span class="n">04</span><h2>Plan de la jornada de grabación</h2><span class="r">Un día · un salón armado</span></div>
  <p class="lead">Todo se graba en una jornada con el salón armado como para un evento. El orden sigue la luz y el armado, no el número del creativo.</p>
  <table>
    <tr><th>Bloque</th><th>Hora</th><th>Qué se graba</th><th>Creativos</th><th>Listo</th></tr>
    <tr><td class="n">1</td><td><span class="var">HORA</span></td><td>Llegada, salón armado intacto: planos generales, travelling entre mesas, detalles de centros de mesa</td><td>03 05</td><td><span class="box"></span></td></tr>
    <tr><td class="n">2</td><td>+1 h</td><td>POV completo entrada → pista con encendido de luces y humo (3 tomas completas)</td><td>05</td><td><span class="box"></span></td></tr>
    <tr><td class="n">3</td><td>+2 h</td><td>Anfitrión/a en la pista: ganchos y cierres de 01, 03 y 05</td><td>01 03 05</td><td><span class="box"></span></td></tr>
    <tr><td class="n">4</td><td>+3 h</td><td>Barra: frapera con hielo, barra en acción, plano medio</td><td>02 03</td><td><span class="box"></span></td></tr>
    <tr><td class="n">5</td><td>+4 h</td><td>Calendario 2027 en la pared: tachados, plano general y primer plano</td><td>06</td><td><span class="box"></span></td></tr>
    <tr><td class="n">6</td><td>+5 h</td><td>Entrevista al cliente (testimonio) con 2 cámaras + paseo por el salón</td><td>04</td><td><span class="box"></span></td></tr>
    <tr><td class="n">7</td><td>+6 h</td><td>Detalles de catering y mesa dulce · fotos fijas para carrusel y estáticos</td><td>03 06</td><td><span class="box"></span></td></tr>
  </table>
  <div class="grid g2" style="margin-top:10px">
    <div class="card"><span class="lbl">Equipo</span><ul class="check">
      <li>Celular 4K 9:16 (+ uno de respaldo)</li><li>Gimbal / estabilizador</li><li>2 micrófonos corbateros</li><li>Luz LED de rostro + difusor</li>
      <li>Trípode</li><li>Baterías y cargadores</li><li>Calendario 2027 impreso (A1/A0)</li><li>Fibrón grueso bordó</li><li>Frapera + hielo</li><li>Etiqueta de precio</li><li>Autorizaciones de imagen impresas</li><li>Este kit impreso</li></ul></div>
    <div class="card"><span class="lbl">Antes de grabar</span><ul class="check one">
      <li>Cuestionario respondido y números confirmados (sección 05)</li>
      <li>Salón armado completo y técnico de luces disponible</li>
      <li>Anfitrión/a definido/a, con el guion leído (se dice con sus palabras, no se lee)</li>
      <li>Cliente para el testimonio confirmado, con autorización firmada</li>
      <li>Fechas reales ocupadas de 2027 marcadas en el calendario</li>
      <li>Vestuario: liso, sin logos, color que contraste con el salón</li>
      <li>Grabar 2 cierres por creativo: 15 años y casamiento/cumpleaños</li></ul></div>
  </div>
  <h3>Reglas de edición para los 6</h3>
  <div class="grid g3">
    <div class="card"><span class="lbl">Ritmo</span>Corte cada 2–3 s. El gancho entra en el cuadro 1: nada de logo ni introducción al principio.</div>
    <div class="card"><span class="lbl">Texto</span>Subtítulos siempre (más del 80% se ve sin sonido). El texto principal va en el tercio medio, fuera de la zona de botones.</div>
    <div class="card"><span class="lbl">Cierre</span>Placa final 1,5 s: logo + «Agenda 2027» + ícono de WhatsApp. Sin teléfono escrito (el botón ya lo resuelve).</div>
  </div>
</section>"""

def creativo(c, hoja):
    cls = "nuevo" if c["tipo"]=="nuevo" else "eco"
    ficha = "".join(f'<div><span class="lbl">{k}</span>{v(x)}</div>' for k,x in c["ficha"])
    vars_ = "".join(f'<li class="{"rec" if r else ""}"><b class="l">{l}{" ★" if r else ""}</b><span>{v(d)}</span><span class="scr">{v(s)}</span></li>' for l,d,s,r in c["variantes"])
    beats = '<div class="beat h"><div class="tc">Tiempo</div><div class="pl">Plano</div><div>Qué se dice</div><div>Texto en pantalla</div></div>'
    beats += "".join(f'<div class="beat avoid"><div class="tc">{t}</div><div class="pl">{v(p)}</div><div class="dice">{v(d)}</div><div class="lee">{v(l)}</div></div>' for t,p,d,l in c["beats"])
    tomas = "".join(f"<li>{v(t)}</li>" for t in c["tomas"])
    uti = "".join(f"<li>{v(t)}</li>" for t in c["utileria"])
    ad = c["ad"]
    return f"""
<section class="page {cls}-sec">
  <div class="cab {cls}">
    <div class="num"><small>Creativo</small><b>{c['n']}</b><small>{'Ganador' if cls=='eco' else 'Nuevo'}</small></div>
    <div class="tit"><span class="chip {cls}">{'Ángulo ganador' if cls=='eco' else 'Ángulo nuevo'}</span><span class="chip neutro">{v(c['angulo'].split('·')[1].strip())}</span>
      <h2>{v(c['titulo'])}</h2><div class="idea">{v(c['idea'])}</div></div>
    <div class="estado"><span><i class="box"></i>Grabado</span><span><i class="box"></i>Editado A</span><span><i class="box"></i>Editado B</span><span><i class="box"></i>Aprobado</span><span><i class="box"></i>En Meta</span></div>
  </div>
  <div class="ficha">{ficha}</div>
  <div class="gancho-tit"><h3>El gancho · 0 a 3 s</h3><span class="mini">Lo que decide si el anuncio se mira o se pasa</span></div>
  <div class="gancho avoid">
    <div><span class="lbl">Se dice</span><div class="t">{v(c['gancho'][0])}</div></div>
    <div><span class="lbl">Se lee en pantalla</span><div class="pantalla">{v(c['gancho'][1])}</div></div>
    <div><span class="lbl">Se ve</span>{v(c['gancho'][2])}</div>
  </div>
  <span class="lbl">Cuatro ganchos para grabar · se editan A y B</span>
  <ul class="variantes">{vars_}</ul>
  <p class="mini">★ {v(c['rec'])}</p>
  <h3>Guion</h3>
  <div class="riel">{beats}</div>
</section>
<section class="page {cls}-sec">
  <div class="sec"><span class="n">{c['n']}</span><h2 style="font-size:15pt">{v(c['titulo'])}</h2><span class="r">Producción y anuncio</span></div>
  <div class="grid g2 avoid">
    <div class="card"><span class="lbl">Lista de tomas</span><ul class="check one">{tomas}</ul></div>
    <div class="card"><span class="lbl">Utilería y preparación</span><ul class="check one">{uti}</ul></div>
  </div>
  <h3>El anuncio en Meta</h3><p class="mini">Mismo texto para las versiones A y B. Primera línea = gancho: es lo único que se ve antes del «ver más».</p>
  <div class="ad avoid">
    <div class="row"><div>Texto principal</div><div>{v(ad['principal'])}</div></div>
    <div class="row"><div>Título</div><div><b>{v(ad['titulo'])}</b></div></div>
    <div class="row"><div>Descripción</div><div>{v(ad['desc'])}</div></div>
    <div class="row"><div>Botón</div><div>{ad['boton']}</div></div>
    <div class="row"><div>Mensaje precargado</div><div>{v(ad['wsp'])}</div></div>
  </div>
  <div class="sep"></div>
  <div class="grid g2 avoid">
    <div class="nota"><b>Por qué funciona.</b> {v(c['porque'])}</div>
    <div class="nota roja"><b>Notas y plan B.</b> {v(c['notas'])}</div>
  </div>
  <h3>Cómo lo medimos</h3>
  <table class="avoid"><tr><th>Indicador</th><th>Meta</th><th>Versión A</th><th>Versión B</th></tr>
    <tr><td>Tasa de gancho (3 s ÷ impresiones)</td><td>&gt; 25%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Retención al 50% del video</td><td>&gt; 15%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Costo por conversación</td><td>&lt; USD 0,92</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Conversaciones calificadas (fecha + invitados)</td><td>&gt; 40%</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
    <tr><td>Visitas agendadas / señas</td><td>—</td><td><div class="escribir" style="min-width:0"></div></td><td><div class="escribir" style="min-width:0"></div></td></tr>
  </table>
</section>"""

def variables():
    filas = "".join(f'<tr><td><span class="var" style="white-space:normal">{k}</span></td><td>{d}</td><td>{w}</td><td><div class="escribir" style="min-width:0;height:20px"></div></td><td><span class="box"></span></td></tr>' for k,d,w in VARIABLES)
    return f"""
<section class="page">
  <div class="sec"><span class="n">05</span><h2>Datos a reemplazar</h2><span class="r">Completar antes de grabar</span></div>
  <p class="lead">Cada casilla amarilla del kit es un dato del salón. Se completa acá una sola vez, a mano o el día de la grabación, y se usa el mismo valor en los guiones, los textos del anuncio y las respuestas de WhatsApp.</p>
  <div class="nota">Referencia del test 1: venta de <b>$13.000.000 en 12 cuotas</b> = <b>≈ $1.083.333 por mes</b> (sin ajuste). Sirve de ejemplo para el creativo 01 si el cliente confirma que ese es su paquete más vendido.</div>
  <table style="table-layout:fixed"><colgroup><col style="width:44mm"><col><col style="width:20mm"><col style="width:48mm"><col style="width:9mm"></colgroup><tr><th>Dato</th><th>Qué es</th><th>Creativos</th><th>Valor real</th><th>OK</th></tr>{filas}</table>
  <div class="sep"></div>
  <div class="grid g2">
    <div class="card"><span class="lbl">Firma del cliente · datos aprobados</span><div style="height:22mm"></div><div class="escribir"></div><span class="mini">Nombre y fecha</span></div>
    <div class="card"><span class="lbl">Notas del día de grabación</span><div style="height:30mm"></div></div>
  </div>
</section>"""

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Trebelno · Kit de rodaje Agenda 2027</title><style>{CSS}</style></head><body>
{portada()}{estrategia()}{benchmark()}{estructura()}{rodaje()}
{''.join(creativo(c, 6+i) for i,c in enumerate(CREATIVOS))}
{variables()}
</body></html>"""
(AQUI / "guiones.html").write_text(html, encoding="utf-8")
print("ok guiones.html")
