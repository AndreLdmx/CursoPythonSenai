print("Calcule os juros da sua prestação")
valor= float(input("Qual o valor da sua divida? R$"))
taxa= int(input("Qual a taxa que você tem que pagar? ")) 
tempo= int(input("Quantos dias de atraso está a sua divida? "))
print(f"Você está devendo R${valor+(valor*(taxa/100)*tempo)}") 
input()