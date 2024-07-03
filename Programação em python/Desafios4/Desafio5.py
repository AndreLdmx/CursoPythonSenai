# DESAFIO 05

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais

# Isósceles: Dois lados iguais

# Escaleno: Todos os lados diferentes


lado1=float(input("Digite o tamanho de um dos lados: "))
lado2=float(input("Digite o tamanho de mais um lado: "))
lado3=float(input("Digite o tamanho de mais um lado: "))

if  lado1==lado2==lado3:
    tipoTriangulo="Equilátero"
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    tipoTriangulo="Isósceles"
else:
    tipoTriangulo="Escaleno"

if lado1+lado2<lado3 or lado2+lado3<lado1 or lado3+lado1<lado2:  
    print("Esses lados não podem formar um triângulo")
else:
    print(f"Esses lados podem formar um triângulo {tipoTriangulo}")

