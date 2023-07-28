#Exercício 1:
#Crie uma lista chamada "lista_numeros" contendo três elementos: um vetor com
#os números de 1 a 5, um vetor com os números de 6 a 10 e um vetor com os números de 11 a 15.
lista_numeros <- list(c(1:5),c(6:10),c(11:15))
lista_numeros

#Exercício 2:
#A partir da lista "lista_numeros", acesse o segundo elemento (vetor com os números
#de 6 a 10) e calcule a média dos valores desse vetor.
media <- mean(lista_numeros[[2]])
media

#Exercício 3:
#Crie uma lista chamada "lista_alunos" contendo três elementos: um vetor de nomes
#de alunos, um vetor de suas respectivas idades e um vetor de notas (de 0 a 10) de provas.
 lista_alunos <- list(nomes = c("Gabriel","Lucas","Gui"), idades = c(23,20,19), notas = c(10,9,8))
 lista_alunos
 
#Exercício 4:
#A partir da lista "lista_alunos", obtenha o nome, idade e nota do terceiro aluno.
 response <-list(lista_alunos$nomes[3],lista_alunos$idades[3],lista_alunos$notas[3])
 response
 
#Exercício 5:
#Crie uma lista chamada "lista_paises" contendo três elementos: um vetor de nomes
#de países, um vetor de suas respectivas capitais e um vetor de idiomas falados nesses países.
 lista_paises <- list(Pais = c("Brasil","EUA","Espanha"),
                      Capital = c("Brasilia","Washington","Madrid"), 
                      Idiomas = c("Pt Br","English","Spanish")
                      )
 lista_paises
 
#Exercício 6:
#A partir da lista "lista_paises", adicione um novo país com suas informações
#(nome, capital e idioma) à lista.
 #novo_pais <- list(Pais = "Inglaterra", Capital= "Londres", Idiomas = "English")
 lista_paises <- append(Pais = "Inglaterra", Capital= "Londres", Idiomas = "English")

lista_paises
