from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento: '))
    verif = atual - ano
    if verif >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas ainda não atingiram a maior idade, e {} já atingiram.'.format(menor, maior))
