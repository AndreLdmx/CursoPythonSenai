# n1=int(input("Digite um numero: "))
# for i in range(0,11):
#     resultado=n1*i
#     print(f"{n1}x{i} = {resultado}")

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
