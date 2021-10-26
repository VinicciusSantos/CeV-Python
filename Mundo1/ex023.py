# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = str(int(input('Digite um número: ')))
print(f'Analisando o número {num}:')
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
