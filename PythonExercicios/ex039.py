from datetime import date
nasc =  int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
if idade < 18:
    alist = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(alist))
    print('Seu alistamento será em {}'.format(alist + ano))
elif idade == 18:
    print('Já está na hora de se alistar.')
else:
    alist = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(alist))
    print('Seu alistamento foi em {}'.format(ano - alist))
