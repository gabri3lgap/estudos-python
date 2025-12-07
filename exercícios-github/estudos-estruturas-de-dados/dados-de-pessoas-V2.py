pessoa = dict()
grupo = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-_' * 30)
print(f'Foram cadastradas {len(grupo)} pessoas.')
media = soma / len(grupo)
print(f'A média das idades foi de {media:5.2f} anos.')
print('As mulheres do grupo foram: ', end = '')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print('As pessoas com idade acima da média geral do grupo foram: ', end = '')
for p in grupo:
    if p['idade'] > media:
        print(f'{p["nome"]}, com {p["idade"]} anos;', end = ' ')