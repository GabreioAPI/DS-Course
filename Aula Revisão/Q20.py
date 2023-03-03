#Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.

idade =[]
cont = 0

for aux in range(10):
    idades = int(input(f"Informe a {aux+1}° idade: "))
    idade.append(idades)

    if idades>=18:
        cont = cont + 1

print(f"O total de pessoas com idade maior ou igual a 18 = {cont} pessoas")
