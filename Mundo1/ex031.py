# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Digite a distância: '))
if km < 200:
    print(f'Você pagará R${0.5 * km:.2f}')
else:
    print(f'Você pagará R${0.45 * km:.2f}')
