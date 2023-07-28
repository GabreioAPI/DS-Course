#Verbo select: Serve para selecionar colunas:
base %>%
  select(digite aqui as colunas que você quiser)

#Caso não queira alguma coluna, é só digita o sinal de menos:
base %>%
  select(-digite aqui as colunas que você não quiser)

#Para mudar as ordens das colunas:
base %>%
  select(digite aqui a nova ordem)

#ou

base %>%
  select(digite aqui as primeiras colunas, depois digite everything())

#Verbo filter
#A dica é digitar distinct() para saber quais opções na coluna que temos para filtrar.

base %>%
  select(coluna que você quer filtrar) %>% distinct()​

#Após isso, vamos filtrar:
  
base %>%
  filter(coluna == valor)

#(== igual; > maior; < menor; >= maior ou igual; <= menor ou igual; != diferente; %in% filtrar diversos valores de uma vez)

#Filtrar mais do que uma variável:
base %>%
  filter(coluna1 == valor1 & coluna2 == valor2)
base %>%
  filter(coluna1 == valor1 | coluna2 == valor2)

#Para filtrar quem é valor vazio, você escreve is.na antes da variável:
base %>%
  filter(is.na(coluna))

#Para filtrar quem não é valor vazio, você escreve !is.na antes da variável:
base %>%
  filter(!is.na(coluna))

#Verbo mutate: Para criar uma nova coluna, é só digita mutate com o nome da variável:
base %>%
  mutate(nova_coluna = escolhe aqui o valor que terá a nova coluna)

#Podemos criar condicionais dentro do mutate:
Base %>%
  mutate(nova_coluna = ifelse(condição, valor_se_verdadeiro, valor_se_falso))

#Verbo arrange: Para ordenar uma coluna, é só escrever arrange com o nome da variável que você quer ordenar
base %>%
  arrange(variável)

#Por padrão, é sempre em ordem crescente (do menor para o maior).
#Caso você queira na ordem decrescente (do maior para o menor), é só escrever desc antes da variável.
base %>%
  arrange(desc(altura))

#Verbos Group_by e Summarise
#Serve para agrupar pelas variáveis que você quer (variáveis categóricas) e sumarizar (fazer alguma operação matemática com as variáveis numéricas)
base %>%
  group_by(variável_categorica) %>% summarise(variavel_numérica)

#Para tirar valor vazio, é só digitar na.rm = TRUE

