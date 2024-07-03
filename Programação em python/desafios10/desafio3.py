# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

def maior(n1, n2, n3):
    print(max(n1,n2,n3))
maior(int(input("Digite um valor: ")),int(input("Digite um segundo valor: ")),int(input("Digite um terceiro valor: ")))