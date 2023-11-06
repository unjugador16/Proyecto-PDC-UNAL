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


print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))