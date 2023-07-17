valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {c} : ')))
maior = menor = valores[0]
for num in valores:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'O maior número foi o {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i)
print(f'O menor número foi o {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i)
print('FIM')