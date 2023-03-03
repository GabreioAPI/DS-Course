media = 0

for cont in range (1,5,1):
    nota = float(input(f'Informe a {cont}º nota:'))
    media+=nota

media = media / 4

if media == 10:
    print(f'\nAprovado com distinção',end=' -> ')

elif media >= 7:
    print(f'\nAprovado',end=' -> ')

elif media < 7:
    print(f'\nReprovado',end=' -> ')

print(f'Média = {media:.2f}\n')



