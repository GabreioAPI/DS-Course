notas = []

for _ in range(4):
    nota=float(input('Informe sua nota: '))
    notas.append(nota)

media = sum(notas)/len(notas)

if media >=7 :
    print(f'Aluno aprovado com média {media:.2f}')
elif media >=5 and media <7:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')