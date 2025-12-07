jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for p in range(partidas):
    gols.append(int(input(f'   Gols na partida {p+1}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'   => Na partida {i+1}: {v} gols')