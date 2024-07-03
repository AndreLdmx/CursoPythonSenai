# Faça um programa que leia dois números e mostre qual é o
# maior e qual é o menor.

n1=int(input("Digite um número: "))
n2=int(input("Digite um segundo número: "))

if n1>n2:
    print(f"{n1} é o maior número")
else:
    print(f"{n2} é o maior número")

if n1<n2 :
    print(f"E {n1} é o menor número")
else:
    print(f"E {n2} é o menor número")
