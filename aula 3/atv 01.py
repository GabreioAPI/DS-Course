inicio = int(input('Informe o inicio: '))
parada = int(input('Informe a parada: '))
passo = int(input('Informe o passo: '))

if inicio>parada and passo>0:
    passo *= -1
elif inicio<parada and passo<0:
    passo*= -1

print('(',end ='')
for aux in range(inicio,parada,passo):
    print(aux,end = ' ')
print(')')
