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
### ⏳ Lab 04 - Inferring
### ⏳ Lab 05 - Transforming
### ⏳ Lab 06 - Expanding
### ⏳ Lab 07 - Chatbot