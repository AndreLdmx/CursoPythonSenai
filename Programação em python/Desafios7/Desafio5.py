# DESAFIO 05

# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.
impressão=0
print("____________________________________")
produtos=("|Camiseta lisa          | R$60,00  |", "|Camiseta manga longa   | R$70,00  |", "|Blusa                  | R$200,00 |", "|Calça                  | R$150,00 |")
print("|Produtos               | Preço(R$)|")
print("|-----------------------|----------|")
while impressão!=len(produtos):
    print(produtos[impressão])
    impressão+=1
    print("|-----------------------|----------|")