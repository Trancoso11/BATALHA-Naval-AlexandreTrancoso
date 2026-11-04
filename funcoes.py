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