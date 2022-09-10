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

df.printSchema()


#Adicionando colunas
#new_df = df.withColumn("soma_novos_e_acumulados", F.col("casosNovos")+F.col("casosAcumulados"))
#new_df.show(1000)

#As funções SQL do PySpark lit() e typedLit() são usadas para adicionar uma nova coluna ao DataFrame atribuindo um valor literal ou constante. Ambas as funções retornam o tipo de coluna como tipo de retorno.
# Tranformando a coluna personalizada em str
#new_df = (df.withColumn("soma_novos_e_acumulados", F.col("casosNovos")+F.col("casosAcumulados")).
#          withColumn("coluna_personalizada", F.lit("O Valor da Coluna"))
#          )
#new_df.show(10)


# Utilizando Cast para altera o tipo da coluna
"""
new_df = (df.withColumn("soma_novos_e_acumulados", F.col("casosNovos")+F.col("casosAcumulados")).
          withColumn("coluna_personalizada", F.lit("O Valor da Coluna"))
          )
new_df_cast = new_df.select(F.col("casosNovos").cast("string"))
new_df_cast.printSchema()

new_df_cast.show(10)
"""

# Utilizando Cast em formato de expressão SQL para altera o tipo da coluna

new_df = (df.withColumn("soma_novos_e_acumulados", F.col("casosNovos") + F.col("casosAcumulados")).
          withColumn("coluna_personalizada", F.lit("O Valor da Coluna"))
          )
new_df_cast = new_df.selectExpr("cast(casosNovos as string)")
new_df_cast.printSchema()
# new_df_cast.show(10)
