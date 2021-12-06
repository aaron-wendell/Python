import math
angulo = float(input('Digite o angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O seno de {angulo} = {sen:.2f}º \nO cosseno de {angulo} = {cos:.2f}º \nA tangente de {angulo} = {tan:.2f}º')