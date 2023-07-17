peso = float(input('Digite seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso / alt ** 2
if imc < 18.5:
    print('O seu IMC é {:.2f}'.format(imc))
    print('Abaixo do peso')
elif imc <= 25:
    print('O seu IMC é {:.2f}'.format(imc))
    print('Peso ideal')
elif imc <= 30:
    print('O seu IMC é {:.2f}'.format(imc))
    print('Sobrepeso')
elif imc <= 40:
    print('O seu IMC é {:.2f}'.format(imc))
    print('Obesidade')
else:
    print('O seu IMC é {:.2f}'.format(imc))
    print('Obesidade mórbida')