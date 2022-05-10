
def maiusculas(frase):
    letras = ''
    for i in frase:
        if (ord(i) >= 65) and (ord(i) <= 90):
            letras += i
    return letras

print(maiusculas('PrOgRaMaMoS em python!'))