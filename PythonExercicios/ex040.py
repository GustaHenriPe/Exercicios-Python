n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2
if md >= 7:
    print('Média {}, APROVADO'.format(md))
elif md >= 5:
    print('Média {}, RECUPERAÇÃO'.format(md))
else:
    print('Média {}, REPROVADO'.format(md))
