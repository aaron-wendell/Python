nome = input('Qual seu nome completo? ').lower()
nome = nome.split()
print(nome[0].capitalize(), nome[len(nome)-1].capitalize())