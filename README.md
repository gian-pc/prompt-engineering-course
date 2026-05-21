# ChatGPT Prompt Engineering for Developers

Laboratorios del curso de DeepLearning.AI practicados desde PyCharm con Python.
Curso original: [DeepLearning.AI](https://www.deeplearning.ai/courses/chatgpt-prompt-eng)

## Tecnologías
- Python 3.14
- OpenAI API (gpt-3.5-turbo)
- PyCharm

## Laboratorios

### ✅ Lab 01 - Guidelines
Principios fundamentales del prompting.

**Principio 1: Instrucciones claras y específicas**
- Táctica 1: Usar delimitadores para separar instrucciones del contenido
- Táctica 2: Pedir salida estructurada (JSON)
- Táctica 3: Pedir al modelo que verifique condiciones antes de actuar
- Táctica 4: Few-shot prompting — dar ejemplos antes de la tarea real

**Principio 2: Dale tiempo al modelo para pensar**
- Táctica 1: Especificar pasos para completar una tarea
- Táctica 2: Pedir al modelo que razone antes de concluir

**Alucinaciones**
- Los modelos pueden inventar información con total confianza
- Nunca usar un LLM como fuente de verdad sin verificar

---

### ✅ Lab 02 - Iterative
Desarrollo iterativo de prompts para generar copy de marketing.

**Concepto principal:** Ningún prompt es perfecto a la primera — lo importante es el proceso de refinamiento.

**Ciclo iterativo:**
1. Escribir un primer prompt
2. Ver el resultado
3. Identificar el problema
4. Refinar el prompt
5. Repetir hasta llegar al resultado deseado

**Problemas resueltos:**
- Problema 1: Texto muy largo → limitar número de palabras
- Problema 2: Enfoque incorrecto → especificar audiencia y detalles técnicos
- Problema 3: Falta de estructura → pedir formato HTML con tabla de dimensiones

---

### ✅ Lab 03 - Summarizing
Resumir reseñas de productos de ecommerce con enfoque específico.

**Concepto principal:** El mismo texto puede resumirse de formas 
diferentes según el departamento o propósito que lo necesite.

**Ejercicios:**
- Resumir con límite de palabras (máximo 30 palabras)
- Resumir con enfoque en envío y entrega
- Resumir con enfoque en precio y valor percibido
- Extraer vs Resumir — diferencia clave entre ambos enfoques
- Resumir múltiples reseñas con un loop automatizado

**Aprendizaje clave:** Con un loop de Python puedes procesar 
cientos de reseñas automáticamente — la diferencia entre usar 
el chat manualmente y construir una aplicación real.

---
### ✅ Lab 04 - Inferring
Inferir sentimientos, emociones y temas a partir de texto.

**Concepto principal:** El modelo analiza un texto y deduce 
información que no está explícitamente escrita — como detectar 
emociones, sentimientos o temas sin entrenamiento previo.

**Ejercicios:**
- Detectar sentimiento positivo/negativo (respuesta completa vs una palabra)
- Identificar emociones específicas del cliente
- Detectar enojo para priorizar atención al cliente
- Extraer producto y marca en formato JSON
- Múltiples tareas en un solo prompt — más eficiente y económico
- Inferir temas de un artículo de noticias
- Crear alertas automáticas por tema — Zero-Shot Learning

**Aprendizaje clave:** Con un solo prompt puedes reemplazar 
semanas de trabajo de machine learning tradicional. 
Zero-Shot Learning significa que el modelo clasifica 
sin ejemplos previos — solo con el prompt.

---
### ✅ Lab 05 - Transforming
Transformar texto usando LLMs para múltiples propósitos.

**Concepto principal:** Los LLMs pueden transformar texto 
de una forma a otra — idioma, tono, formato o estilo — 
con un solo prompt.

**Ejercicios:**
- Traducción básica entre idiomas
- Detectar el idioma de un texto automáticamente
- Traducir a múltiples idiomas en una sola llamada
- Traducción formal e informal
- Traductor universal con loop — mensajes de soporte en 5 idiomas
- Transformación de tono — de jerga informal a carta formal
- Conversión de formatos — JSON a tabla HTML
- Corrección ortográfica y gramatical automática
- Visualizar cambios con redlines
- Mejorar estilo y tono de un texto

**Aprendizaje clave:** Una tarea que antes requería código 
complejo con expresiones regulares ahora se resuelve 
con un solo prompt.

---
### ⏳ Lab 06 - Expanding
### ⏳ Lab 07 - Chatbot