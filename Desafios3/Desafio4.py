# DESAFIO 04

# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.

n1=int(input("Digite um número: "))
n2=int(input("Digite um segundo número: "))
n3=int(input("Digite um terceiro número: "))

if n1>n2 and n1>n3:
    print(f"{n1} é o maior número")
elif n2>n1 and n2>n3:
    print(f"{n2} é o maior número")
else:
    print(f"{n3} é o maior número")
    
if n1<n2 and n1<n3:
    print(f"E {n1} é o menor número")
elif n2<n1 and n2>n3:
    print(f"E {n2} é o menor número")
else:
    print(f"E {n3} é o menor número")