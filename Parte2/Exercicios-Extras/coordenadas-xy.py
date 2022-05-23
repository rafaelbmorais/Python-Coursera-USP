'''
Dados duas coordenadas (x e y), o código imprime dentro se tiver na área
das coordenadas ou fora. (x vai de -5 a 5) e (y vai de 0 a 8).
'''

x = float(input("Digite um valor para a coordenada x: "))
y = float(input('Digite um valor para a coordenada y: '))

if (x >= -5) and (x <= 5):
    if (y >= 0) and (y <= 8):
        print('Dentro!')
    else:
        print('Fora!')
else:
    print('Fora!')
        
