# DESAFIO 01

# Faça um jogo, onde o computador vai “pensar” em um número
# entre 0 a 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários

import random
valorPc=random.randint(0,10)
palpiteJogador=int(input("Tente adivinhar o número de 0 a 10 que estou pensando: \n"))
numPalpites=1

while palpiteJogador != valorPc:
    if palpiteJogador>10:
        palpiteJogador=int(input("\nEssa resposta não atende aos requisitos, releia a frase e tente novamente: \n"))
    else:
        palpiteJogador=int(input("\n\nResposta ERRADA\nTente novamente:\n"))
        numPalpites+=1
print(f"\n✨🎇✨🎇✨🎇✨🎇✨🎇✨🎇✨\n\n Resposta CORRETA!!\n Você levou {numPalpites} tentativas\n\n✨🎇✨🎇✨🎇✨🎇✨🎇✨🎇✨")
input()