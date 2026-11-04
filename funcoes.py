def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(navio)
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    valor = tabuleiro[linha][coluna]
    if valor == 1:
        tabuleiro[linha]    [coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)

    for nome in frota:
        for navio in frota[nome]:
            for p in navio:
                linha = p[0]
                c = p[1]
                tabuleiro[linha][c] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    qtd = 0
    for nome in frota:
        for navio in frota[nome]:
            afundou = True
            for p in navio:
                if tabuleiro[p[0]][p[1]] != 'X':
                    afundou = False
            if afundou:
                qtd += 1

    return qtd

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)
    valida = True

    for p in novas:
        l = p[0]
        c = p[1]
        if l >= 10 or c >= 10:
            valida = False
        if l < 0 or c < 0:
            valida = False

    if valida == False:
        return False

    for p in novas:
        for nome in frota:
            for navio in frota[nome]:
                for posicao in navio:
                    if posicao == p:
                        return False

    return True