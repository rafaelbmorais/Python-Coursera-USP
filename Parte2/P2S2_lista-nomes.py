def mais_curto(lista_de_nomes):
    aux = 10
    for i in lista_de_nomes:
        n = i.strip()
        tamanho = len(n)
        if tamanho < aux:
            aux = tamanho
            nome = n
    nome.capitalize()
    return nome

lista_de_nomes = ['Ana', 'José', 'Renato', 'Rafael', 'Fernanda', 'Carol', '    Ra   ', 'C']
print(mais_curto(lista_de_nomes))
