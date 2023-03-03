nomes = []
#posicao = []

for x in range(3):
    nome = input(f"informe o nome do {x+1}° colocado: ").strip().title()
    nomes.append(nome)    
    #posicao.append(x+1)

print('================================================')
#for x in range(3):
    #print(f'{nomes[x]} -> {posicao[x]}° colocado')
     
for pos, nome in enumerate(nomes, start=1):
    print(f'{pos}º lugar - {nome}')
print('================================================') 