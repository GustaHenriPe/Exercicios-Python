import math
ang = float(input('Digite o ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do ângulo vale {:.2f}, o cosseno vale {:.2f} e a tangente vale {:.2f}'.format(sen, cos, tan))
