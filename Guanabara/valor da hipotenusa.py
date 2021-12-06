catad = float(input('Valor do cateto adjascente: '))
catop = float(input('Valor do cateto oposto: '))
hip = (catad**2 + catop**2) ** (1/2)
print('Valor da Hipotenusa = {:.2f}'.format(hip))