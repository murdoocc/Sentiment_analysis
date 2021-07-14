# Analisis de sentimientos a traves de un sistema web

El sistema fue desarrollado haciendo uso de tecnologías que implementan Redes neuronales. Dado que el sistema busca predecir los sentimientos, el tipo de Red fue de una arquitectura recientemente integrada para tareas referentes al analisis del lenguaje:

## Redes Transformer

Las redes transformer implementan una arquitectura en la cual su nucleo esta conformado por un bloque atencional, el cual tiene la tarea de extraer lo más importante del texto que recibio como entrada.

## BERT

Conocido como un modelo que implementa a la red transformer y agrega la función de analizar el texto de manera bidereccional, además es un modelo pre - entrenado el cual ya entiende el texto y solo necesita volver a ser entrenado para conocer cual será su tarea:

* Inferencia de texto
* Correción grámatical
* Preguntas y respuestas
* Análisis de emociones
* Entre otros...

## Requisitos del sistema

El sistema puede ser compilado de 3 formas según la disposición de la Unidad de Procesamiento Gráfico (GPU) por parte de la computadora:

1. El Sistema web en su toalidad el cual consume tanto la red transformer como bert ajustado:
[] 2GB
[] 4GB
[x] 8GB

3. La red transformer que traduce el idioma de español a ingles:
[x] 2GB
[] 4GB
[] 8GB

5. El modelo **BERT** afinado para el analisis de sentmientos:
[] 2GB
[x] 4GB
[x] 8GB

## Instalación de paquetes

- Principalmente se necesita tener instalado python, de la versión 3.8 en adelante es funcional para todo lo demás. [Instalación de Python] (https://www.python.org/downloads/)
- Instalar Django es necesario para la cuestión del sistema web, basta con codificar **py -m pip install Django** en la consola para tener Django funcionando.
- Las dos librerias principales con las cuales podemos trabajar todo lo referente a las redes transformer, bert y demás, es con las siguientes lineas de codigo:
  -
  -
  -







