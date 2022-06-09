#utilizando o metodo keys

frutas = {'banana': 230, 'laranja': 380, 'manga': 217, 'melancia': 58}

for item in frutas.keys():
    print('Na chave', item, 'temos a quantidade de', frutas[item], 'unidades.\n')


lista_frutas = list(frutas.keys())
print(lista_frutas, '\n')


for chave in frutas:
    print('A chave é', chave,'.\n') 
