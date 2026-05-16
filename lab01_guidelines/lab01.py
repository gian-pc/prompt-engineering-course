from helper import get_completion

# ============================================
# PRINCIPIO 1: Instrucciones claras y especificas
# ============================================

# --------------------------------------------
# Tactica 1: Usar delimitadores
# --------------------------------------------
text = f"""
Debes expresar lo que quieres que un modelo haga \
proporcionando instrucciones que sean lo mas claras \
y especificas que puedas.
"""

prompt = f"""
Resume el texto delimitado por triple comillas \
en una sola oracion.
```{text}```
"""

response = get_completion(prompt)
print(response)

# --------------------------------------------
# Tactica 2: Pedir salida estructurada (JSON)
# --------------------------------------------
prompt = f"""
Genera una lista de tres titulos de libros inventados \
junto con sus autores y generos.
Proporcionalos en formato JSON con las siguientes claves:
book_id, titulo, autor, genero.
"""

response = get_completion(prompt)
print(response)

# --------------------------------------------
# Tactica 3: Pedir al modelo que verifique condiciones
# --------------------------------------------
text_1 = f"""
¡Hacer una taza de te es facil! Primero, necesitas \
hervir agua. Mientras eso pasa, agarra una taza y \
ponle una bolsita de te. Una vez que el agua este \
caliente, viertela sobre la bolsita. Dejala reposar \
unos minutos para que el te se infusione. Luego \
saca la bolsita. Si quieres, agrega azucar o leche \
al gusto. ¡Y listo! Ya tienes una deliciosa taza de te.
"""

prompt = f"""
Se te proporcionara un texto delimitado por triple comillas.
Si contiene una secuencia de instrucciones, \
reescribe esas instrucciones en el siguiente formato:

Paso 1 - ...
Paso 2 - ...
...
Paso N - ...

Si el texto no contiene una secuencia de instrucciones, \
escribe simplemente: "No se proporcionaron pasos."

\"\"\"{text_1}\"\"\"
"""

response = get_completion(prompt)
print("Resultado para Texto 1:")
print(response)

text_2 = f"""
Hoy el sol brilla intensamente y los pajaros estan \
cantando. Es un dia hermoso para caminar por el parque. \
Las flores estan floreciendo y los arboles se mecen \
suavemente con la brisa. La gente esta afuera \
disfrutando del buen clima. Algunos hacen picnic, \
otros juegan o simplemente descansan en el cesped.
"""

prompt = f"""
Se te proporcionara un texto delimitado por triple comillas.
Si contiene una secuencia de instrucciones, \
reescribe esas instrucciones en el siguiente formato:

Paso 1 - ...
Paso 2 - ...
...
Paso N - ...

Si el texto no contiene una secuencia de instrucciones, \
escribe simplemente: "No se proporcionaron pasos."

\"\"\"{text_2}\"\"\"
"""

response = get_completion(prompt)
print("Resultado para Texto 2:")
print(response)

# --------------------------------------------
# Tactica 4: Few-shot prompting(Prompting con pocos ejemplos)
# --------------------------------------------
prompt = f"""
Tu tarea es responder con un estilo consistente.

<hijo>: Enséñame sobre la paciencia.

<abuelo>: El rio que esculpe el valle mas profundo \
fluye desde un modesto manantial; la \
sinfonia mas grandiosa se origina de una \
sola nota; el tapiz mas elaborado \
comienza con un solo hilo solitario.

<hijo>: Enséñame sobre la resiliencia.
"""

response = get_completion(prompt)
print(response)


# ============================================
# PRINCIPIO 2: Dale tiempo al modelo para pensar
# ============================================

# --------------------------------------------
# Tactica 1: Especificar los pasos
# --------------------------------------------
text = f"""
En un encantador pueblo, los hermanos Jack y Jill \
salen en una busqueda para buscar agua de un pozo \
en lo alto de una colina. Mientras subian, cantando \
alegremente, Jack tropezó con una piedra y cayó \
colina abajo, seguido de Jill. Aunque un poco golpeados, \
la pareja regresó a casa. A pesar del percance, \
su espiritu aventurero no se vio afectado y \
continuaron explorando con alegria.
"""

