# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em °C: '))
print(f'A temperatura em °f é: {(celsius * 9/5) + 32:.1f}°f')
