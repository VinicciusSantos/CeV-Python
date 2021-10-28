# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''Sua opções: \n0 - PEDRA\n1 - PAPEL\n2 - TESOURA''')
jog = int(input('Qual é a sua jogada? '))

print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!!!')

print('-=' * 12)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jog]}')
print('-=' * 12)

if pc == jog:
    print('EMPATE!')

elif pc == 0 and jog == 1 or pc == 1 and jog == 2 or pc == 2 and jog == 0:
    print('JOGADOR VENCE!')

elif pc == 0 and jog == 2 or pc == 1 and jog == 0 or pc == 2 and jog == 1: 
    print('COMPUTADOR VENCE!')

else:
    print('JOGADA INVÁLIDA!')
