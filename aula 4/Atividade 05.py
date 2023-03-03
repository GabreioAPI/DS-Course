numeros = []

print()
for _ in range(10):
    numero = int(input('Informe um numero qualquer: '))
    numeros.append(numero)

numeros.sort()
print(f'\nLista = {numeros}')

numeros.sort(reverse=True)
print(f'Lista Inversa = {numeros}\n')