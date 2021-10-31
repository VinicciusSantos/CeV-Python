# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(). que mostre na tela algumas informações
# geradas pelas funções que já temos no módulo criado até aqui.
def resumo(valor, bonus, onus):
    print(f'Preço analisado:   {moeda(valor)}')
    print(f'Dobro do preço:    {dobro(valor)}')
    print(f'Metade do preço:   {metade(valor)}')
    print(f'{bonus}% de aumento:    {aumentar(valor, bonus)}')
    print(f'{onus}% de redução:    {diminuir(valor, onus)}')


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus):
    return moeda(valor + (valor * bonus / 100))


def diminuir(valor, onus):
    return moeda(valor - (valor * onus / 100))


def dobro(valor):
    return moeda(valor * 2)


def metade(valor):
    return moeda(valor / 2)
