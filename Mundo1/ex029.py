# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km = float(input('Qual a velocidade do carro? '))
if km > 80:
    print(f'Você utrapassou o limite!')
    print(f'Por passar à {km}Km/h: pagará R${(km - 80) * 7:.2f}')
else:
    print(f'Tenha um bom dia.')
