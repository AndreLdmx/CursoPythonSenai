# DESAFIO 05

# Desenvolva um programa que leia 
# seis números inteiros e
# mostre a soma apenas daqueles que forem pares. 
# Se o valor
# digitado for impar desconsidere-o.

soma=0
for i in range(0,6):
    n1=int(input("Digite um número inteiro: "))
    if n1%2==0:
        soma=soma+n1
print(soma)