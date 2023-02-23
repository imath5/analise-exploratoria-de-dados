#Desafio:
#Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu
# que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos
# enormes para a empresa
# O que fazer para evitar isso ?
# Como saber as pessoas que têm maior
# tendência a cancelar o cartão?


#O que temos:

#Temos 1 base de dados com informações dos clientes, tanto clientes atuais
# quanto clientes que cancelaram o cartão

#Passo 1: Importar a base de dados
#Passo 2: Tratamento da base de dados
#(Excluir/Corrigir linhas e colunas vazias)
#(Ajeitar as colunas importadas)
#(Excluir colunas inúteis)
#Passo 3: Analisar a base de dados
#(Queremos descobrir os principais motivos de cancelamento do cartão)

# Passo 1: Importar a base de dados
import pandas as pd  #importar dados de uma tabela excell

tabela_clientes = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/ClientesBanco.csv", encoding="latin1")
#excluindo coluna#
tabela_clientes = tabela_clientes.drop("CLIENTNUM", axis=1) #axis=0 - LINHAS/ axis=1 - COLUNAS
display (tabela_clientes)

#Passo 2: Tratamento da base de dados
tabela_clientes = tabela_clientes.dropna() #exclui as linhas que têm itens vazios
display (tabela_clientes.info())
display (tabela_clientes.describe())

#Passo 3: Analisar a base de dados (Quero descobrir o motivo dos clientes cancelarem o cartão)

#Primeira coisa para fazer uma análise de dados é tentar olhar como que estão distribuidos os valores que você quer entender
display (tabela_clientes["Categoria"].value_counts())
display (tabela_clientes["Categoria"].value_counts(normalize=True))

#Objetivo: Analisar o 80/20 - Regra de Pareto
#Olhar todas as características dos clientes e descobrir os PRINCIPAIS MOTIVOS de cancelamento

import plotly.express as px #cria gráfico interativo
# 2 passos para criar graficos:
#Passo 1- Criar a figura, Passo 2- Exibir a figura # https://plotly.com/python/histograms/

for coluna in tabela_clientes:  #tabela_clientes em um for sempre vai percorrer as colunas / tabela_clientes.index  vai percorrer as linhas
  fig = px.histogram(tabela_clientes, x=coluna, color="Categoria")
  #Exibir figura
  fig.show()


#pouco limite e cartão blue foram os que mais cancelaram, solução = aumentar o limite do cartão blue ?
#O que conseguimos perceber analisando os gráficos? Verificar a maior diferença entre os gráficos, análise exploratória = achar algo que saltam os olhos PROCURAR O QUE ESTA EM DESTAQUE ( NO OLHO)

#Gráfico (Categoria Cartão) *SALTA OS OLHOS= 1500 dos nossos clientes totais(1600) são CATEGORIA BLUE.
#Gráfico (Inatividade) *SALTA OS OLHOS = Quando mais você aumenta a
#Gráfico (Limite Consumido) *SALTA OS OLHOS = Não usam muito o cartão cancela
#Gráfico (Qntde. Transações 12m) *SALTA OS OLHOS = Se o cara 80 transações no ano ele não cancela mais o cartão FINALIDADE:
#Quase todos os clientes que cancelaram são da categoria Blue;
#Quanto mais o cliente entra em contato comigo, maior a chance dele cancelar -> Plano de ação: Analisar o motivo do contato/Tratar os clientes que mais entraram em contato com a gente
#Me parece, que quem usa pouco o cartão, cancela o cartão.
#Com mais de 80 transações, o cliente não cancela o cartão.
#Clientes com menos de 60 transações são muito críticos.
#A mesma coisa acontece com a quantidade de transações.
#SOLUÇÃO: Incentivar o uso do cartão, criar algum programa de incentivo.

