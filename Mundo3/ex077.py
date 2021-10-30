# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.
palavras = ('Ola', 'Mundo', 'Python', 'Me Segue no GitHub', 'Guanabara', 'Curso em Video', 'Vinicius', 'Guedes', 'Computacao')
for p in palavras:
    print(f'\nEm {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
