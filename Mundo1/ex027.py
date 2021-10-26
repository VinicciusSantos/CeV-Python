# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
nome = str(input("Qual o seu nome? ")).strip()
print(f'Seu primeiro nome é: {nome[0:nome.find(" ")]}')
print(f'Seu último nome é: {nome[nome.rfind(" "):]}')
