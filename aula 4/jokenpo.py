qtd_jogadas = 0
pontuacao_j1 = 0
pontuacao_j2 = 0

def jogadas(pular_intro):
    global qtd_jogadas, pontuacao_j1, pontuacao_j2
    if(pular_intro == False):
      if(qtd_jogadas == 0):
          print("Vamos jogar jokenpo")
      elif(qtd_jogadas < 3):
          print("\nVamos jogar mais uma rodada!")
      else:
          print("\nVamos conhecer o resultado!")


    if(qtd_jogadas < 3):
        jogador_1 = int(input("Primeiro jogador Escolha sua jogada:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))
        if(jogador_1 != 0 and jogador_1 != 1 and jogador_1 != 2):
            print("\nJogada inválida, vamos recomeçar!\n")
            jogadas(True)
        jogador_2 = int(input("Segundo jogador Escolha sua jogada:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA\n"))
        if(jogador_2 != 0 and jogador_2 != 1 and jogador_2 != 2):
            print("\nJogada inválida, vamos recomeçar!\n")
            jogadas(True)
        qtd_jogadas += 1

        #primeiro jogador jogou pedra
        if(jogador_1 == 0):
            if(jogador_2 == 0): #segundo jogador jogou pedra
                pontuacao_j1 += 1
                pontuacao_j2 += 1
                jogadas(False)
            elif(jogador_2 == 1):#segundo jogador jogou papel
                pontuacao_j2 += 1
                jogadas(False)
            elif(jogador_2 == 2):#segundo jogador jogou tesoura
                pontuacao_j1 += 1
                jogadas(False)

            #primeiro jogador jogou papel
        elif(jogador_1 == 1):
            if(jogador_2 == 1): #segundo jogador jogou papel
                pontuacao_j1 += 1
                pontuacao_j2 += 1
                jogadas(False)
            elif(jogador_2 == 0): #segundo jogador jogou pedra
                pontuacao_j1 += 1
                jogadas(False)
            elif(jogador_2 == 2):#segundo jogador jogou tesoura
                pontuacao_j2 += 1
                jogadas(False)
                
            
            #primeiro jogador jogou Tesoura
        elif(jogador_1 == 2):
            if(jogador_2 == 2): #segundo jogador jogou tesoura
                pontuacao_j1 += 1
                pontuacao_j2 += 1
                jogadas(False)
            elif(jogador_2 == 1): #segundo jogador jogou papel
                pontuacao_j1 += 1
                jogadas(False)
            elif(jogador_2 == 0): #segundo jogador jogou pedra
                pontuacao_j2 += 1
                jogadas(False)
    else:
        definir_ganhador()

def definir_ganhador():
    if(pontuacao_j1 > pontuacao_j2):
        print(f"jogador 1 foi o vencedor! Com {pontuacao_j1} pontos")
    elif(pontuacao_j1 < pontuacao_j2):
        print(f"jogador 2 foi o vencedor!  Com {pontuacao_j2} pontos")
    else:
        print("Foi um empate!")

jogadas(False)
    