# a função retira os espaços em branco antes e depois do nome e devolve o mais curto com a letra inicial maiúscula

def menor_nome(nomes):
    aux = 10
    for i in nomes:
        n = i.strip()
        tamanho = len(n)
        if tamanho < aux:
            aux = tamanho
            nome = n
    
    n2 = nome.capitalize()
    return n2

nomes = ['Bárbara', 'JOSÉ  ', 'Bill']
print(menor_nome(nomes))
