# DESAFIO 01

# Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
import time

print("Os fogos serão estourados em:")
time.sleep(0.7)
for i in range(10,-1,-1):
    print(i)
    time.sleep(1)