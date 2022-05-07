'''a função corta a string recebida de acordo com o separador recebido 
   e retorna uma lista de letras, inclusive espaços em branco'''

def separa(texto, sep):
    letras = texto.split(sep)
    return letras

print(separa(",1,,2,3,", ','))         