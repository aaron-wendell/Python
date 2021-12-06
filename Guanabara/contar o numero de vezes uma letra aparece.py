letra = input('O que você está pensando? ')
letra = letra.lower()
print('A letra "a" aparece', letra.count('a'), 'vezes')
print('A primeira vez na posição', letra.find('a'),'e a ultima vez na posicao', letra.rfind('a'))