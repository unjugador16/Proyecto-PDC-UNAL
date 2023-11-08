import matplotlib.pyplot as plt
import stopwordsiso as stopwords
    
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

def identifica_idioma(texto, crudo): #7
    """
    Identifica el idioma en el que está escrito el texto (ingles (en), español (es), frances (fr), portugues (pt), aleman (de))
    """
    español,frances,aleman,portugues = set(["ñ","á","é","í","ó","ú","ü"]),set(["æ","œ","ç","à","â","é","è","ê","ë","î","ï","ô","ù","û","ü","ÿ"]),set(["ä","ö","ü","ß"]),set(["á","à","â","ã","é","ê","í","ó","ô","õ","ú","ç"])
    esp,fra,ale,por = 0,0,0,0
    for i in texto:
        if i in español:
            esp += texto.index(i)
        if i in frances:
            fra += texto.index(i)
        if i in aleman:
            ale += texto.index(i)
        if i in portugues:
            por += texto.index(i)
    if max(esp, fra, ale, por) == 0 or max(esp, fra, ale, por)<=((list(map(int,str(contar(texto, crudo)).split())))[0])//1000:
        return "en"
    elif max(esp, fra, ale, por) == esp:
        return "es"
    elif max(esp, fra, ale, por) == fra:
        return "fr"
    elif max(esp, fra, ale, por) == ale:
        return "de"
    elif max(esp, fra, ale, por) == por:
        return "pt"

def palabras_frec_nostop(texto,lang): #8
    """
    Muestra las 50 palabaras mas frecuentes que no corresponen a stop words
    """
    idiomas = {'de': stopwords.stopwords("de"), 'en': stopwords.stopwords("en"), 'fr': stopwords.stopwords("fr"), 'pt': stopwords.stopwords("pt"), 'es': stopwords.stopwords("es")}
    stop_w = idiomas[lang]
    cinc_pal_stop = []
    frec_pal_inv = repetidos(texto)
    cont = 50
    while cont > 0 and len(frec_pal_inv) > 0:
        for i in frec_pal_inv[max(frec_pal_inv.keys())]:
            if i not in stop_w:
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

#======================================= Empieza el Codigo =======================================#

texto = open(f'{input()}.txt', 'r', encoding='utf-8') # ingresa el nombre del libro #1
texto_leido = texto.read() 
signos = r'ºª!|@·#$~%&¬/\()=?"¿¡`^[]+*çÇ}¨´{_-:.;,' # faltan las comillas simples, pero no se le agregan porque en frances e ingles se usan

lang = identifica_idioma(texto_leido) 
texto_sin_signos = '' #sin acentos, saltos de linea o signos (teniendo en cuenta el abecedario del idioma)
texto_crudo = '' # sin acentos, espacios, saltos de linea o signos

##issue## segun el abecedario del idioma, que se dejen algunos caracteres como el ß o '

for i in texto_leido:
    if i == '\n':
        texto_sin_signos += ' ' 
    if i not in signos and i != '\n': # hay que hacer una funcion que elimine acentos
        texto_sin_signos += i
        if i != ' ':
            texto_crudo += i

##issue## replantear como se va limpiando el texto, primero se quitan saltos de linea, luego signos, luego acentos y por ultimo espacios

contado = contar(texto_sin_signos, texto_crudo) #2
print(f'Cantidad de caracteres: {contado[0]}, Cantidad de palabras: {contado[1]}')

frec_letras(texto_crudo) #3

frec_long_palabras(texto_sin_signos) #4

print(frec_palabras(texto_sin_signos)) #5

print(palabras_dist(texto_sin_signos)) #6

print(lang) #7

##issue## para las stopwords se requieren acentos

print(palabras_frec_nostop(texto_sin_signos, lang)) #8 

personajes() #9

person_principal() #10

lugares() #11

tiempo() #12

#======================================= Textos de Pruebas =======================================#

