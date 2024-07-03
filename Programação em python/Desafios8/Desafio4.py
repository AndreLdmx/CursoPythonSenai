# DESAFIO 04

# Crie um programa que vai ler vários números e colocar em
# uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

listaPar=[]
listaImpar=[]
valor=-1
listaNum=[]
while valor!=0:
    
    valor=int(input("Digite um valor: "))
    print("(Digite 0 para sair)")
    if valor not in listaNum and valor!=0:
        listaNum.append(valor)
        if valor%2==0 :
            listaPar.append(valor)
        else:
            listaImpar.append(valor)
listaNum.sort()
listaPar.sort()
listaImpar.sort()
print(listaNum)
print(f"Pares: {listaPar}")
print(f"Impares: {listaImpar}")