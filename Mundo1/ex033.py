# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
num = [n1, n2, n3]
num.sort()
print(f"O menor número é: {num[0]}")
print(f'O maior número é: {num[2]}')
