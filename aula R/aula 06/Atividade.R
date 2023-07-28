#q1
df %>%
  summarise(NumProdutos = n())

#q2
df %>%
  arrange(desc(Preco)) %>%
  head(1)

#q3
df %>%
  filter(Preco > 1000) %>%
  summarise(NumProdutosPrecoAlto = n())

#q4
df %>%
  arrange(Preco) %>%
  head(1)

#q5
df %>%
  filter(QuantidadeEstoque < 50) %>%
  summarise(NumProdutosEstoqueBaixo = n())

#q6
df %>%
  summarise(MediaPreco = mean(Preco))

#q7
df %>%
  summarise(TotalEstoque = sum(QuantidadeEstoque))

#q8
df %>%
  arrange(DataEntradaEstoque) %>%
  head(1)

#q9
df %>%
  arrange(desc(DataEntradaEstoque)) %>%
  head(1)

#q10
df %>%
  filter(Preco >= 100 & Preco <= 500)

#q11
df %>%
  filter(QuantidadeEstoque > 0)

#q12
df %>%
  mutate(ValorEstoque = QuantidadeEstoque * Preco) %>%
  summarise(TotalEstoqueValor = sum(ValorEstoque))

#q13
df %>%
  filter(format(DataEntradaEstoque, "%Y-%m") == "2023-01") %>%
  summarise(NumProdutosJaneiro = n())

#q14
df %>%
  filter(QuantidadeEstoque > 20) %>%
  summarise(MediaPrecoEstoqueAlto = mean(Preco))

#q15
df %>%
  arrange(desc(QuantidadeEstoque)) %>%
  head(5)

#16
df %>%
  arrange(QuantidadeEstoque) %>%
  head(1)

#q17
df %>%
  summarise(DataInicio = min(DataEntradaEstoque), DataFim = max(DataEntradaEstoque))

#q18
df %>%
  filter(str_starts(Produto, "S"))

#q19
media_preco <- mean(df$Preco)
df %>%
  filter(Preco > media_preco) %>%
  summarise(NumProdutosPrecoAltoMedia = n())

#q20
df %>%
  mutate(Receita = Preco * QuantidadeEstoque) %>%
  arrange(desc(Receita)) %>%
  head(1)

#q21
df %>%
  filter(Preco < 200) %>%
  summarise(TotalProdutosPrecoBaixo = sum(QuantidadeEstoque))

#q22
df %>%
  mutate(Categoria = substr(Produto, 1, 2)) %>%
  group_by(Categoria) %>%
  summarise(MediaEstoque = mean(QuantidadeEstoque))

#q23
df %>%
  filter(DataEntradaEstoque < "2023-01-10") %>%
  summarise(NumProdutosAntes10Jan = n())

#q24
df %>%
  filter(QuantidadeEstoque == 0)

#q25
df %>%
  mutate(Categoria = substr(Produto, 1, 2)) %>%
  group_by(Categoria) %>%
  summarise(TotalEstoqueCategoria = sum(QuantidadeEstoque))

###############################################################################

#q1
df_alunos %>%
  summarise(NumAlunos = n())

#q2
df_alunos %>%
  summarise(MediaIdade = mean(Idade, na.rm = TRUE))

#q3
df_alunos %>%
  summarise(NotaMaximaProva1 = max(NotaProva1, na.rm = TRUE))

#q4
df_alunos %>%
  filter(!is.na(NotaProva2)) %>%
  summarise(NumAlunosComNotaProva2 = n())

#q5
df_alunos %>%
  summarise(MediaNotasProva1 = mean(NotaProva1, na.rm = TRUE))

#q6
df_alunos %>%
  filter(Idade == min(Idade, na.rm = TRUE)) %>%
  select(Nome)

#q7
df_alunos %>%
  filter(!is.na(MediaNotas)) %>%
  summarise(NumAlunosComMediaNotas = n())

#q8
df_alunos %>%
  summarise(MediaNotasProva2 = mean(NotaProva2, na.rm = TRUE))

#q9
df_alunos %>%
  filter(MediaNotas == max(MediaNotas, na.rm = TRUE)) %>%
  select(Nome)

#q10
df_alunos %>%
  filter(!is.na(NotaProva1) | !is.na(NotaProva2)) %>%
  summarise(NumAlunosComPeloMenosUmaNota = n())
