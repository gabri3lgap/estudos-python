tot = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    tot += num
print(f'Foram digitados {cont} valores e a soma total é de {tot}.')