# DESAFIO 03

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro Serie B de Futebol, na ordem de
# colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.

# B) Os últimos 4 colocados da tabela.

# C) Uma lista com os times em ordem alfabética.

# D) Em que posição na tabela está o time do Santos.

serieB=("América-MG","Goiás","Mirassol","Avaí","Santos","Sport Recife","Ceará SC","Operário","Coritiba","Vila Nova")
print(serieB[:4])
print(serieB[6:])
print(tuple(sorted(serieB)))
print(serieB.index("Santos")+1)