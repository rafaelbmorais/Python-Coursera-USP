import re


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma = 0
    x = 0
    for i in as_a:
        soma = soma + (as_a[x] - as_b[x])
        x += 1
    similar = abs(soma) / 6

    return similar

a = [4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
b = [5.507142857142857, 1.6928571428571428, 2.55, 50.81818181818181, 0.8181818181818181, 30.5]

print(compara_assinatura(a, b))


