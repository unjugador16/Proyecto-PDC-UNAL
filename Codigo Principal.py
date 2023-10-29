texto = list(map(str,open(f'{input()}.txt', 'r'))) # # ingresa el nombre del libro y carga el archivo de texto para guardarlo en una lista
#texto = texto[0] # como la lista es de un solo elemento que es el string 
#Tenemos que quitar la forma en que se convierten las letras con tildes o la ñ, porque se crean nuevas letras, tambien esta tomado el salto de linea y

def contar_palabras(texto):
    cont = 0
    for i in range(0, len(texto)-1):
        if texto[i] != ' ' and texto[i+1] == ' ':
            cont += 1
    if texto[-1] != ' ': cont += 1 
    return cont
def contar_linea(texto):
    cont = 0
    for i in texto:
        if i!=' ':
            cont += 1
    return [cont, contar_palabras(texto)]
def contar(texto):
    """
    Devuelve la cantidad de caracteres y palabras en el texto de la forma (caracteres, palabras)
    """
    contador_final = {'caracteres':0, 'palabras':0}
    for linea in texto:
        contador_final['caracteres'] += contar_linea(linea)[0]
        contador_final['palabras'] += contar_linea(linea)[1]
    return contador_final
print('Cantidad de caracteres: '+str(contar(texto)['caracteres']),', Cantidad de palabras: '+str(contar(texto)['palabras']))

def frecuencia(texto):
    """
    Retorna la cantidad de veces que se repite una letra, ademas de hacer un histograma del mismo
    """
    pass

def frec_long_palabras(texto):
    """
    Retorna un histograma de las longitudes de las palabras
    """
    pass

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

def person_principal(texto):
    """
    Retorna los personajes principales del texto
    """
    pass

def lugares(texto):
    """
    Identifica los lugares mencionados en el texto (solo para obras en español)
    """

def tiempo(texto):
    """
    Identifica el tiempo en el que transcurre el texto (edad contemporanea, futurista, edad media, etc...)
    """
