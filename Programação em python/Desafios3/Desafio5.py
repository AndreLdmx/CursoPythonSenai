# DESAFIO 05

# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.


lado1=float(input())
lado2=float(input())
lado3=float(input())

# if lado1+lado2>=lado3 or lado2+lado3>=lado1 or lado3+lado1>=lado2:  
#     print("Esses lados podem formar um triângulo")
# else:
#     print("Esses lados não podem formar um triângulo")

if lado1+lado2<lado3 or lado2+lado3<lado1 or lado3+lado1<lado2:  
    print("Esses lados não podem formar um triângulo")
else:
    print("Esses lados podem formar um triângulo")
