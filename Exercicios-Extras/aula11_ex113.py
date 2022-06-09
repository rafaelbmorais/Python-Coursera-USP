def simetrica(matriz):
    l = 0
    c = 0
    for linha in matriz:
        l += 1
        for coluna in linha:
            c += 1
    
    if (c / l) == l:
        return True
    else:
        return False    



#a = [[11, -3, 4 ], [-3, 12, 6], [4, 6, 5], [8, 11, 13]]
a = [[11, -3, 4, 8], [-3, 12, 6, 11], [4, 6, 5, 13], [8, 11, 13, 5]]
if simetrica(a):
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")