# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário
# formatado.

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, bonus=0):
    return moeda(valor + (valor * bonus / 100))


def diminuir(valor=0, onus=0):
    return moeda(valor - (valor * onus / 100))


def dobro(valor=0):
    return moeda(valor * 2)


def metade(valor=0):
    return moeda(valor / 2)
