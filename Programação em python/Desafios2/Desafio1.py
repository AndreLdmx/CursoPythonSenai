#DESAFIO 01

# Crie um programa que leia o nome completo de uma pessoas e mostre
nome=input("Digite seu nome: ")
# O nome com todas as letras maiúsculas
print(f'Nome maiusculo: {nome.upper()}')
# O nome com todas as letras minúsculas
print(f'Nome minusculo: {nome.lower()}')
# Quantas letras ao todo (sem considerar espaços)
semEspaco= nome.replace(" ", "")
print(f"Seu nome completo possui {len(semEspaco)} letras")
# Quantas letras tem o primeiro nome
array= nome.split()
print(f"Seu primeiro nome tem {len(array[0])} letras")