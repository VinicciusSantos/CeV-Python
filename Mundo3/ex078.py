# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

lnum = []
maior = menor = 0
for c in range(5):
    lnum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lnum[c]
    else:
        if lnum[c] > maior:
            maior = lnum[c]
        if lnum[c] < menor:
            menor = lnum[c]

print('=-' * 30)
print(f'Você digitou os valores {lnum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(lnum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lnum):
    if v == menor:
        print(f'{i}... ', end='')
