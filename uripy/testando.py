def computador_escolhe_jogada(n,m):
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

    

def usuario_escolhe_jogada(n,m):
    jogada = int(input('\nQuantas peças voce vai tirar?'))
    while jogada > n or jogada > m or jogada <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada = int(input('\nQuantas peças voce vai tirar?'))
    return jogada    



def partida():
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    while m < 1:
        print('O número de peças retiradas deve ser maior que 0 ou igual ao total de peças!')
        m = int(input('Limite de peças por jogada?'))
    jogada = 0
    rodada = 0
    if n%(m+1) == 0:
        print('\nVocê começa!')
        rodada = 1
        while n > 0:
            if rodada == 1:
                jogada = usuario_escolhe_jogada(n,m)
                print('\nVocê tirou', jogada,'peças')
                n = n - jogada
                print('Agora restam', n ,'peças no tabuleiro')
                rodada = rodada + 1
            else:
                jogada = computador_escolhe_jogada(n,m)
                print('\nO computador tirou',jogada,'peças')
                n = n - jogada
                print('Agora restam', n ,'peças no tabuleiro')
                rodada = 1
        if rodada == 1:
            print('Fim do jogo! O computador ganhou!\n')
            return 2
        else:
            print('Fim do jogo! Você ganhou!\n')
            return 1
    else:
        print('\nComputador começa!')
        rodada = 2
        while n > 0:
            if rodada == 2:
                jogada = computador_escolhe_jogada(n,m)
                print('\nO computador tirou', jogada,'peças')
                n = n - jogada
                print('Agora restam', n ,'peças no tabuleiro')
                rodada = 1
            else:
                jogada = usuario_escolhe_jogada(n,m)
                print('\nVocê tirou,',jogada,'peças')
                n = n - jogada
                print('\nAgora restam', n ,'peças no tabuleiro')
                rodada = 2
        
        if rodada == 1:
            print('\nFim do jogo! O computador ganhou!')
            return 2
        else:
            print('\nFim do jogo! Você ganhou!')
            return 1
        
def nim():
    print('\n      ************** SEJA BEM VINDO AO JOGO NIM ***************\n\n')
    print('1 - para jogar uma partida')
    print('2 - para jogar um campeonato')
    option = int(input('\nSua escolha:'))

    while option != 1 and option != 2:
        print('Escolha "1" ou "2"')
        option = int(input())    
    if option == 1:
        print('\n      --------- Escolheu... Partida individual ------------\n')
        partida()
    else:
        print('\n      --------- Escolheu... Campeonato --------------------\n')
        campeonato()

def campeonato():
    print('\n------------ Rodada 1 ------------\n\n')
    pontosCPU = 0
    pontosUSU = 0
    
    if partida() == 1:
        pontosUSU = pontosUSU + 1
    else:
        pontosCPU = pontosCPU + 1
    print('\n------------ Rodada 2 ------------\n\n')
    
    if partida() == 1:
        pontosUSU = pontosUSU + 1
    else:
        pontosCPU = pontosCPU + 1
    print('\n------------ Rodada 3 ------------\n\n')
    
    if partida() == 1:
        pontosUSU = pontosUSU + 1
    else:
        pontosCPU = pontosCPU + 1
    print('\n ------------ FINAL DO CAMPEONATO -------------\n\n')
    print('Placar: Você',pontosUSU,'X',pontosCPU,'Computador''\n\n')

nim()








