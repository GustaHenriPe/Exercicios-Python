dias = float(input('Digite por quantos dias ele foi alugado: '))
km = float(input('Digite quantos quilometros foram rodados: '))
preço = dias * 60 + km * 0.15
print('O valor total do aluguel é de R${}'.format(preço))