prompt = f"""
Realiza las siguientes acciones con el texto \
delimitado por triple comillas:
1 - Resume el texto en una oración.
2 - Traduce el resumen al frances.
3 - Lista cada nombre del resumen en frances.
4 - Genera un objeto JSON con las siguientes claves: \
nombres_franceses, numero_de_nombres.

Separa tus respuestas con saltos de linea.

\"\"\"{text}\"\"\"
"""

response = get_completion(prompt)
print("Respuesta:")
print(response)

prompt_2 = f"""
Realiza las siguientes acciones con el texto \
delimitado por triple comillas:
1 - Resume el texto en una oración.
2 - Traduce el resumen al frances.
3 - Lista cada nombre del resumen en frances.
4 - Genera un objeto JSON con las siguientes claves: \
nombres_franceses, numero_de_nombres.

Usa el siguiente formato de respuesta:
Texto: <texto original>
Resumen: <resumen>
Traduccion: <traduccion del resumen>
Nombres: <lista de nombres en el resumen en frances>
JSON: <json con nombres_franceses y numero_de_nombres>

\"\"\"{text}\"\"\"
"""

response_2 = get_completion(prompt_2)
print("Respuesta 2:")
print(response_2)


# --------------------------------------------
# Tactica 2: Pedir al modelo que razone antes de concluir
# --------------------------------------------
prompt = f"""
Determina si la solucion del estudiante es correcta o no.

Pregunta:
Estoy construyendo una instalacion de energia solar \
y necesito ayuda para calcular los costos financieros.
- El costo del terreno es de 100 dolares por pie cuadrado
- Puedo comprar paneles solares por 250 dolares por pie cuadrado
- Negocié un contrato de mantenimiento que me costara \
100 dolares fijos al año, y 10 dolares adicionales \
por pie cuadrado.
¿Cual es el costo total para el primer año en funcion \
del numero de pies cuadrados?

Solucion del estudiante:
Sea x el tamaño de la instalacion en pies cuadrados.
Costos:
1. Costo del terreno: 100x
2. Costo de paneles solares: 250x
3. Costo de mantenimiento: 100 + 100x
Costo total: 100x + 250x + 100 + 100x = 450x + 100
"""

response = get_completion(prompt)
print(response)


prompt = f"""
Tu tarea es determinar si la solucion del estudiante \
es correcta o no.
Para resolver el problema haz lo siguiente:
- Primero, encuentra tu propia solucion al problema.
- Luego compara tu solucion con la del estudiante \
y evalua si la solucion del estudiante es correcta o no.
No decidas si la solucion del estudiante es correcta \
hasta que hayas resuelto el problema tu mismo.

Pregunta:
Estoy construyendo una instalacion de energia solar \
y necesito ayuda para calcular los costos financieros.
- El costo del terreno es de 100 dolares por pie cuadrado
- Puedo comprar paneles solares por 250 dolares por pie cuadrado
- Negocié un contrato de mantenimiento que me costara \
100 dolares fijos al año, y 10 dolares adicionales \
por pie cuadrado.
¿Cual es el costo total para el primer año en funcion \
del numero de pies cuadrados?

Solucion del estudiante:
Sea x el tamaño de la instalacion en pies cuadrados.
Costos:
1. Costo del terreno: 100x
2. Costo de paneles solares: 250x
3. Costo de mantenimiento: 100 + 100x
Costo total: 100x + 250x + 100 + 100x = 450x + 100
"""
print("-------------------------------------------")
response = get_completion(prompt)
print(response)


# --------------------------------------------
# Alucinaciones
# --------------------------------------------
prompt = f"""
Cuentame sobre el cepillo de dientes inteligente \
AeroGlide UltraSlim de Boie.
"""

response = get_completion(prompt)
print(response)