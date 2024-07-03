# DESAFIO 04

# Refaça o DESAFIO 09, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

n1=int(input("Digite um numero: "))
fimTabuada=int(input("Digite o limíte da tabuada: "))
operacao=input("Digite uma operação\n+ = Adição\n- = Subtração\nx = Multiplicação\n: = Divisão\n")
if operacao=="+":
    for i in range(1,11):
        resultado=n1+i
        print(f"{n1}+{i} = {resultado}")
if operacao=="-":
    for i in range(1,11):
        resultado=n1-i
        print(f"{n1}-{i} = {resultado}")
if operacao=="x":
    for i in range(1,11):
        resultado=n1*i
        print(f"{n1}x{i} = {resultado}")
if operacao==":":
    for i in range(1,11):
        resultado=n1/i
        print(f"{n1}:{i} = {resultado}")
input()