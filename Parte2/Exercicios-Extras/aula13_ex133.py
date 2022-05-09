''' lê um arquivo contendo ao menos 1 número real por linha, e para cada linha imprime a sua soma. 
    Ao final, o programa imprime também a soma total.'''

def separa(numeros, sep):
    numeros_separados = numeros.split(sep)
    return numeros_separados

nome = "aula13_ex133-numeros.txt"

with open(nome, 'r', encoding='utf-8') as arquivo:
    somatoria = 0
    for linha in arquivo:
        soma_linha = 0
        linha_sem_brancos = linha.strip()
        elementos_separados = separa(linha_sem_brancos, ',')
        for i in elementos_separados:
            soma_linha += float(i)
        print(soma_linha)
        somatoria += soma_linha
    print(somatoria)    