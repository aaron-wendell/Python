import random
numero = random.randint(0, 10)
vet = []
suposicao = int(input('Digite um valor entre 0 e 10: '))
tentativa = 1
vet.append(suposicao)
while suposicao>10 or suposicao<0:
    suposicao = int(input('Valor invalido. Digite um valor entre 0 e 10: '))
while suposicao != numero:
    suposicao = int(input('Na verdade eu estava pensando em um valor diferente. Digite um valor entre 0 e 10: '))
    if suposicao in vet:
        print('Voce ja tentou esse numero!')
        print('Numeros ja testados ->', vet)    
    tentativa += 1
    vet.append(suposicao)
if tentativa == 1:
    print(f'Parabens! O numero escolhido era {numero} e voce acertou na primeira tentativa!')
else:
    print(f'Acertou! Parabens! O numero escolhido era {numero}, mas lhe custaram {tentativa} tentativas')
    for i in range(len(vet)):
        print('Tentativa {} = {}'.format(i+1, vet[i]))