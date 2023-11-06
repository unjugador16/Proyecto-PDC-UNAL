import matplotlib.pyplot as plt

texto = open(f'{input()}.txt', 'r', encoding='utf-8') # ingresa el nombre del libro y carga el archivo de texto para guardarlo en una lista 
texto_leido = texto.read()
caracteres = r"ºª!|@·#$~%&¬/\()=?'¿¡`^[]+*çÇ}¨´{_-:.;,"
caracteres += '"' # como no pude poner las dobles comillas en el pimer string porque lo definí con comillas dobles, las sumo acá

texto_sin_caracteres = ''
texto_crudo = ''

for i in texto_leido:
    if i == '\n':
        texto_sin_caracteres += ' '
    if i not in caracteres and i != '\n':
        texto_sin_caracteres += i
        if i != ' ':
            texto_crudo += i  # el crudo es el texto sin espacios ni saltos de linea ni signos, por lo que la cantidad de caracteres es la longitud

def contar(texto, crudo):
    """
    Devuelve la cantidad de caracteres y palabras en el texto de la forma [caracteres, palabras]
    """
    return len(crudo), len(texto.split())

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

def frec_palabras(texto):
    """
    Calcula la frecuencia de cada palabra y muestra las 100 mas repetidas
    """
    cien_pal , cont = [] , 100
    frec_pal_inv = repetidos(texto)
    while cont > 0 and len(frec_pal_inv) > 0:
        cien_pal.extend(frec_pal_inv[max(frec_pal_inv)]) # se agrega a una lista las 10 palabras mas repetidaas
        cont -= len(frec_pal_inv[max(frec_pal_inv)])
        del frec_pal_inv[max(frec_pal_inv)]
    return cien_pal

def palabras_dist(texto):
    """
    Retorna la cantidad de palabras no repetidas que hay en el texto
    """
    frec_pal_inv = repetidos(texto)
    return len(frec_pal_inv[1])
    

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

contado = contar(texto_sin_caracteres, texto_crudo) 
print(f'Cantidad de caracteres: {contado[0]}, Cantidad de palabras: {contado[1]}')

frecuencia(texto_crudo)

frec_long_palabras(texto_sin_caracteres)

print(frec_palabras(texto_sin_caracteres))

print(palabras_dist(texto_sin_caracteres))