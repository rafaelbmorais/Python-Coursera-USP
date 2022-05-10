# a função devolve a menor string

def primeiro_lex(lista_de_nomes):

    nome = lista_de_nomes[0]

    for i in lista_de_nomes:
        if i < nome:
            nome = i

    return nome


lista_de_nomes = ['AAAAAA', 'b']
print(primeiro_lex(lista_de_nomes))
