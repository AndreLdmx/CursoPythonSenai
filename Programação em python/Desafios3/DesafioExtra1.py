# Media escola
# Aprovado se  media maior ou igual a 7
# faltas até 10

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas= int(input("Quantos dias você faltou: "))
media= (nota1+nota2)/2

print("A sua média é:", media)
if media>=7 and faltas<=10:
    print("Você foi aprovado!")
elif media>=5:
    print("Você está de recuperação")
else:
    print("Você foi reprovado")
input()