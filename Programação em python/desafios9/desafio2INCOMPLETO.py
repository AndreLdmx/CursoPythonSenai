from random import randint
from operator import itemgetter
from time import sleep
dados={}

for i in range(1,5):
    dados[f"Jogador {i}"]= randint(1, 6)
for k,v in dados.items():
    print(f"{k} tirou {v}\n")
    sleep(0.7)
sorted(dados.items(), key=itemgetter(1), reverse=True)
print(f"1º - {dados}\n2º - {dados}\n3º - {dados}\n4º - {dados}")