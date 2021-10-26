# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$'))
print(f'o produto que custava R${preco}, com 5% de desconto vai custar R${preco * 0.95:.2f}')
