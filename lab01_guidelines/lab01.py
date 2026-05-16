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