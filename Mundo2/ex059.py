# Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('1 - Somar \n2 - Multiplicar \n3 - Maior \n4 - Novos Números \n5 - Sair do Programa')
    opcao = int(input('Opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-' * 10)
    sleep(0.5)
print('Fim do programa. Volte sempre!')
