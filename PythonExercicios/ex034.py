sal = float(input('Digite o seu salário: '))
if sal > 1250:
    sal = sal + (sal * 0.1)
    print('Seu salário com aumento de 10% é R${}'.format(sal))
else:
    sal = sal + (sal * 0.15)
    print('Seu salário com aumento de 15% é R${}'.format(sal))
