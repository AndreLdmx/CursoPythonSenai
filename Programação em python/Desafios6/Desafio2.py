# DESAFIO 02

# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999).
n999=int(input("Digite o número 999:\n"))
somaFinal=n999
quantidadeDeVezes=0


if n999==999:
    print("\nObrigado, desligando operação")
else:
    while n999!=999:
        n999=int(input("\nTeimoso, digite o número 999:\n"))
        somaFinal+=n999
        quantidadeDeVezes+=1
    print(f"\nPronto, foi difícil? A soma de todos os {quantidadeDeVezes} números que você digitou contra o meu comando foi: {somaFinal-999}")