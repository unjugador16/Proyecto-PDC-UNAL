def normalize(s):
    rem = {
        "a": "áäàâã",
        "e": "éëèê",
        "i": "íïìî",
        "o": "óöòôõ",
        "u": "úüùô",
        "n": "ñ",
        "y": "ýÿ"
    }
    for a, b in rem:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

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

def personas_y_lugares(texto_sin_saltos):
    pers,luga,texto_procesado={},[],nlp(texto_sin_saltos)
    for ent in texto_procesado.ents:
        if ent.label_=="LOC":
            luga.append(ent.text)
        elif ent.label_=="PERSON":
            pers[ent.text]=pers.get(ent.text,0)+1
        return pers,luga

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
