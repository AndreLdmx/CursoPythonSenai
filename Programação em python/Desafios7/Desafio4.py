# DESAFIO 04

# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram o números pares.

valores=int(input("Insira um número:\n"))
tupla=[valores]
for i in range(0,3):
    valores= int(input("Insira mais um número:\n"))
    tupla.append(valores)
tupla=tuple(tupla)
print(f"\nA) {tupla.count(9)}")
if 3 in tupla:
    print(f"B) {tupla.index(3)+1}")
else:
    print(f"B) Não contém")
tuplaPar=[]
for i in tupla:
    if i%2==0:
        tuplaPar.append(i)
print(f"C) {tuple(tuplaPar)}")
