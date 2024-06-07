#DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

sViagem=int(input("Em quantos Km está o seu destino"))
taxViagemCurta=0,50
taxViagemLonga=0,45

if sViagem<=200:
    print(f"Sua corrida irá custar R${sViagem*taxViagemCurta}")
else:
    print(f"Sua corrida irá custar R${sViagem*taxViagemLonga}")