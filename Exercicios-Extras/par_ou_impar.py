#devolve a quantidade de numeros pares e impares.

numeros = [6, -2, 7, 0, -5, 8, 4, 80, 31, 128, 535]
cont_pares = 0
cont_impares = 0
for n in numeros:
    if (n != 0) and ((n % 2) == 0):
        cont_pares += 1
    elif (n !=0):
        cont_impares += 1

print('A quantidade de números pares é:', cont_pares)
print('A quantidade de números ímpares é:', cont_impares)
    
