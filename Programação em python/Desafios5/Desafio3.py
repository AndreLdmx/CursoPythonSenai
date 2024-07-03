# DESAFIO 03

# Faça um programa que 
# calcule a soma 
# entre todos os números ímpares 
# que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma=0
for i in range(3,501,3):
    if i%2!=0:
        soma=soma+i
print(f"soma={soma}")