'''
Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. No final imprima as consoantes.
'''
caracteres = []
cont = 0
ref = []

for aux in range(5):
    caractere = input(f'Informe o {aux+1}° caractere: ')
    caracteres.append(caractere)

    if caractere not in 'aeiou':
        cont = cont + 1
        ref.append(aux)

print(f'\nO total de consoantes foi {cont}.\nAs vogais foram desconsideradas!')
print('Caracteres: ')
for aux in range(0,len(ref),1):
    print(caracteres[ref[aux]])


