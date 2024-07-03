# DESAFIO 02

# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla.

# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na Tupla.

import random

listaNum=[]

for i in range(0,6):
    rand=random.randint(0,50)
    listaNum.append(rand)
listaNum=tuple(sorted(listaNum))
print(f"A lista gerada foi {listaNum}\nSeu menor número é {min(listaNum)}, e seu maior número é {max(listaNum)}")
