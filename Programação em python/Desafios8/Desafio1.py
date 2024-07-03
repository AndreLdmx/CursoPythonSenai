# DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.

listaNum=[]
for i in range(0,5):
    num=int(input("Digite um número: "))
    listaNum+=[num]
listaNum.index(min(listaNum))
print(f"menor = {min(listaNum)} na posição {listaNum.index(min(listaNum))}")

print(f"maior = {max(listaNum)} na posição {listaNum.index(max(listaNum))}")
