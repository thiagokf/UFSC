dados = read.csv2("dados_salarios.csv")
# 1)
sapply(dados[, c("experiencia", "emprego", "cargo", "salario_USD", "trab_remoto")], class)

# 2)
set.seed(16032006)
base1 = dados[sample(nrow(dados), 350),]

# 3)
library(dplyr)
base1$trab_remoto <- recode(base1$trab_remoto, '0' = "não", '50' = "parcial", '100' = "sim") 

# 4)
library(ggplot2)
library(scales)

base1 %>%
  count(experiencia) %>%
  mutate(pct = n / sum(n)) %>%
  
  ggplot(aes(x = experiencia, y = pct)) +
  geom_bar(stat = "identity", color = "red", fill = "black") +
  scale_y_continuous(labels = percent) + 
  labs(title = "Tipos de Experiência", x = "Experiência", y = "Porcentagem")

# Com grafico, fica visível que a experiência nivel Senior é a mais comum, e a nivel Executivo a menos aparente da amostra.

# 5)

library(ggplot2)
library(RColorBrewer)

ggplot(subset(base1, !is.na(experiencia) & !is.na(trab_remoto)), aes(x = experiencia, fill = trab_remoto)) + 
  geom_bar(position = "fill", color = "black") +  
  scale_y_continuous(labels = percent) +  
  labs(title = "Relação entre Experiência e Trabalho Remoto", x = "Experiência", y = "Porcentagem", fill = "Trabalho Remoto") +
  scale_fill_brewer(palette = "Set2") +  
  theme_minimal()

# Com o gráfico, é perceptivel que o trabalho remoto prevalece em todos os niveis de experiência, mesmo nos niveis
# que o presencial e o parcial são mais aparentes.

# 6)
library(scales)
ggplot(base1, aes(x = salario_USD)) +
  geom_density(color = "red", linewidth = 1)  +
  scale_y_continuous(labels = number_format(scale = 10000000)) +
  scale_x_continuous(labels = number_format(scale = 1)) +
  labs(title = "Gráfico de densidade de Salario", x = "Salario", y = "Amostra")

# Com o grafico, é possível perceber que a maioria da amostra ganha menos de 200000, enquanto uma menor parte ganha mais que esse valor

#7)
ggplot(base1) +
  aes(x = salario_USD, fill = trab_remoto) +
  geom_density(linewidth = 0.5) +
  scale_fill_manual(
    values = c(não = "#24245F",
               parcial = "#BA3853",
               sim = "#FCFFA4")
  ) +
  labs(title = "Gráfico de densidade de Salario", x = "Salario", y = "Amostra") +
  theme_minimal() +
  theme(legend.position = "right")

# Pelo gráfico, percebe-se que a parte parcial recebe menos que a parte
# remota, que, por sua vez, recebe menos que uma pequena parte de quem não
# trabalha remotamente.
