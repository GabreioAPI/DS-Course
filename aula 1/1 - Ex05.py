maior = 0

for cont in range(1,4):
    num = int(input(f'informe o {cont}º número: '))

    if num > maior:
        maior = num
    
print(f'O maior valor é {maior}')