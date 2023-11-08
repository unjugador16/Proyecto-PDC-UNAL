import matplotlib.pyplot as plt
from langdetect import detect
import stopwordsiso as stopwords

aleman = stopwords.stopwords("de")
ingles = stopwords.stopwords("en")
frances = stopwords.stopwords("fr")
portugues = stopwords.stopwords("pt")
español = stopwords.stopwords("es")
idiomas = {'de': aleman, 'en': ingles, 'fr': frances, 'pt': portugues, 'es': español}

texto = open(f'{input()}.txt', 'r', encoding='utf-8') # ingresa el nombre del libro #1
texto_leido = texto.read() # lo lee para trabajar con el 
signos = r"ºª!|@·#$~%&¬/\()=?'¿¡`^[]+*çÇ}¨´{_-:.;," 
signos += '"' # como no pude poner las dobles comillas en el pimer string porque lo definí con comillas dobles, las sumo acá

def identifica_idioma(texto): #7
    """
    Identifica el idioma en el que está escrito el texto (ingles (en), español (es), frances (fr), portugues (pt), aleman (de))
    """
    return detect(texto) # crear una funcion que reciba el texto e identifique el idioma que que retorne la abreviaura como string

texto_sin_signos = '' #sin acentos, saltos de linea o signos
texto_crudo = '' # sin acentos, espacios, saltos de linea o signos 

for i in texto_leido:
    if i == '\n':
        texto_sin_signos += ' ' 
    if i not in signos and i != '\n': # hay que hacer una funcion que elimine acentos
        texto_sin_signos += i 
        if i != ' ':
            texto_crudo += i  

def contar(texto, crudo): #2
    """
    Devuelve la cantidad de caracteres y palabras en el texto de la forma [caracteres, palabras]
    """
    return len(crudo), len(texto.split())

def frec_letras(crudo): #3
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

def frec_long_palabras(texto): #4
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
    plt.bar(long_palabras.keys(),long_palabras.values())
    plt.show()

def repetidos(texto): 
    frec_pal , frec_pal_inv = {} , {}
    for i in texto.split(): # se agrega la frecuencia de cada palabra a un diccionario
        if i in frec_pal:
            frec_pal[i] += 1
        else:
            frec_pal[i] = 1
    for key, value in frec_pal.items(): # se invierten las llaves y valores
        if value in frec_pal_inv:
            frec_pal_inv[value].append(key)
        else:
            frec_pal_inv[value] = [key]
    return frec_pal_inv

def frec_palabras(texto): #5
    """
    Calcula la frecuencia de cada palabra y muestra las 100 mas repetidas
    """
    cien_pal , cont = [] , 100
    frec_pal_inv = repetidos(texto)
    while cont > 0 and len(frec_pal_inv) > 0:
        cien_pal.extend(frec_pal_inv[max(frec_pal_inv)]) # se agrega a una lista las 100 palabras mas repetidas
        cont -= len(frec_pal_inv[max(frec_pal_inv)])
        del frec_pal_inv[max(frec_pal_inv)]
    return cien_pal

def palabras_dist(texto): #6
    """
    Retorna la cantidad de palabras distintas en el texto
    """
    return len(set(texto.split()))

def palabras_frec_nostop(texto): #8
    """
    Muestra las 50 palabaras mas frecuentes que no corresponen a stop words
    """
    lang = idiomas[identifica_idioma(texto)]
    cinc_pal_stop = []
    frec_pal_inv = repetidos(texto)
    cont = 50
    while cont > 0 and len(frec_pal_inv) > 0:
        for i in frec_pal_inv[max(frec_pal_inv.keys())]:
            if i not in lang:
                cinc_pal_stop.append(i)
                cont -= 1
        del frec_pal_inv[max(frec_pal_inv.keys())]
    return cinc_pal_stop

def personajes(texto): #9
    """
    Retorna los personajes de la obra junto con la cantidad que se menciona cada uno
    """
    pass

def person_principal(texto): #10
    """
    Retorna los personajes principales del texto
    """
    pass

def lugares(texto): #11
    """
    Identifica los lugares mencionados en el texto (solo para obras en español)
    """
    pass

def tiempo(texto): #12
    """
    Identifica el tiempo en el que transcurre el texto (edad contemporanea, futurista, edad media, etc...)
    """
    pass


contado = contar(texto_sin_signos, texto_crudo) 
print(f'Cantidad de caracteres: {contado[0]}, Cantidad de palabras: {contado[1]}')

print(identifica_idioma(texto_sin_signos))

frec_letras(texto_crudo)

frec_long_palabras(texto_sin_signos)

print(frec_palabras(texto_sin_signos))

print(palabras_dist(texto_sin_signos))

print(frec_palabras(texto_sin_signos))

print(palabras_frec_nostop(texto_sin_signos))