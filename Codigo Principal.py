nombre = input()
texto = open(f'{nombre}.txt', 'r') # se carga el archivo de texto

for i in texto:
    print(i,len(i), sep='')
