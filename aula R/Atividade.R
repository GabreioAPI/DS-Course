#Exercício 1:
#Crie um vetor chamado "v" contendo os números de 1 a 10.
  v <- c(1:10)

#Exercício 2:
#Calcule o tamanho (número de elementos) do vetor "v".
  tamanho <- length(v)
  
#Exercício 3:
#Calcule a soma de todos os elementos do vetor "v".
  soma <- sum(v)
  
#Exercício 4:
#Crie um novo vetor "v2" que seja o dobro de cada elemento do vetor "v".
  v2 <- 2*v
  
#Exercício 5:
#Crie um vetor "v3" que contenha apenas os elementos pares de "v".
  v3 <- v[v%%2 == 0]
  
#Exercício 6:
#Calcule o produto escalar entre o vetor "v" e o vetor "v2".
  produto_escalar <- sum(v*v2)
  
#Exercício 7:
#Crie uma função chamada "media_vetor" que receba um vetor como parâmetro e retorne a média de seus elementos.
  media_vetor <- function(vetor){
    return(mean(vetor))
  }
  result <- media_vetor(v)
  
#Exercício 8:
#Crie uma função chamada "maior_elemento" que receba um vetor como parâmetro e retorne o maior elemento.
  maior_elemento <- function(vetor){
    return(max(vetor))
  }
  maior <- maior_elemento(v)
  
  
#Exercício 9:
#Crie uma função chamada "ordenar_vetor" que receba um vetor como parâmetro e retorne o vetor ordenado em 
#ordem crescente.
  ordenar_vetor <- function(vetor){
    return(sort(vetor))
  }
  ordenado <- ordenar_vetor(v)

#Exercício 10:
#Crie uma função chamada "repeticoes_elemento" que receba um vetor e um elemento como parâmetros e retorne
#o número de vezes que o elemento aparece no vetor.
  repeticoes_elemento <- function(vetor,numero){
    return(sum(v == numero))
  }
  repeticoes <- repeticoes_elemento(v,6)

#Exercício 11:
#Crie uma função chamada "substituir_elemento" que receba um vetor, um elemento-alvo e um novo elemento como
#parâmetros, e substitua todas as ocorrências do elemento-alvo pelo novo elemento no vetor.
  substituir_elemento <-  function(vetor,alvo,novo_elemento){
    vetor[vetor == alvo] <-  novo_elemento
    return(vetor)
  }
  v_sub <- substituir_elemento(v,5,23)
    

#Exercício 12:
#Crie uma função chamada "concatenar_vetores" que receba dois vetores como parâmetros e retorne um novo vetor
#que seja a concatenação dos dois vetores recebidos.
  concatenar_vetores <- function(vetor1,vetor2){
    return(c(vetor1,vetor2))
  }
  vet_conc <- concatenar_vetores(v,v2)

#Exercício 13:
#Crie uma função chamada "existe_elemento" que receba um vetor e um elemento como parâmetros e retorne um valor 
#booleano indicando se o elemento existe no vetor.
  existe_elemento <- function(vetor,elemento){
    return(elemento%in%vetor)
  }
  vetor_bol = existe_elemento(v,5)
  
    
#Exercício 14:
#Crie uma função chamada "soma_vetores" que receba dois vetores como parâmetros e retorne um novo vetor que
#seja a soma dos elementos correspondentes dos dois vetores recebidos.
  somar_vetores <- function(vetor1,vetor2){
    return(vetor1+vetor2)
  }
  vet_somar <- somar_vetores(v,v2)

#Exercício 15:
#Crie uma função chamada "produto_vetores" que receba dois vetores como parâmetros e retorne um novo
#vetor que seja o produto dos elementos correspondentes dos dois vetores recebidos.
  produto_vetores <- function(vetor1,vetor2){
    return(vetor1*vetor2)
  }
  vet_prod <- produto_vetores(v,v2)
  