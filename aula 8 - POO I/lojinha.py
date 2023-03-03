from produto import Produto

estoque = []

while True:
    estoque.append(
        Produto(
        input('Nome do Produto: '),
        float(input('Preço = R$')),
        input('Categoria do Produto: '),
        input('Descrição:')
        )
    )
    
    resp = input('\nDeseja Cadastrar Outro Produto: ')[0]
    if resp.lower() == 'n':
        break

print('='*30,'\n',' '*11,'Estoque:',' '*11,'\n','_'*30)
for aux in estoque:
    print(f'- Nome do Produto: {aux.nome}')
    print(f'- Preço: R${aux.preco:.2f}')
    print(f'- Categoria:{aux.categoria}')
    print('_'*30)
print('='*30)
    

    


