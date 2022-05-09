'''lê vários números inteiros em uma mesma linha e imprime a soma.'''

def main():
    linha = "100, 35, 50, 10, 5, 3, 2, 4, 1, 123, 456"
    print(somatoria(separa(linha, ',')))


def separa(numeros, sep):
    numeros_separados = numeros.split(sep)
    return numeros_separados


def somatoria(numeros_separados):
    soma = 0
    for n in numeros_separados:
        soma += int(n)

    return soma

main()

