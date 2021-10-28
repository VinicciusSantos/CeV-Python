# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Você ainda não tem 18 anos. Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {atual + (18 - idade)}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}.'.format(ano))
