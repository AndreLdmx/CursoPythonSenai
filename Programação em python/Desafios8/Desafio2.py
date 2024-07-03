# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários  valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente .

loop=1
listaNum=[]
while loop!=0:
    for i in range(0,3):
        valor=int(input("Digite um valor: "))
        if valor not in listaNum:
            listaNum.append(valor)
    loop= int(input("fechar? (0 = Sim)"))
listaNum.sort()
print(listaNum)

