jogador = dict()
lista = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
    print('-' * 30)
    for p in range(partidas):
        gols.append(int(input(f'Gols na partida {p+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
    print('-' * 30)
print('=' * 43)
print(f'{"Cod.":<4}{"Nome":<15}{"Gols":<18}{"Total":<5}')
print('-' * 43)
for i, e in enumerate(lista):
    print(f'{i:<4}{e["nome"]:<15}{str(e["gols"]):<18}{e["total"]:<5}')
while True:
    dados = int(input('Levantar dados de qual jogador? [cod.] '))
    if dados == 999:
        break
    if dados >= len(lista):
        print('ERRO! Não existe jogador com esse código.')
    else:
        print(f'Levantamento do jogador {lista[dados]["nome"]}')
        for i, g in enumerate(lista[dados]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 43)
print('<<< ENCERRADO >>>')
