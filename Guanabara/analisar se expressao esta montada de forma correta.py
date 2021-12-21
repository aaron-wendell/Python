exp = str(input('Digite a expressão desejada: '))
vet = []
for i in exp:
    if i == '(':
        vet.append('(')
    elif i == ')':
        if len(vet) > 0:
            vet.pop()
        else:
            vet.append(')')
            break
if len(vet) == 0:
    print('\033[32mSua expressao esta valida\033[m')
else:
    print('\033[31mSua expressao esta invalida\033[m')