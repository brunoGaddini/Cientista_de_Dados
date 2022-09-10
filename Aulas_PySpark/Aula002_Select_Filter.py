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

df_erros = df

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
#filtro = F.col("regiao") == "Sul"
#df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter(filtro).show(10)
"""
df.printSchema()

df_erros.createOrReplaceTempView ('Performance')

spark.sql('''

        select 
        count(*)
        from Performance

        ''').show()


spark.sql('''

        select 
        count(distinct regiao)
        from Performance

        ''').show()


spark.sql('''

        select distinct regiao from Performance

        ''').show(5)
"""

#df.printSchema()

# Utilizando dois filtros
# 1ª forma
#df.filter("regiao = 'Norte'").filter("estado = 'AM'").show(10)

#2ª forma
#df.filter("regiao = 'Norte' and estado = 'AM'").show(10)

# 3º forma utilizando & como agregador
#df.filter((F.col("regiao") == 'Norte') & (F.col("estado") == 'AM')).show(10)

#O | aqui funciona como not
#df.filter((F.col("regiao") == 'Norte') | (F.col("estado") == 'AM')).show(10)

# Utilizando where
#df.where((F.col("regiao") == 'Norte') | (F.col("estado") == 'AM')).show(10)

# Utilizando like - ex: buscando estado iniciando com a letra A na regiao norte
#df.filter((F.col("regiao") == 'Norte')).filter("estado like 'A%'").show(10)

#df.filter("regiao in ('Norte','Sul')").show(1000)

# Utilando lista
#lista_regiao = ["Norte","Sul"]
#df.filter(F.col("regiao").isin(lista_regiao)).show(1000)

# Utilizando o startwith
df.filter(F.col("regiao").startswith("C")).show(1000)
