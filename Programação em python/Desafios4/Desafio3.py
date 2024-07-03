# DESAFIO 03

# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.

# Média abaixo de 5.0: REPROVADO

# Média entre 5.0 a 6.9: RECUPERAÇÃO

# Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media= (nota1+nota2)/2

print("A sua média é:", media)
if media>=7:
    print("Você foi aprovado!")
elif media>=5:
    print("Você está de recuperação")
else:
    print("Você foi reprovado")
input()