# DESAFIOS

# DESAFIO 06

# Crie um programa que faça o computador jogar Jokenpô com
# você:

import random

numAleatorio=random.randint(0,2)
jogadaBot=

jogadaPlayer=int(input("Faça sua jogada: \n1-Pedra \n2-Papel \n3-Tesoura"))

pedra=0
papel=1
tesoura=2

print(f"O computador jogou: {jogadaBot}")
# import random

# def jogar_jokenpo(escolha_usuario):
#     escolhas = ['pedra', 'papel', 'tesoura']
#     escolha_computador = random.choice(escolhas)
    
#     print("Você escolheu:", escolha_usuario)
#     print("O computador escolheu:", escolha_computador)
    
#     if escolha_usuario == escolha_computador:
#         print("Empate!")
#     elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
#          (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
#          (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
#         print("Você venceu!")
#     else:
#         print("Você perdeu!")

# def main():
#     print("Bem-vindo ao Jokenpô!")
#     print("Escolha uma opção: pedra, papel ou tesoura.")
#     escolha_usuario = input("Sua escolha: ").lower()
    
#     if escolha_usuario in ['pedra', 'papel', 'tesoura']:
#         jogar_jokenpo(escolha_usuario)
#     else:
#         print("Escolha inválida. Tente novamente!")

# if __name__ == "__main__":
#     main()