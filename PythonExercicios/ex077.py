palavras = ('Abacate', 'Abacaxi', 'Abobrinha', 'Alface',
            'Alho', 'Banana', 'Batata', 'Cebola',
            'Cenoura', 'Chuchu', 'Couve', 'Goiaba')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')
