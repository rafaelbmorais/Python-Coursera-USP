

def main():
    dic = Dicionario()

    dic.insere("banana", 50)
    dic.insere("abacaxi", 20)
    dic.insere("melancia", 5)
    print(dic)

    print("Eu tenho", dic.pega_valor("banana"), "bananas.")

    dic.insere("banana", dic.pega_valor("banana")+10)
    print("Agora tenho", dic.pega_valor("banana"), "bananas.")
    

class Dicionario:
    def __init__(self):
        self.chave = []
        self.valor = []

    def __str__(self):
        tam = len(self.chave)
        if tam == 0:
            return '{}'

        dic = '{%s:%s'%(str(self.chave[0]),str(self.valor[0]))
        for i in range(1, len(self.chave)):
            dic += ',%s:%s'%(str(self.chave[i]),str(self.valor[i]))
        dic += '}'
        return dic

    def procura(self, c):
        ''' (chave) -> int
            Recebe uma chave e devolve o indice da chave, caso
            exista e None caso contrario '''
        for i in range(len(self.chave)):
            if c == self.chave[i]:
                return i
        return None

    def insere(self, c, v):
        ''' (chave, valor) -> None
            altera o valor do par chave:valor para chave:v no
            dicionario caso a chave exista ou cria o par chave:v
            caso a chave ainda nao esteja no dicionario. '''
        i = self.procura(c)
        if i == None:
            self.chave.append(c)
            self.valor.append(v)
        else:
            self.valor[i] = v

    def pega_valor(self, c):
        ''' (chave) -> valor
            Retorna o valor de uma chave, caso exista, ou None '''
        for i in range(len(self.chave)):
            if c == self.chave[i]:
                return self.valor[i]
            else:
                return None
        

main()


