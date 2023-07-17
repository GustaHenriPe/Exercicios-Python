vel = float(input('Digite a velocidade do seu carro: '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print('Sua multa ficou no total de {} reais '.format(multa))
else:
    print('Tudo está certo')