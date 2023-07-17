adult = homem = mulhermenor =0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip().split()[0]
    if idade > 18:
        adult += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    while True:
        continuar = str(input('Você quer cadastras outra pessoa [S/N]? ')).upper().strip().split()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
print(f'{adult} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulhermenor} mulheres cadastradas tem menos de 20 anos.')