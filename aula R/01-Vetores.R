#Vetores (1d) - Uma estrutura de dados básicos.

#Vetores atômicos
c(100,200,300)
v <- 1:5
v
seq(2,4, by=0.4)
length(c("aa","bb","cc","dd"))
vetor <- c('cachorro', 4, "gato", 4.2, TRUE)
vetor
typeof(vetor)


#Operações com vetores
mode(vetor)
vetor[2]+vetor[4]
as.numeric(vetor[2]) + as.numeric(vetor[4])
x <- c(1,4,7,NA,12,19,15,21,20)
x
mean(x)
mean(x, na.rm = TRUE)
x[!is.na(x)]
typeof(x)
is.atomic(x)


#Indexação e subsetting
vec = c(15,30,20,73,91,41)
vec[c(1,5,6,9)]
vec[2:5]
vec[-2]
vec[vec<40]
