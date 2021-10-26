# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantidade de Km: '))
dias = int(input('Quantidade de dias: '))
preco = 60*dias + 0.15*km
print(f'O preço é: {preco:.2f}')
