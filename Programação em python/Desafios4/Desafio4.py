# DESAFIO 04

# A confederação Nacional de Natação precisa de uma programa
# que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade.

# Até 9 anos: MIRIM

# Até 14 anos: INFANTIL

# Até 19 anos: JUNIOR

# Até 24 anos: SÊNIOR

# Acima: MASTER

from datetime import datetime

anoNascimento=int(input('Digite seu ano de nascimento:'))
anoAtual=datetime.now().year
idade=anoAtual-anoNascimento

if idade<5:
    print("Você não pode se inscrever")
    input()
elif idade<=9:
    categoria="MIRIM"
elif idade<=14:
    categoria="INFANTIL"
elif idade<=19:
    categoria="JUNIOR"
elif idade<=24:
    categoria="SÊNIOR"
else:
    categoria="MASTER"

print(F"Você está na categoria: {categoria}")

input()