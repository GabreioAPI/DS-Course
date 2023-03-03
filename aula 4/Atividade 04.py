par = []
impar = []

print()
for _ in range(10):
    numero = int(input('Informe um numero qualquer: '))
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

impar.sort()
par.sort()
print(f'\nExistem {len(par)} numeros Pares. O valor máximo é {max(par)}. O valor minimo é {min(par)}.')
print(f'Conjunto dos pares = {par}')

print(f'\nExistem {len(impar)} numeros Impares. O valor máximo é {max(impar)}. O valor minimo é {min(impar)}.')
print(f'Conjunto dos impares = {impar}\n')