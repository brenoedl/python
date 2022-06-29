palavras = ('aprederr', 'programar', 'linguagem', 'python','curso', 'gratis',
'estudaar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'star', 'davi')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras ,end=' ')
