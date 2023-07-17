s = c = 0
while True:
    n = int(input('Digite um número [999 PARA]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'No total foram digitados {c} números e a soma deles vale {s}')
