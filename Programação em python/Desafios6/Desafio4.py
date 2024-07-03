# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

import random
import time

parImpar=str(input("Par ou impar?\n"))
parImpar=parImpar.upper()

opPc=random.randint(0,10)
opJogador=int(input("\nJogue um número de 0 a 10: "))
par=(opJogador+opPc)%2==0

if parImpar=="PAR":
    print("\nO computador ganhará com um resultado impar, você com um resultado par") 
    time.sleep(0.6)
    print(f"Você jogou {opJogador}")
    time.sleep(0.8)
    print(f"O computador jogou {opPc}")
    time.sleep(0.2)
    if par==True:
        print("Você ganhou!!")
    else:
        print("Você perdeu")
elif parImpar=="IMPAR":
    print("\nO computador ganhará com um resultado par, você com um resultado impar")
    time.sleep(0.6)
    print(f"Você jogou {opJogador}")
    time.sleep(0.8)
    print(f"O computador jogou {opPc}")
    time.sleep(0.2)
    if par==False:
        print("Você ganhou!!")
    else:
        print("Você perdeu")


while opJogador>10:
    opJogador=int(input("\n        INVÁLIDO\nJogue um número de 1 a 10: "))


