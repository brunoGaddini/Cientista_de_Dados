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

"""
Se o .option inferSchema estiver como false, todas as colunas serão retornadas no tipo string
"""

#df.show(10)

# Exibe os tipos das colunas
#df.printSchema()

#df.select("regiao","estado","casosNovos").show(10)

# Buscando funções de str que posso utilizar
# Buscando funções de coluna que posso utilizar

#print(dir("regiao"))
#print(dir(F.col("regiao")))

#df.select(F.col("regiao"),F.col("estado"),F.col("casosNovos")).filter(F.col("regiao") != "Sul" ).show(10)

#df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter("regiao = 'Norte'").show(10)

#df com variáveis
filtro = F.col("regiao") == "Sul"
df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter(filtro).show(10)