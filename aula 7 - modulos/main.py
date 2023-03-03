import meus_modulos.caracteres as char
#from meus_modulos.caracteres import conta_vogais,conta_letras
#from meus_modulos.caracteres import (
    #conta_vogais,
    # conta_letras
    #)

y = "Hello World"

quantidade_vogais = char.conta_vogais(y)
quantidade_consoantes = char.conta_consoante(y)
quantidade_maiusculas = char.tem_maiusculas(y)
quantidade_minusculas = char.tem_minusculas(y)
palindromo = char.eh_palindromo(y)

print(f'({y}) tem:')
print(f'- {quantidade_vogais} vogais, {quantidade_consoantes} consoantes')
print(f'- {quantidade_maiusculas} maiusculas, {quantidade_minusculas} minusculas ')
print(f'- {palindromo}')