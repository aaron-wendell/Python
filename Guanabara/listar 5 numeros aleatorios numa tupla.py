import random
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(f'Os valores sorteados foram: {tupla}')
maior = 0
menor = 10
for i in tupla:
    if i>maior:
        maior = i
    if i<menor:
        menor = i
print('O maior valor sorteado foi {} e o menor foi {}'.format(maior, menor))