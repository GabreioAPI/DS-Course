'''
Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa da informada.
'''

numeros = []

for aux in range(10):
    numero = float(input(f'Informe o {aux+1}° numero: '))
    numeros.append(numero)
print('\n Ordem Inversa: ')
for aux in range(9,-1,-1):
    print(numeros[aux])