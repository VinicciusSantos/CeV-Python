# Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um
# programa que importe esse módulo e use algumas dessas funçóes.
def aumentar(valor, bonus):
    return valor + (valor * bonus / 100)


def diminuir(valor, onus):
    return valor - (valor * onus / 100)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2
