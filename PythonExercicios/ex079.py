numeros = []
cont = 0
esc = 's'
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero adicionado com sucesso..')
    else:
        print('Valor duplicado! Não vou adicionar.')
    esc = input('Quer o continuar [s]SIM [n]NÃO: ').upper()
    while esc not in 'sn':
        print('Opção inválida!')
        esc = input('Quer o continuar? [s]SIM [n]NÃO: ').upper()
    if esc == 'n':
        break
print('-='*20)
print(f'Os números validados digitados foram: {sorted(numeros)}')
