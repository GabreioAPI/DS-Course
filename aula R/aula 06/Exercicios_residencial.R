#Carregando pacotes
library(dplyr)
library(ggplot2)

#Carregando dados
dados <- read.csv('C:/Users/Thiago/Desktop/Material_R/Aula3/dataset/dataset_veiculos.csv')

#Tipo de dados
str(dados)

#Tipo de dados
summary(dados)

#1-Quais as 3 cores dos veículos mais vendidos?

cores <- dados %>% 
  group_by(cor) %>% 
  summarise(total = n()) %>% 
  arrange(desc(total)) %>% 
  head(3)

#2-De qual ano são os veículos mais vendidos?

ano <- dados %>% 
  group_by(ano) %>% 
  summarise(total = n()) %>% 
  arrange(desc(total)) %>% 
  head(1)

#3-Crie um barplot para apresentar sua resposta no item 2.

todos_anos <- dados %>% 
  group_by(ano) %>% 
  summarise(total = n())

todos_anos$ano <- as.factor(todos_anos$ano)

ggplot(todos_anos, mapping = aes(x=ano, y=total)) +
  geom_bar(stat='identity', colour='blue')+
  geom_text(aes(label=total), vjust=-1, size=3)+
  theme_bw()
  

#4-Qual o percentual de vendas de veículos com transmissão automática?

percnt <- dados %>% 
  group_by(transmissao) %>% 
  summarise(total = n()) %>% 
  mutate(percentual = round((total/sum(total)*100),2))

#5-Qual o percentual de venda de veículos por modelo?

percentual <- dados %>% 
  group_by(modelo) %>% 
  summarise(total = n()) %>% 
  mutate(percent = round((total/sum(total)*100),2))

#6-Calcule o percentual de vendas por preco de veículo e o percentual acumulado.

percent <- dados %>% 
  group_by(preco) %>% 
  summarise(total = n()) %>% 
  mutate(percent = round((total/sum(total)*100),2)) %>% 
  mutate(acumulado = cumsum(percent))

#7-Liste o total de veículos vendidos por ano e por tipo de transmissão
#(Dica: uma tabela de contingência faz isso para você com um comando).

total_vendas_ano <- table(dados$ano, dados$transmissao)
