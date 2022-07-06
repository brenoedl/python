expr = str(input('Digite a expressão: '))
pilha = []
for sinb in expr:
    if sinb == '(':
        pilha.append('(')
    elif sinb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está certa')
else:
    print('Sua expressão está erada')
