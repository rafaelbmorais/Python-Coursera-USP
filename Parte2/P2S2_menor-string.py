def menor_string(lista_de_nomes):
    menor = lista_de_nomes[0]
    for i in lista_de_nomes:
        if i < menor:
            menor = i

    return menor

lista_de_nomes = ['José', 'Renato', 'Rafael', 'Fernanda', 'Carol', 'Ed', 'Bruna', 'Ana', 'A']
print(menor_string(lista_de_nomes))
