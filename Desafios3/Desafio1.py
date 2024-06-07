# DESAFIO 01

# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

print('Desafio você acertar o número de 0 a 5 que eu estou pensando')
answer=int(input())
import random
rAnswer= random.randint(0,5)
if answer==rAnswer:
    print("Parabéns você acertou!")
else:
    print("Perdeu o jogo")