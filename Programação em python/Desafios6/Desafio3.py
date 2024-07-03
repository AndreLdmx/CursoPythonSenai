# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

#***INCOMPLETO***

num=int(input("\nDigite um número:\n"))
fim=str(input("\nDeseja continuar digitando números? (s/n)\n"))
mediaI=1
mediaF=num

while fim=="s":
    num=int(input("\nDigite um número:\n"))
    mediaI+=1
    mediaF+=num
    fim=str(input("\nDeseja continuar digitando números? (s/n)\n"))

print(f"\nA média entre todos os valores foi: {mediaF/mediaI}\nO menor valor lido foi: \nE o maior foi:")