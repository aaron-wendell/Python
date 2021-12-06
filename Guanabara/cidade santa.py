cidade = input('Digite o nome da sua cidade: ')
print(cidade)
cidade = cidade.lower()
cidade = cidade.strip()
cidade = cidade.split()
if 'san' in cidade[0] or 'são' in cidade or 'sao' in cidade:
    print('Sua cidade é santa')
else:
    print('Sua cidade não é santa')
