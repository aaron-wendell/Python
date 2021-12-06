# Aaron Wendell 23736 Engenharia de Software
print('Jogo da Forca')
tentativas = 5
alfabeto = list('abdcefghijklmnopqrstuvwxyzçáãéóõê')
palavra = input('Digite a palavra: ').lower()
while palavra.isalpha()!= True:
    palavra = input('Há caracter(es) invalido(s) na palavra. Digite a palavra: ')

vetor = []

for i in range(10):
    print()

while True:
    for letra in palavra:
        if letra in vetor:
            print(letra, end= ' ')
        else:
            print('_', end= ' ')
    if set(palavra).issubset(set(vetor)):
        print('\nParabens! Voce venceu o jogo da forca!')
        break
    letra = input('\nDigite uma letra: ')
    if letra not in alfabeto or letra == '':
        print('Caractere invalido. Digite uma letra: ')
        continue
    elif letra in vetor:
        print('\nLetra repetida. Tente uma letra diferente das ja usadas.')
        print('\nLetras ja usadas:', vetor)
        continue
    if letra not in palavra:
        tentativas -= 1
        print('\nLetra não existe na palavra. Tentativas restantes:', tentativas)
    if tentativas == 0:
        print('\nQue pena! Voce perdeu o jogo da forca! A resposta correta era: '+ palavra)
        break
    
    vetor.append(letra)