'''
Crie um programa que capture 5 nomes, armazene-os em uma lista ou dicionário, em seguida, exiba-os na tela.
'''

nomes = []

for aux in range(5):
    nome = input(f'Informe o {aux+1}° nome: ').strip().title()
    nomes.append(nome)

print('\nNomes armazenados = ',end = '{')
for aux in range(5):
    if aux != 4:
        print(nomes[aux], end = ',')
    else:
        print(nomes[aux], end = '}')
