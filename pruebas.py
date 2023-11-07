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
    español,frances,aleman,portugues=[ñ,á,é,í,ó,ú,ü,ý],[æ,œ,ç,à,â,é,è,ê,ë,î,ï,ô,ù,û,ü,ÿ],[ä,ö,ü,ß],[á,à,â,ã,é,ê,í,ó,ô,õ,ú]
    pass

print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))
