# DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai
# pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

valCasa=float(input('Digite o valor da sua casa: '))
salario=float(input('Digite o seu salário: '))
anos=int(input('Em quantos anos você vai pagar: '))
prestacao= valCasa/(12*anos)
if prestacao>salario*(30/100): 
    print("EMPRÉSTIMO NEGADO \nVocê não pode pagar por esse empréstimo")
else:
    print(f"A prestação mensal sairá R${prestacao}")