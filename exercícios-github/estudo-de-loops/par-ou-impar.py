from random import randint
tentativas = 0
print('~~' * 20)
print('PAR OU ÍMPAR'.center(40))
print('~~' * 20)
while True:
    npc = randint(0, 10)
    escolha = str(input('Escolha entre par ou ímpar [P/I]: ')).upper().strip()[0]
    val = int(input('Digite um valor entre 0 e 10: '))
    print('~~' * 20)
    if (npc + val) % 2 == 0:
        if escolha == 'P':
            print(f'O total foi de {npc + val}')
            print('Você escolheu PAR!')
            print('Você venceu!')
            tentativas += 1
            print('-' * 40)
        else:
            print(f'O total foi de {npc + val}')
            print('Você escolheu ÍMPAR!')
            print('Você perdeu!')
            break
            print('-' * 40)
    else:
        if escolha == 'I':
            print(f'O total foi de {npc + val}')
            print(f'Você escolheu ÍMPAR!')
            print('Você venceu!')
            tentativas += 1
            print('-' * 40)
        else:
            print(f'O total foi de {npc + val}')
            print(f'Você escolheu PAR!')
            print('Você perdeu!')
            break
            print('-' * 40)
print('-' * 40)
print(f'Você venceu um total de {tentativas} tentativas.')
