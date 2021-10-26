# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjacente: '))
hip = sqrt(ca**2 + co**2)
print(f'A hipotenusa vai medir {hip:.2f}')
