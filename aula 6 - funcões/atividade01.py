def imc_calculator(dados: list,cont: int)->float:
    '''Imprime o nome e a idade de uma pessoa

        params:
            dados - uma lista com os dados do usuários
            cont - um inteiro positivo com a quantidade de IMC a serem calculados

        return:
            O valor do IMC dos usuários
    '''
    imc = []
    for contador in range (cont):
        calc = dados[contador][1]/(dados[contador][2] **2)
        imc.append(round(calc,2))
    return imc

def imc_calculator2(altura: float,peso: float)->float:
    imc = round(peso / (altura**2),2)
    return imc


#Main():
nome = []
peso = []
altura = []

print('='*70)
print(' '*22,'IMC Calculator')
print('='*70)
quantidade = int(input('\nInforme a quantidade de IMC que serão calculados: '))

for cont in range(quantidade):
    nomes = input(f'\nInforme o {cont+1}° nome: ')
    pesos = float(input(f'Informe o peso de {nomes}[Kg]: '))
    alturas = float(input(f'Informe a altura de {nomes}[M]: '))

    nome.append(nomes)
    peso.append(pesos)
    altura.append(alturas)
print()
database = list((zip(nome, peso,altura)))

imc = imc_calculator(database,quantidade)

print('-'*70)
for cont in range(quantidade):
    print(f'O IMC de {nome[cont]} = {imc[cont]}')

print('-'*70)
for dados in database:
    pessoa, massa,alt = dados
    print(f'O IMC de {pessoa} = {imc_calculator2(alt, massa)}')

print('-'*70)
    
