# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

jogador={}
listaGols=[]
jogador['nome']=str(input("Digite o nome do jogador: "))
jogador['partidas']=int(input("Digite o número de partidas que jogou: "))
for i in range(1, jogador['partidas']+1):
    gols=(int(input(f"Digite o número de gols  que você fez na partida {i}: ")))
    listaGols.append(gols)
    jogador[f'golsPartida{i}']=gols
jogador['golsCamp']=sum(listaGols)
print(f'\nJogador: {jogador["nome"]}\nPartidas jogadas: {jogador["partidas"]}',
      "\n--------------------------\n"'Estatísticas das partidas:')
for i in range(1, jogador['partidas']+1):
    print(f"\nQuantidade de gols feitos na {i}ª partida: {jogador[f'golsPartida{i}']}")
print("-"*43, 
      f"\nQuantidade total de gols feitos no campeonato: {jogador['golsCamp']}")