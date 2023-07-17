tabela = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians',
          'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos',
          'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza',
          'Botafogo', 'Ceará', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO',
          'Juventude')
print(f'Os primeiros cinco colocados são: {tabela[:5]}')
print(f'Os últimos quatro colocados são: {tabela[-4:]}')
print(f'Em ordem alfabetica os times são: {sorted(tabela)}')
print(f'O Corinthians está na posição {tabela.index("Corinthians")+1}')
