# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Largura da Parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'A área é de {area}m²')
print(f'Você precisará de {area/2}l de tinta')