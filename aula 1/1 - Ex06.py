#Conta até 10.
'''
for numero in range(1,11,1):
    print( numero, end=' ')

'''


#ex do slide
'''
soma = 0
for voltas in range(6):
    numero = int(input(f'Informe o {voltas+1}º numero: '))

    if numero % 2 == 0:
        soma += numero

print(f'O Resultado da soma é: {soma}')

'''
media = 0
velho = 0
novo = 0

for contador in range(3):
    nome = input('\nInforme o nome: ')
    sexo = input('Informe o seu sexo: ')
    idade = int((input('Informe sua idade: ')))

    media +=idade

    if (idade>velho):
        velho = idade
        nome_velho = nome    

    if (idade < 20):
        novo +=1 
        

media = media / 3

print(f'\nA média de idade é: {media:.1f}')
print(f'A pessoa mais velha se chama {nome_velho}')
print(f'{novo} pessoas tem menos de 20 anos')
