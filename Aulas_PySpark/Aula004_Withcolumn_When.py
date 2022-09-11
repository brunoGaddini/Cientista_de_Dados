from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

if __name__ == "__main__":
    conf = SparkConf() \
    .setMaster("local") \
    .setAppName("estudando-dataframes")

    spark = SparkSession.builder.config(conf = conf).getOrCreate()

df = (spark
      .read
      .format("csv")
      .option("header","true")
      .option("inferSchema","true")
      .option("delimiter",",")
      .load("csv/cientista_de_dados.csv"))

# df.printSchema()

#Criando coluna com condição
#Neste ex. quero verificar a qtde de casos novos
#otherwise funciona de forma semelhante ao else

"""
df_status_casos_novos = (df.withColumn("Status",
                                       F.when(
                                       F.col("casosNovos") > 0, "Tem casos novos").
                                       otherwise("Sem casos novos")))


df_status_casos_novos.show(1000)
"""

#Concatenando o valor de casosNovos com "Status" casos novos
#A função lit trasnforma a leitura para str
"""
df_status_casos_novos = (df.withColumn("Status",
                                       F.when(
                                       F.col("casosNovos") > 0, F.concat(df.casosNovos, F.lit(" casos novos"))).
                                       otherwise("Sem casos novos")))


df_status_casos_novos.show(1000)
"""

# Criando coluna com dia, mês e ano. fazendo substring da coluna data, para isso preciso colocar dois valores (onde ela se inicia e o tamanho da substring)
#Nota-se que as colunas, dia, mês e ano são do tipo str, verificado pelo df.printSchema() antes de ser inserido o cast
df_status_casos_novos = (df.withColumn("Status",
                                       F.when(
                                       F.col("casosNovos") > 0, F.concat(df.casosNovos, F.lit(" casos novos"))).
                                       otherwise("Sem casos novos")).
                                       withColumn("Dia", F.substring(F.col("data"),9,2).cast("integer")).
                                       withColumn("Mês", F.substring(F.col("data"),6,2).cast("integer")).
                                       withColumn("Ano", F.substring(F.col("data"),1,4).cast("integer"))
                                       )

df_status_casos_novos.show(1000)

df.printSchema()