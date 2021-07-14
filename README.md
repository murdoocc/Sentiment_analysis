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
- [ ] 2GB
- [ ] 4GB
- [x] 8GB

3. La red transformer que traduce el idioma de español a ingles:
- [x] 2GB
- [ ] 4GB
- [ ] 8GB

5. El modelo **BERT** afinado para el analisis de sentmientos:
- [ ] 2GB
- [x] 4GB
- [x] 8GB


## Instalación de paquetes

- Principalmente se necesita tener instalado python, de la versión 3.8 en adelante es funcional para todo lo demás. [Instalación de Python] (https://www.python.org/downloads/)
- Instalar Django es necesario para la cuestión del sistema web, basta con codificar **py -m pip install Django** en la consola para tener Django funcionando.
- Las dos librerias principales con las cuales podemos trabajar todo lo referente a las redes transformer, bert y demás, es con las siguientes lineas de codigo:
  - pip install keras-transformer
  - pip install transformers==3
  - pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
  - Adicional a las librerias necesarias hay librerias muy utilies independientes del proposito en el codigo de Python:
    - pip install numpy
    - pip install pandas


### Uso del sistema en su totalidad

Para ello debes de clonar el repositorio completo, si tienes un gestor de codigo como visual estudio puedes abrir la carpeta y abrir una terminal de linea de comandos, de lo contrario solo basta con abrir una linea de comandos y ubicarte en la dirección donde hayas clonado el repositorio
1. En la linea de comandos iniciaras el servidor de Django con **python manage.py runserver**, antes de ello como es tu primera interacción necesitas cargar las migraciones de los modelos y crear tu super usuario (el super usuario solo es si quieres administrar las entradas de oraciones del sistema):
   * Para las migraciones (python manage.py makemigrations y python manage.py migrate) **ASEGURATE DE ESTAR EN LA CARPETA DONDE ESTE EL ARCHIVO manage.py antes de ejecutar**
   * Crear un administrador con python manage.py createsuperuser, sigue los pasos que te muestra en la consola y inicia el servidor con python manage.py runserver
2. Una vez hayas iniciado el servidor puedes dirigite a dos ventanas, la principal y la del administrador:
   * http://127.0.0.1:8000/primaryapp/
   * http://127.0.0.1:8000/admin/
3. En la ventana principal puedes ver las emociones registradas, y el proposito del sistema, así como un menu en la parte superior izquierda para acceder a las diferentes ventanas:
   * Ventana "Todos los sentimientos" la primera vez no habrá ningún sentimiento registrado pero hay puedes visualizar una lista de todos los sentimientos registrados, además puedes ver los detalles del sentimiento.
   * Ventana "Analiza tu sentimiento" te permite interactuar con los modelos para predecir el sentimiento que desees dar como entrada.
5. Por otro lado si accediste a la dirección de administrador solo necesitar digitar tus credenciales que diste en la creación de tú super usuario.
   * En este modo podrás hacer una infinidad de funciones, ya que como administrador puedes hacer un CRUD completo de todas las emociones.

Es recomendable que si accedes por primera vez lo hagas como administrador para digitar algunos sentimientos por defecto en tu rol como administrador, de esta manera podras ver reflejados algunos cambios en la pagina principal de manera más sencilla, sobre todo si tu ordenador excede su límite de GPU en la ventana "Analiza tu sentimiento".


### Uso de la arquitectura Transformer

Una vez que hayas clonado el repositorio solo debes de acceder a traves de la linea de comandos a la dirección donde se encuentra el archivo "translate.py", ahora con el explodor de archivos ingresa al archivo como si fuera un notepad y donde veas variables con rutas descritas elimina de la ruta "primaryapp/", esto es porque ya no vas a acceder desde el sistema web, si no de manera directa con el archivo. Al finalizar de eliminar esa fracción de la ruta solo necesitas dirigirte a las ultimas 2 lineas de codigo y reemplazar la oración actual por una nueva, compilas el archivo con **python translate.py** y esperas el resultado.


### Uso del modelo BERT Afinado


