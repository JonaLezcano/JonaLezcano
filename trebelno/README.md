# Trebelno Recepciones · Campaña Meta Ads "Agenda 2027"

- `pdf/Trebelno_Cuestionario_Oferta_Comercial.pdf`: cuestionario para el cliente (40 preguntas, ★ = necesarias antes de grabar).
- `pdf/Trebelno_Kit_de_Rodaje_Agenda2027.pdf`: estrategia, competencia, estructura de campaña, plan de rodaje y 6 creativos (4 del ángulo ganador + 2 nuevos), con los datos a reemplazar.

Los datos en amarillo (`[[VARIABLE]]` en `src/guiones.py`) son los números reales del salón. Para regenerar:

```
cd src && python3 guiones.py && python3 cuestionario.py && node imprimir.js
```
