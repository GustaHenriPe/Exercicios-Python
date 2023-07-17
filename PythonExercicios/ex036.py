casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Quantos anos de financiamento: '))
parc = casa / (anos * 12)
print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}'.format(casa, anos), end='')
print('prestação será de {:.2f}'.format(parc))
if parc > sal * 0.3:
    print('Emprestimo negado')
else:
    print('Empréstimo pode ser CONCEDIDO.')