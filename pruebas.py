def crudificar_texto(texto):
    texto_crudo=""
    signos = r'ºª!|@·•#$£€~%&¬/\()=?"¿¡`^[]+*}¨´{_-:—.;,‘“”❝❞™®©' # faltan las comillas simples, pero no se le agregan porque en frances e ingles se usan, y las dos lineas — son diferentes, entonces no las quiten pls
    acentos = {'á','ä','à','â','ã','é','ë','è','ê','í','ï','ì','î','ó','ö','ò','ô','õ','ú','ü','ù','û','ý','ÿ'}
    correccion = {
    'a': {'á','ä','à','â','ã'},
    'e': {'é','ë','è','ê'},
    "i": {'í','ï','ì','î'},
    "o": {'ó','ö','ò','ô','õ'},
    "u": {'ú','ü','ù','û'},
    "y": {'ý','ÿ'}
    }
    for i in texto:
    if i == "’":
        i = "'"
    if i not in signos and i != "'" and i != '\n' and i != ' ':
        if i in acentos:
            for j in correccion:
                if i in correccion[j]:
                    texto_crudo += j.lower()
        else:
            texto_crudo += i.lower()
    return texto_crudo

def identificar_abecedario(a):
    español,frances,aleman,portugues,esp,fra,ale,por=set(["ñ","á","é","í","ó","ú","ü"]),set(["æ","œ","ç","à","â","é","è","ê","ë","î","ï","ô","ù","û","ü","ÿ"]),set(["ä","ö","ü","ß"]),set(["á","à","â","ã","é","ê","í","ó","ô","õ","ú","ç"]),0,0,0,0
    for i in a:
        if i in español:
            esp+=a.get(i)
        if i in frances:
            fra+=a.get(i)
        if i in aleman:
            ale+=a.get(i)
        if i in portugues:
            por+=a.get(i)
    if max(esp,fra,ale,por)==0:
        return "ingles"
    elif max(esp,fra,ale,por)==esp:
        return "español"
    elif max(esp,fra,ale,por)==fra:
        return "frances"
    elif max(esp,fra,ale,por)==ale:
        return "aleman"
    elif max(esp,fra,ale,por)==por:
        return "portugues"

def personas_y_lugares(texto_sin_saltos,lenguaje):
    if lenguaje=="es":
        texto_procesado=nlpes(texto_sin_saltos)
    elif lenguaje=="fr":
        texto_procesado=nlpfr(texto_sin_saltos)
    elif lenguaje=="de":
        texto_procesado=nlpde(texto_sin_saltos)
    elif lenguaje=="pt":
        texto_procesado=nlppo(texto_sin_saltos)
    else:
        texto_procesado=nlpen(texto_sin_saltos)
    pers,luga={},[]
    for ent in texto_procesado.ents:
        if ent.label_=="LOC" and str(ent.text).istitle() and len(str(ent.text))>2:
            luga.append(ent.text)
        elif ent.label_=="PERSON" and str(ent.text).istitle() and len(str(ent.text))>2:
            pers[ent.text]=pers.get(ent.text,0)+1
        return pers,luga

def personajes(

def personajes_principales(pers,longitud_lista_palabras):
    inv,pers_prin={},[]
    for llave, valor in pers.items():
        lista = inv.get(valor, [])
        lista.append(llave)
        inv[valor] = lista
    for i in inv:
        if i>longitud_lista_palabras//450:
            for j in inv.get(i):
                pers_prin.append(j)
    return pers_prin

print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))
