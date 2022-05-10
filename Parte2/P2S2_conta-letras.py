'''
A função recebe dois parametros, 1º frase, 2º vogais ou consoantes:
Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. 
Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. 
Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.
'''

def conta_letras(frase, contar="vogais"):
    frase_min = frase.lower()
    v = ['a', 'e', 'i', 'o', 'u']
    c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    cont = 0
    if contar == "vogais":
        for letra in frase_min:
            if letra in v:
                cont += 1
    elif contar == "consoantes":
        for letra in frase_min:
            if letra in c:
                cont += 1

    return cont

print(conta_letras('programamos em python', 'consoantes'))