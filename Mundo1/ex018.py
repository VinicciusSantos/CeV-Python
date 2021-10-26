# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
print(f'O seno de {ang}° é {sin(radians(ang)):.2f}')
print(f'O cosseno de {ang}° é {cos(radians(ang)):.2f}')
print(f'A tangente de {ang}° é {tan(radians(ang)):.2f}')
