# Aaron Wendell Engenharia de Software 23736
def triangulo(base, altura):
    area = (base*altura)/2
    return area
def somapar(vet):
    soma = 0
    for i in range(5):
        if vet[i]%2 == 0:
            soma += vet[i]
    return soma
def maiormenor(vet):
    maior = -999999999
    maior2 = -999999999
    for i in range(5):
        if vet[i]>maior:
            maior = vet[i]
    for i in range(5):
        if vet[i] > maior2 and vet[i] < maior:
            maior2 = vet[i]
    print(f'O maior valor do vetor foi {maior} e o segundo maior valor foi {maior2}')
opcao = int(input('Digite a opcao escolhida:\n1. Calcular area de triangulo\n2. Soma dos valores pares de um vetor de 50 elementos\n3. Inserir 30 valores em um vetor e encontrar maior e menor valor do vetor\n'))
while opcao != 0:
    if opcao == 1:
        base = float(input('Digite o valor da base: '))
        altura = float(input('Digite a altura do triangulo: '))
        print('Area do triangulo:', triangulo(base, altura))
    if opcao == 2:
        vet = []
        soma = 0
        for i in range(5):
            vet.append(int(input('Digite os números: ')))
        print(vet)
        print('Soma dos valores pares:', somapar(vet))
    if opcao == 3:
        vet = []
        for i in range(5):
            vet.append(int(input('Digite um valor: ')))
        print(vet)
        maiormenor(vet)
    opcao = int(input('Digite a opcao escolhida:\n1. Calcular area de triangulo\n2. Soma dos valores pares de um vetor de 50 elementos\n3. Inserir 30 valores em um vetor e encontrar maior e menor valor do vetor\n'))