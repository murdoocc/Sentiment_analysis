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

Una vez que hayas clonado el repositorio solo debes de acceder a traves de la linea de comandos a la dirección donde se encuentra el archivo "translate.py", ahora con el explodor de archivos ingresa al archivo como si fuera un notepad y donde veas variables con rutas descritas elimina de la ruta "primaryapp/", esto es porque ya no vas a acceder desde el sistema web, si no de manera directa con el archivo. Al finalizar de eliminar esa fracción de la ruta solo necesitas dirigirte a las ultimas 2 líneas de código y reemplazar la oración actual por una nueva, compilas el archivo con **python translate.py** y espera el resultado.


### Uso del modelo BERT Afinado

Al igual que en los casos anteiores, una vez se haya clonado el repositorio debemos de acceder a la misma ruta pero con la intención de acceder al archivo "analisis_sentimientos.py", una vez dentro del archivo debemos de eliminar la misma fracción de cada una de las rutas y dirigirnos a las ultimas 2 líneas de código, **recuerda escribir tu oración en ingles** aunque tambien puedes primero hacer uso de la arquitectura transformer para traducir tu oración a ingles y pegar su resultado en está parte. Compila el archivo y espera su resultado.


## Conclusiones
El bloque de atención es la principal razón de la capacidad de precisión que tienen las redes neuronales actuales, sobre todo las enfocadas en el procesamiento del lenguaje natural, además de ser más efectivas, su funcionamiento interno nos permitió entender cual es la razón de su potencial. Un ejemplo de ello fue su implementación en la traducción de un idioma a otro, logramos reducir costos de procesamiento y en cuestión de un par de horas teníamos una red entrenada con la capacidad de traducir oraciones sencillas de español a inglés. 

BERT como un modelo que implementa el bloque de atención, gracias a su preentrenamiento en una gran cantidad de datos nos permitió de manera eficaz implementar solo una capa adicional para tener un modelo capaz de interpretar dos clases (Sentimiento positivo y sentimiento negativo), con ello observamos que no se necesita una gran cantidad de hardware para conocer acerca de las herramientas implementadas actualmente por empresas tan grandes como los dueños del propio modelo o parecidos.

La implementación de BERT con los datos utilizados fue suficiente para obtener porcentajes de precisión lo suficientemente altos como para estar casi al margen de modelos entrenados con una mayor cantidad de datos, es verdad que entre mayor sea la cantidad de datos mejor será la precisión del modelo, pero el propósito principal de este trabajo fue enseñarte lo mucho que se puede hacer gracias a un uso adecuado del hardware y software disponible tanto física como virtualmente.

El codigo pretende ser muy descriptivo con cada comentario para poder ser comprendido por quien esté interesado en no solo hacer pruebas si no también en empezar a entrar en el mundo del procesamiento del lenguaje natural atraves de estas tecnologías.

### Trabajo futuro
Elaborar un sistema que tome como base el modelo de BERT así como la arquitectura de las redes transformer para realizar un análisis de sentimientos con mayor cantidad de clases, esto no quiere decir que va a estar enfocado en predecir si el sentimiento puede ser negativo, neutral o positivo, si no que contemplando la gran cantidad de datos actual en el internet generar un set de datos con una cantidad de datos suficientes que contengan un conjunto de problemas y soluciones para con ello entrenar un modelo.

Recolectar los problemas y soluciones proporcionadas por personas que expresan su día a día a través de internet, permite suministrar a un modelo un set de datos que para su evaluación logre encontrar soluciones a nuevos problemas, con esto el modelo no solo te dirá si te sientes bien o mal, al contrario, podrá entender tu sentimiento y decirte algo útil para resolver tu problema.



###### Nota importante: Si se presenta algún error en el código es por cuestión de versiones ya que todo el tiempo tanto los modelos como las librerias van siendo actualizadas, conforme la migración a dicha actualización se pueda realizar con éxito, todo el código se estará actualizando.
