# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.

def escreva(txt):
    print("-"*(len(txt)+2)) 
    print(f"\n {txt}\n")
    print("-"*(len(txt)+2))
escreva(input())