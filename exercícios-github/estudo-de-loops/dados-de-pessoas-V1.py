homens = mulheres20 = pessoas18 = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    idade = int(input('Idade: '))
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres20 += 1
    if idade > 18:
        pessoas18 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
print(f'''Foi um total de:
{pessoas18} pessoas acima dos 18 anos;
{homens} homens e
{mulheres20} mulheres com menos de 20 anos.''')