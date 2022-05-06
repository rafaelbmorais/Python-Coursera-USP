# a função retira os espaços em branco antes e depois do nome e devolve o mais curto com a letra inicial maiúscula

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

lista_de_nomes = ['   Ana  ', 'José    ', 'Alfredo', 'João', '     Fred', 'Carol', 'Ed' , '    Maria Julia  ', ' João Victor']
print(mais_curto(lista_de_nomes))
