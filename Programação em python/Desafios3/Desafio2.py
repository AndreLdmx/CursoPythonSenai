# DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

carro= int(input('Velocidade do carro: '))
velLimite=80
tax=float(7)
if carro>velLimite:
    print(f"Você foi multado em R${carro*tax}")
else:
    print("Está tudo certo, pode continuar dirigindo")