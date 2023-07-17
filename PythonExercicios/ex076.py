lista = ('Abacate', 4.99,
         'Abacaxi', 10.0,
         'Abobrinha', 5.59,
         'Alface', 2.99,
         'Alho', 1.99,
         'Banana', 5.99,
         'Batata', 5.99,
         'beterraba', 3.49,
         'Brócolis', 5.90,
         'Cebola', 5.29,
         'Cenoura', 4.89,
         'Chuchu', 4.99,
         'Couve', 2.99,
         'Goiaba', 10.99)
print('='*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('='*30)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}',end='')
    else:
        print(f'R$ {lista[pos]:>}')
print('='*30)
