prod = float(input('Digite o preço do produto: '))
print(''''Qual a forma de pagamento: 
 [ 1 ] Dinheiro/Cheque 
 [ 2 ] À vista no cartão 
 [ 3 ] 2x no cartão 
 [ 4 ] 3x ou mais no cartão''')
opc = int(input('Sua opção: '))
if opc == 1:
    desc = prod - (prod * 0.1)
    print('O preço fica {}'.format(desc))
elif opc == 2:
    desc = prod - (prod * 0.05)
    print('O preço fica {}'.format(desc))
elif opc == 3:
    print('O preço fica {}'.format(prod))
elif opc == 4:
    aum = prod + (prod * 0.2)
    print('O preço fica {}'.format(aum))