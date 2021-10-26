# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite uma distância em metros: "))
print(f'{m/1000}Km')
print(f'{m/100}hm')
print(f'{m/10}dam')
print(f'{m*10}dm')
print(f'{m*100}cm')
print(f'{m*1000}mm')
