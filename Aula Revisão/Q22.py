'''
Faça um programa que peça um número, e então, mostre na tela a tabuada desse número.
'''
numero = int(input('Informe um número: '))

print('\n-------------------------------------------')
for aux in range(1,11,1):
    print(f'{numero} x {aux} = {numero*aux}')
print('--------------------------------------------')