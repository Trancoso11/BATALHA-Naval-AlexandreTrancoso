from funcoes import *



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


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)
    for p in novas:
        if p[0] >= 10 or p[1] >= 10:
            return False
        for nome in frota:
            for navio in frota[nome]:
                if p in navio:
                    return False
    return True


frota = {}
navios = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1]
}

for nome in navios:
    q = navios[nome][0]
    tamanho = navios[nome][1]
    contador = 0
    while contador < q:
        valido = False
        while valido == False:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "vertical"
            else:
                o = int(input("[1] Vertical [2] Horizontal >"))
                if o == 1:
                    orientacao = "vertical"
                elif o == 2:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")
        contador = contador + 1

frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]], [[4, 3], [5, 3], [6, 3]]],
    
    'contratorpedeiro': [[[1, 6], [1, 7]], [[0, 5], [1, 5]], [[3, 6], [3, 7]]],
    
    'submarino': [[[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]] }

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    l = int(input("Jogador, qual linha deseja atacar? "))
    c = int(input("Jogador, qual coluna deseja atacar? "))
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, l, c)

    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False