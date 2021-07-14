import numpy as np
from keras_transformer import get_model, decode
from pickle import load
from keras.models import load_model
import tensorflow as tf

# Instalar dos cosas:
#       pip install keras-transformer
#       pip install tensorflow
# En dado caso de tener tensorflow previamente instalado, vamos a actualizar:
#       pip install --upgrade tensorflow

np.random.seed(0)

filename = 'primaryapp/english-spanish.pkl'

dataset = load(open(filename, 'rb'))
#print(dataset[115000, 0])
#print(dataset[115000, 1])

# Error al ejecutar el codigo en este punto
#       W tensorflow/stream_executor/platform/default/dso_loader.cc:60] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
#       2021-02-13 12:38:49.657091: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.

# El error surge porque no encuentra un archivo .ddl el cual hace uso de nuestra GPU

# Solución:
#       Descargar el archivo 'cudart64_110.dll' a parte y agregar una copia en la ruta 'C:\Windows\System32'


# CREAR "tokens"
source_tokens = []
for sentence in dataset[:,1]:
    source_tokens.append(sentence.split(' '))
#print(source_tokens[115000])

target_tokens = []
for sentence in dataset[:,0]:
    target_tokens.append(sentence.split(' '))
#print(target_tokens[115000])

# Método para agregar todas las palabras a un diccionario
def build_token_dict(token_list):
    token_dict = {
        '<PAD>' : 0,
        '<START>': 1,
        '<END>': 2
    }
    for tokens in token_list:
        for token in tokens:
            if token not in token_dict:
                token_dict[token] = len(token_dict)
    return token_dict

# Llamar al metodo que genera el diccionario para las palabras Clave, las palabras Objetivo y el inverso de las palabras Objetivo
source_token_dict = build_token_dict(source_tokens)
target_token_dict = build_token_dict(target_tokens)
target_token_dict_inv = {v:k for k, v in target_token_dict.items()}

#print(source_token_dict['fraseo'])
#print(target_token_dict['tempo'])
#print(target_token_dict_inv[13468])

# Agregar <START>, <END>,  y <PAD> a cada frase del set de entrenamiento
#Primero, segun el tamaño de cada oración vamor a agregar su respectivo START y END
encoder_tokens = [['<START>'] + tokens + ['<END>'] for tokens in source_tokens]
decoder_tokens = [['<START>'] + tokens + ['<END>'] for tokens in target_tokens]
output_tokens = [tokens + ['<END>'] for tokens in target_tokens]

# Segundo, debemos conocer la oración más larga de cada arreglo, de esta manera podemos rellenar los campos vacios
source_max_len = max(map(len, encoder_tokens))
target_max_len = max(map(len, decoder_tokens))

# Tercero, solo resta rellenar con la etiqueta <PAD> todo los campos que falten para obtener arreglos de la misma longitud
encoder_tokens = [tokens + ['<PAD>'] * (source_max_len - len(tokens)) for tokens in encoder_tokens]
decoder_tokens = [tokens + ['<PAD>'] * (target_max_len - len(tokens)) for tokens in decoder_tokens]
output_tokens = [tokens + ['<PAD>'] * (target_max_len - len(tokens)) for tokens in output_tokens]

#print(encoder_tokens[115000])
#print(decoder_tokens[115000])
#print(output_tokens[115000])

# Una vez asignados los valores correspondientes a cada arreglo de la matriz, necesitamos volver esos valores de tipo String
# a valores de tipo Entero, para eso haremos uso de nuestro diccionario:
# Creamos varibles las cuales guardaran un arreglo con el valor asignado para cada palabra y etiqueta
encoder_input = [list(map(lambda x: source_token_dict[x], tokens)) for tokens in encoder_tokens]
decoder_input = [list(map(lambda x: target_token_dict[x], tokens)) for tokens in decoder_tokens]
output_decoded = [list(map(lambda x: target_token_dict[x], tokens)) for tokens in output_tokens]

#print(encoder_input[115000])
#print(decoder_input[115000])
#print(output_decoded[115000])

# CREAR RED TRANFORMER de la libreria "from keras_transformer import get_model"
model = get_model(
    token_num = max(len(source_token_dict), len(target_token_dict)),
    embed_dim = 32,
    encoder_num = 2,
    decoder_num = 2,
    head_num = 4,
    hidden_dim = 128,
    dropout_rate = 0.05,
    use_same_embed = False,
)

model.compile('adam', 'sparse_categorical_crossentropy')
model.summary()

# ENTRENAMIENTO
# El modelo ya esta entrnado solo vamos a cargar el modelo preentrenado.
filename = 'primaryapp/TranslateModel.h5'
model.load_weights(filename)

# FUNCIÓN PARA HACER LA TRANSACCIÓN DE TRADUCIR UNA PALABRA
def translate(sentence):
    sentence_tokens = [tokens + ['<END>', '<PAD>'] for tokens in [sentence.split(' ')]]
    tr_input = [list(map(lambda x: source_token_dict[x], tokens)) for tokens in sentence_tokens][0]
    decoded = decode(
        model,
        tr_input,
        start_token = target_token_dict['<START>'],
        end_token = target_token_dict['<END>'],
        pad_token = target_token_dict['<PAD>']
    )

    #print('Frase original: {}'.format(sentence))
    #print('Frase traducida: {}'.format(' '.join(map(lambda x: target_token_dict_inv[x], decoded[1:-1]))))
    answer = ' '.join(map(lambda x: target_token_dict_inv[x], decoded[1:-1]))
    return str(answer)

traduccion = translate('escribe aquí tu oración en minusculas y sin acentos')
print(traduccion)