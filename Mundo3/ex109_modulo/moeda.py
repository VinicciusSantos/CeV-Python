# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um paràmetro a mais, informando se o valor retornado por
# elas vai ou não ser formatado pela função moeda(), desenvolvida na aula 108.
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus, view=False):
    return moeda(valor + (valor * bonus / 100)) if view else valor + (valor * bonus / 100)


def diminuir(valor, onus, view=False):
    return moeda(valor - (valor * onus / 100)) if view else valor - (valor * onus / 100)


def dobro(valor, view=False):
    return moeda(valor * 2) if view else valor * 2


def metade(valor, view=False):
    return moeda(valor / 2) if view else valor / 2