ale = "Mein Name ist Anna. Ich komme aus Österreich und lebe seit drei Jahren in Deutschland. Ich bin 15 Jahre alt und habe zwei Geschwister: Meine Schwester heißt Klara und ist 13 Jahre alt, mein Bruder Michael ist 18 Jahre alt. Wir wohnen mit unseren Eltern in einem Haus in der Nähe von München. Meine Mutter ist Köchin, mein Vater arbeitet in einer Bank. Ich lese gerne und mag Tiere: Wir haben einen Hund, zwei Katzen und im Garten einen Teich mit Goldfischen. Ich gehe auch gerne in die Schule, mein Lieblingsfach ist Mathematik. Physik und Chemie mag ich nicht so gerne. Nach der Schule gehe ich oft mit meinen Freundinnen im Park spazieren, manchmal essen wir ein Eis. Am Samstag gehen wir oft ins Kino. Am Sonntag schlafe ich lange, dann koche ich mit meiner Mutter das Mittagessen. Nach dem Essen gehen wir mit dem Hund am See spazieren. Sonntag ist mein Lieblingstag!"
fran = "Je m'appelle Jessica. Je suis une fille, je suis française et j'ai treize ans. Je vais à l'école à Nice, mais j'habite à Cagnes-Sur-Mer. J'ai deux frères. Le premier s'appelle Thomas, il a quatorze ans. Le second s'appelle Yann et il a neuf ans. Mon papa est italien et il est fleuriste. Ma mère est allemande et est avocate. Mes frères et moi parlons français, italien et allemand à la maison. Nous avons une grande maison avec un chien, un poisson et deux chats. Aujourd'hui, on est samedi, nous rendons visite à notre grand-mère. Elle a 84 ans et elle habite à Antibes. J'adore ma grand-mère, elle est très gentille. Elle fait des bons gâteaux. Lundi, je retourne à l'école. Je suis contente, je vais voir Amélie. C'est ma meilleure amie. J'aime beaucoup l'école. Mes matières préférées sont le français et le sport. J'aime beaucoup lire et je nage très bien."
port = "A minha família é constituída por mim, pelo meu pai, a minha mãe, a minha irmã, os meus avós maternos e o meu avô paterno. O meu pai chama-se Miguel. Tem 58 anos, é alto e moreno, com olhos castanhos. Conheceu a minha mãe, Maria, na faculdade, quando estavam a estudar psicologia. A minha mãe tem 55 anos e é ruiva, com olhos azuis. A minha irmã chama-se Joana e tem 25 anos. Tem o cabelo ruivo, como a minha mãe, e os olhos castanhos como o meu pai. Estudou jornalismo, mas agora trabalha numa empresa de publicidade. Os meus avós maternos, Manuel e Irene, têm ambos 80 anos. Conheceram-se numa festa na sua aldeia há 60 anos e estão juntos desde então. O meu avô paterno, Francisco, é agricultor. Apesar dos seus 85 anos, é muito alto e continua a ter muita força. “Trabalhar no campo mantém-me forte”, diz ele." 
ingl = "I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food! My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much."
espa = "Yo vivo en Granada, una ciudad pequeña que tiene monumentos muy importantes como la Alhambra. Aquí la comida es deliciosa y son famosos el gazpacho, el rebujito y el salmorejo. Mi nueva casa está en una calle ancha que tiene muchos árboles. El piso de arriba de mi casa tiene tres dormitorios y un despacho para trabajar. El piso de abajo tiene una cocina muy grande, un comedor con una mesa y seis sillas, un salón con dos sofás verdes, una televisión y cortinas. Además, tiene una pequeña terraza con piscina donde puedo tomar el sol en verano. Me gusta mucho mi casa porque puedo invitar a mis amigos a cenar o a ver el fútbol en mi televisión. Además, cerca de mi casa hay muchas tiendas para hacer la compra, como panadería, carnicería y pescadería."
