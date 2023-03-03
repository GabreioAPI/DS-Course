'''
Faça um Programa que leia 20 números inteiros e armazene-os numa lista. 
Armazene os números pares na lista PAR e os números ímpares na lista ÍMPAR. Imprima as três listas.
'''
numeros =[]
par = []
impar = []

for aux in range (5):
    numero = int(input(f'Informe o {aux+1} numero: '))
    numeros.append(numero)
    if numero%2 ==0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'{" Numeros ":=^30}')
for aux in range (len(numeros)):
    print(numeros[aux])

print(f'{" Pares ":=^30}')
for aux in range (len(par)):
    print(par[aux])

print(f'{" Impares ":=^30}')
for aux in range (len(impar)):
    print(impar[aux])