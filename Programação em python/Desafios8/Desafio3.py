# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela

listaSorted=[]
listaNum=[]
for i in range(0,5):
    num=int(input("Digite um número: "))
    listaNum.append(num)
for i in range(0,5):
    listaSorted.append(min(listaNum))
    listaNum.remove(min(listaNum))

print(listaSorted)