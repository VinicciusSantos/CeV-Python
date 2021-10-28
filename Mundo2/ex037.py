# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para Binário
# 2 para Octal
# 3 para Hexadecimal

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n1 - Converter para BINÁRIO \n2 - Converter para OCTAL \n3 - Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opção inválida. Tente novamente.')
