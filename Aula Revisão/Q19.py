
start = int(input("Informe o inicio do loop: "))
stop = int(input("Informe a parada do loop: "))
step = int(input("Informe o passo do loop: "))

print('-----------------------------------------')
for cont in range(start,stop,step):
    print(f'{cont}')
print('-----------------------------------------')