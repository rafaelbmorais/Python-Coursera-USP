import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma = 0
    for i in as_a:
        soma = soma + (as_a[i] - as_b[i])
    similar = abs(soma) / 6

    return similar


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    l_frases = []
    l_palavras = []

    l_sentencas = separa_sentencas(texto)
    for sent in l_sentencas:
        frases_separadas = separa_frases(sent)
        l_frases.extend(frases_separadas)
    for fra in l_frases:
        palavras_separadas = separa_palavras(fra)
        l_palavras.extend(palavras_separadas)

    tamanho_plv = 0
    cont_plv = 0
    for plv in l_palavras:
        tamanho_plv = tamanho_plv + len(l_palavras[cont_plv])
        cont_plv += 1
    wal_palavras = tamanho_plv / len(l_palavras)
    assinatura.append(wal_palavras)

    ttr_palavras = n_palavras_diferentes(l_palavras) / len(l_palavras)
    assinatura.append(ttr_palavras)

    hlr_palavras = n_palavras_unicas(l_palavras) / len(l_palavras)
    assinatura.append(hlr_palavras)

    tamanho_sentenca = 0
    cont_stnc = 0
    for stnc in l_sentencas:
        tamanho_sentenca = tamanho_sentenca + len(l_sentencas[cont_stnc])
        cont_stnc += 1
    sal_sentenca = tamanho_sentenca / len(l_sentencas)
    assinatura.append(sal_sentenca)

    sac_sentenca = len(l_frases) / len(l_sentencas)
    assinatura.append(sac_sentenca)

    tamanho_frase = 0
    cont_fr = 0
    for fr in l_frases:
        tamanho_frase = tamanho_frase + len(l_frases[cont_fr])
        cont_fr += 1
    pal_frases = tamanho_frase / len(l_frases)
    assinatura.append(pal_frases)

    return assinatura


texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
print(calcula_assinatura(texto))
