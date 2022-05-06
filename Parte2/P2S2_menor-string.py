# a função devolve a menor string

def menor_string(lista_de_nomes):

    nome = lista_de_nomes[0]

    for i in lista_de_nomes:
        if i < nome:
            nome = i

    return nome

lista_de_nomes = ['José', 'Ronaldo', 'Rafaela', 'João Bosco', 'Carol', 'Ed', 'Jo', 'Bu', 'Carlos']
print(menor_string(lista_de_nomes))
