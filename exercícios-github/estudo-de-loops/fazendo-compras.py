menorval = cont = maisdemil = tot = 0
menorprod = ' '
print('=' * 40)
print('Mercadinho Gabriel'.center(40))
print('=' * 40)
while True:
    produto = str(input('Nome do produto: ')).strip()
    val = float(input('Valor do produto: R$'))
    print('-' * 40)
    tot += val
    if cont == 0:
        menorval = val
        menorprod = produto
    if val < menorval:
        menorval = val
        menorprod = produto
    if val > 1000:
        maisdemil += 1
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-' * 40)
print(f'''O valor total gasto foi R${tot:.2f}
O produto de menor valor foi {menorprod} custando R${menorval:.2f}
Foram {maisdemil} produtos custando mais de R$1.000,00''')