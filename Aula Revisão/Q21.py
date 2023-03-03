'''
Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:
A quantidade de pessoas com mais de 90 quilos;
A média das idades das sete pessoas; 
'''

media = 0
quantidade = 0

for aux in range(7):
    idade = int(input(f"Informe a idade da {aux+1}° pessoa: ")) 
    peso = float(input(f"Informe o peso da {aux+1}° pessoa: "))

    media = idade + media
    if peso > 90:
        quantidade = quantidade + 1

media = media / 7

print(f"A média das idades é: {media}")
print(f"A quantidade de pessoas com mais de 90 quilos é: {quantidade}")
