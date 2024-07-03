# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostra-lo por extenso.
import time 

extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
numeral=int(input("Digite um número de 0 a 10:\n\n"))
time.sleep(0.2)
print(f"\n{extenso[numeral]}")
