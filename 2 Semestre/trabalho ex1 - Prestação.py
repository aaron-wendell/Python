# Aaron Wendell 23736 Engenharia de Software
def valorp(vet, prestacao, atraso):
    soma = 0
    if atraso == 0 and prestacao > 0:
        valor = prestacao
        vet.append(valor)
        print(f"Valor da prestação= R${valor:.2f}")
    elif atraso > 0 and prestacao > 0:
        valor = (prestacao*1.03) + (atraso*0.001) # 3% de multa do valor da prestação + 0,1% de atraso
        print(f"Valor da prestação= R${valor:.2f}")
        vet.append(valor)
    elif prestacao == 0:
        print('Transações concluídas')
        print('Numero de prestações:', len(vet))
        for i in range(len(vet)):
            print(f'Prestacao {i+1}: R${vet[i]}')
            soma += vet[i]
        print('Valor total das prestações pagas: R${:.2f}'.format(soma))
    
vet = []

prestacao = float(input('Digite o valor da primeira prestacao: '))
i = 1
while prestacao <= 0:
    prestacao = float(input('Valor invalido. Digite o valor da primeira prestacao: '))
while prestacao != 0:
    atraso = int(input('Digite os dias em atraso: '))
    while atraso < 0:
        atraso = int(input('Valor invalido. Digite os dias em atraso: '))
    valorp(vet, prestacao, atraso)
    i += 1
    prestacao = float(input(f'Digite o valor da {i}ª prestacao: '))
    while prestacao < 0:
        prestacao = float(input('Valor invalido. Digite o valor da prestacao: '))

valorp(vet, prestacao, atraso)
