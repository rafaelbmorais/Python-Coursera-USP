'''lê uma linha com palavras separadas por vírgula, e determina o comprimento 
   da maior palavra. A linha pode conter palavras vazias.'''

def main():
    linha = ",, zebra, xuxa, inconstitucional, carro, prato, democraticamente, xicara, paralelepipido, carta, ,"
    print(comprimento(separa(linha, ',')))


def separa(texto, sep):
    letras = texto.split(sep)
    return letras


def comprimento(texto):
    palavra = ''
    for item in texto:
        if len(item) > len(palavra):
            palavra = item

    return len(palavra), palavra

main()

