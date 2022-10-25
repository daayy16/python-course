jogador_1 = 0
jogador_2 = 0
lista = [0, 1, 2]
qtd_jogadas = 0
pontuacao_j1 = 0
pontuacao_j2 = 0

def jogadas():
    global qtd_jogadas, pontuacao_j1, pontuacao_j2
    if qtd_jogadas == 0:
        print("\nVamos jogar jokenpo! ")
    else:
        print("\nVamos jogar mais uma vez! ")
    
    jogador_1 = int(input("\nPrimeiro jogador escolha sua jogada:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))
    #verifica se o jogador escolheu um valor valido
    while jogador_1 not in lista:
        jogador_1 = int(input("\nPrimeiro jogador digite um valor válido:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))

    jogador_2 = int(input("\nSegundo jogador Escolha sua jogada:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))
    #verifica se o jogador escolheu um valor valido
    while jogador_2 not in lista:
        jogador_2 = int(input("\nSegundo jogador digite um valor válido:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))
        
    qtd_jogadas += 1

        #primeiro jogador jogou pedra
    if(jogador_1 == 0):
        if(jogador_2 == 0): #segundo jogador jogou pedra
            pontuacao_j1 += 1
            pontuacao_j2 += 1
        elif(jogador_2 == 1):#segundo jogador jogou papel
            pontuacao_j2 += 1
        elif(jogador_2 == 2):#segundo jogador jogou tesoura
            pontuacao_j1 += 1
            #primeiro jogador jogou papel
    elif(jogador_1 == 1):
        if(jogador_2 == 1): #segundo jogador jogou papel
            pontuacao_j1 += 1
            pontuacao_j2 += 1
        elif(jogador_2 == 0): #segundo jogador jogou pedra
            pontuacao_j1 += 1
        elif(jogador_2 == 2):#segundo jogador jogou tesoura
            pontuacao_j2 += 1
            #primeiro jogador jogou Tesoura
    elif(jogador_1 == 2):
        if(jogador_2 == 2): #segundo jogador jogou tesoura
            pontuacao_j1 += 1
            pontuacao_j2 += 1
        elif(jogador_2 == 1): #segundo jogador jogou papel
            pontuacao_j1 += 1
        elif(jogador_2 == 0): #segundo jogador jogou pedra
            pontuacao_j2 += 1

def definir_ganhador():
    if(pontuacao_j1 > pontuacao_j2):
        print(f"jogador 1 foi o vencedor! Com {pontuacao_j1} pontos")
    elif(pontuacao_j1 < pontuacao_j2):
        print(f"jogador 2 foi o vencedor!  Com {pontuacao_j2} pontos")
    else:
        print("Foi um empate!")

while qtd_jogadas < 3:
    jogadas()

definir_ganhador()