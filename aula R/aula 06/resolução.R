# Carregando o pacote dplyr
library(dplyr)
install.packages("dplyr")

# Criando o DataFrame
df <- data.frame(
  Produto = c("Smartphone A", "Tablet B", "Notebook C", "Smartwatch D", "Fone de Ouvido E", 
              "Câmera Digital F", "Smart TV G", "Console de Videogame H", "Monitor I", 
              "Teclado J", "Mouse K", "Headset L", "Impressora M", "Roteador N", "Caixa de Som O"),
  Preco = c(1200, 800, 2200, 300, 100, 500, 1500, 1600, 700, 80, 50, 120, 300, 120, 250),
  QuantidadeEstoque = c(50, 30, 20, 40, 100, 15, 25, 10, 40, 60, 80, 30, 25, 35, 45),
  DataEntradaEstoque = as.Date(c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", 
                                 "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
                                 "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15")),
  vendidos = c(15,20,12)
)


#1-Qual o número total de produtos diferentes na loja?
df %>%
  summarise(NumTot = n())


#2-Qual o produto mais caro na loja?
df %>%
  arrange(desc(Preco)) %>% 
  head(1)


#3-Quantos produtos têm um preço superior a R$ 1000?
df %>%
  filter(Preco>1000) %>% 
  summarise(NumProdutos = n())

#4-Qual o produto mais barato em estoque?
df %>%
  arrange((Preco)) %>% 
  head(1)

#5-Quantos produtos têm menos de 50 unidades em estoque?
df %>%
  filter(QuantidadeEstoque<50) %>% 
  summarise(NumProdutos = n())

#6-Qual é a média de preço dos produtos na loja?
df %>% 
  summarize(media = mean(df$Preco))

#7-Qual é a quantidade total de produtos em estoque?
df %>% 
  summarize(totalprod = sum(df$QuantidadeEstoque))

#8-Qual é o produto mais antigo em estoque? (Data de entrada mais antiga)
df %>%
  arrange((DataEntradaEstoque)) %>% 
  head(1)

#9-Qual é o produto mais recente em estoque? (Data de entrada mais recente)
df %>%
  arrange(desc(DataEntradaEstoque)) %>% 
  head(1)

#10-Quais produtos têm o preço entre R$ 100 e R$ 500?
df %>%
  filter(Preco>=50 & Preco<=100) %>% 
  arrange(Produto)

#11-Quais produtos estão disponíveis em estoque?
df %>%
  filter(QuantidadeEstoque>0) %>% 
  arrange(Produto)

#12-Qual é o valor total em estoque (estoque atual x preço)?
df %>%
  mutate(nova_coluna = QuantidadeEstoque * Preco)

#13-Quantos produtos foram adicionados ao estoque em janeiro de 2023?
df %>%
  filter(DataEntradaEstoque>'2023-01-01' & DataEntradaEstoque<'2023-01-30') %>% 
  arrange(Produto)

#14-Qual é o preço médio dos produtos que têm mais de 20 unidades em estoque?
df %>%
  filter(QuantidadeEstoque>20) %>% 
  summarize(media = mean(Preco))

#15-Quais são os cinco produtos mais vendidos (maior quantidade vendida)?
df %>%
  arrange((QuantidadeEstoque)) %>% 
  head(5)

#16-Qual é o produto com o menor estoque disponível?
df %>%
  arrange((QuantidadeEstoque)) %>% 
  head(1)
#17-Qual é o intervalo de datas de entrada dos produtos no estoque?
df %>%
  summarize(DataInicio = min(DataEntradaEstoque),DataFim = max(DataEntradaEstoque))

#19-Quantos produtos têm preço superior à média dos preços?
df %>%
  filter(Preco>mean(Preco)) %>% 
  summarise(NumProdutos = n())

#20-Qual é o produto mais vendido em termos de receita (preço x quantidade vendida)?

#21-Qual é a quantidade total de produtos com preço abaixo de R$ 200?
df %>%
  filter(Preco<200) %>% 
  summarise(NumProdutos = n())
#22-Qual é a média de estoque por categoria de produtos (as duas primeiras letras do nome)?

#23-Quantos produtos tiveram entrada no estoque antes do dia 10 de janeiro de 2023?
df %>%
  filter(DataEntradaEstoque>'2023-01-10') %>% 
  summarise(NumProdutos = n())

#24-Quais produtos têm estoque esgotado (quantidade em estoque igual a zero)?
df %>%
  filter(QuantidadeEstoque ==0) %>% 
  summarise(NumProdutos = n())

#25-Qual é a quantidade total de produtos em estoque por categoria?
##################################################################################

# Carregando o pacote dplyr
library(dplyr)

# Criando o DataFrame com valores vazios (NA)
df_alunos <- data.frame(
  Nome = c("João", "Maria", "Pedro", "Ana", "Lucas"),
  Idade = c(20, NA, 22, 19, 21),
  NotaProva1 = c(8.5, 7.0, NA, 6.5, 9.0),
  NotaProva2 = c(7.8, 6.5, 8.0, NA, 9.5),
  MediaNotas = c(NA, NA, NA, NA, NA)
)

#1-Qual é o número total de alunos no DataFrame?

#2-Qual é a média de idade dos alunos?

#3-Qual é a nota mais alta da prova 1?

#4-Quantos alunos têm nota na prova 2?

#5-Qual é a média das notas da prova 1?

#6-Qual é o nome do aluno mais novo?

#7-Quantos alunos têm média de notas calculada?

#8-Qual é a média das notas da prova 2?

#9-Qual é o nome do aluno com a maior média de notas?

#10-Quantos alunos têm pelo menos uma nota informada (prova 1 ou prova 2)?
