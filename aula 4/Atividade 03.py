numeros = []

for _ in range(10):
    numero = int(input('Informe um numero qualquer: '))
    numeros.append(numero)

print(f'\nO valor máximo é {max(numeros)}')
print(f'O valor mínimo é {min(numeros)}')