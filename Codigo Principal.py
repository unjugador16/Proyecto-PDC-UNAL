import matplotlib.pyplot as plt

texto = open(f'{input()}.txt', 'r', encoding='utf-8') # # ingresa el nombre del libro y carga el archivo de texto para guardarlo en una lista 
texto_leido = texto.read()

texto_crudo = ''
for i in texto_leido:
    if i == ' ' or i == '\n': # se pasa por el texto y si hay un espacio o salto de lina que lo omita
        continue
    texto_crudo += i # el cuento es el texto sin espacios ni saltos de linea, por lo que la cantidad de caracteres es la longitud

def contar(texto, crudo):
    """
    Devuelve la cantidad de caracteres y palabras en el texto de la forma [caracteres, palabras]
    """
    return len(crudo), len(texto.split())

contado = contar(texto_leido, texto_crudo) 
print(f'Cantidad de caracteres: {contado[0]}, Cantidad de palabras: {contado[1]}')

def frecuencia(crudo):
    """
    Retorna la cantidad de veces que se repite una letra, ademas de hacer un histograma del mismo
    """
    letras = {}
    for i in crudo:
        if i in letras:
            letras[i] += 1
        else:
            letras[i] = 1

    plt.bar(letras.keys(),letras.values())
    plt.show()
    
frecuencia(texto_crudo)

def frec_long_palabras(texto):
    """
    Retorna un histograma de las longitudes de las palabras
    """
    long_palabras = {}
    texto = texto.split()
    for i in texto:
        if str(len(i)) in long_palabras:
            long_palabras[str(len(i))] += 1
        else:
            long_palabras[str(len(i))] = 1
    plt.bar(long_palabras.keys(),long_palabras.values()) # problema: la palabra "¿que" la toma como 4 caracteres, la deberia tomar como de 3?
    plt.show()
    
frec_long_palabras(texto_leido)

def frec_palabras(texto):
    """
    Calcula la frecuencia de cada palabra y muestra las 100 mas repetidas
    """
    pass

def palabras_dist(texto):
    """
    Retorna la cantidad de palabras no repetidas que hay en el texto
    """
    pass

def identifica_idioma(texto):
    """
    Identifica el idioma en el que está escrito el texto (ingles, español, frances, portugues, aleman)
    """
    pass

def palabras_frec_nostop(texto):
    """
    Muestra las 50 palabaras mas frecuencias que no corresponen a stop words
    """
    pass

def personajes(texto):
    """
    Retorna los personajes de la obra junto con la cantidad que se menciona cada uno
    """
    pass

def person_principal(texto):
    """
    Retorna los personajes principales del texto
    """
    pass

def lugares(texto):
    """
    Identifica los lugares mencionados en el texto (solo para obras en español)
    """
    pass
def tiempo(texto):
    """
    Identifica el tiempo en el que transcurre el texto (edad contemporanea, futurista, edad media, etc...)
    """
    pass