from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

if __name__ == "__main__":
    conf = SparkConf() \
    .setMaster("local") \
    .setAppName("estudando-dataframes")

    spark = SparkSession.builder.config(conf = conf).getOrCreate()
"""
df = (spark
      .read
      .format("csv")
      .option("header","false")
      .option("inferSchema","false")
      .option("delimiter",",")
      .load("csv/cientista_de_dados.csv").toDF("um", "dois", "três", "quatro", "cinco", "seis", "sete"))
"""

# Nota-se que com a opção false em header na criação do df, o spark nomeia as colunas para nós
# df.printSchema()

# Uma forma de nomear as colunas no início é com a criação de um schema, conforme Aula005
# Outra forma de se inserir os nomes das colunas é com o .toDF

# Outra forma de se criar um df com lista. Esta forma no .toDF é criando uma lista

"""
lista = ["um", "dois", "três", "quatro", "cinco", "seis", "sete"]

df = (spark
      .read
      .format("csv")
      .option("header","false")
      .option("inferSchema","false")
      .option("delimiter",",")
      .load("csv/cientista_de_dados.csv").toDF(*lista))

df.printSchema()
"""

df = (spark
      .read
      .format("csv")
      .option("header","false")
      .option("inferSchema","false")
      .option("delimiter",",")
      .load("csv/cientista_de_dados.csv"))

# Definindo os nomes das colunas com pyspark functions e .alias

df = (df.select(F.col("_c0").alias("um"),
                F.col("_c1").alias("dois"),
                F.col("_c2").alias("três"),
                F.col("_c3").alias("quatro"),
                F.col("_c4").alias("cinco"),
                F.col("_c5").alias("seis"),
                F.col("_c6").alias("sete")))

df.printSchema()

