altura = float(input('Qual a altura em metros? '))
largura = float(input('Qual a largura em metros? '))
while altura<=0 or largura<=0:
    print('Valor invalido')
    altura = float(input('Qual a altura em metros? '))
    largura = float(input('Qual a largura em metro? '))
area = largura * altura
tinta = area/2
print(f'Sua parede tem dimensao {altura}x{largura} e sua area é de {area}m\nPara pintar essa parede é necessario {tinta}L de tinta')