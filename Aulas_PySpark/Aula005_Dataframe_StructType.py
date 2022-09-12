from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pyspark.sql.functions as F

"""
O StructType e StructFields são usados para definir um esquema ou sua parte para o Dataframe. Isso define o nome, tipo de dados e sinalizador anulável
para cada coluna. O objeto StructType é a coleção de objetos StructFields. É um tipo de dados interno que contém a lista de StructField.

PySpark STRUCTTYPE é uma maneira de criar um quadro de dados no PySpark.

https://www.educba.com/pyspark-structtype/

Para definir o esquema, temos que usar o objeto StructType() no qual temos que definir ou passar o StructField() que contém o nome da coluna, o tipo de dados da coluna e o sinalizador anulável. 
Nós podemos escrever:

Ex1:
schema = StructType([StructField(column_name1,datatype(),nullable_flag),
            StructField(column_name2,datatype(),nullable_flag),
            StructField(column_name3,datatype(),nullable_flag)
            ])

Ex2:
sch = StructType([StructField("Name",StringType(),True),StructField("ID",StringType(), True),StructField("ADD",StringType() , True)])
"""

# Novos imports realizado from pyspark.sql.types

# StringType – Uma string de texto.
# IntegerType – Um valor inteiro.

if __name__ == "__main__":
    conf = SparkConf() \
    .setMaster("local") \
    .setAppName("estudando-dataframes")

    spark = SparkSession.builder.config(conf = conf).getOrCreate()

# Criando e definindo tipos dos dados
    schema = (StructType([
        StructField("regiao", StringType(), True),
        StructField("estado", StringType(), True),
        StructField("data", StringType(), True),
        StructField("casosNovos", IntegerType(), True),
        StructField("casosAcumulados", IntegerType(), True),
        StructField("obitosNovos", IntegerType(), True),
        StructField("obitosAcumulados", IntegerType(), True),
    ]))

# Para o sucesso da criação do schema é necessário definir que o load vai receber schema

df = (spark
      .read
      .format("csv")
      .option("header","true")
      .option("inferSchema","false")
      .option("delimiter",",")
      .load("csv/cientista_de_dados.csv", schema = schema))

df.printSchema()

# Primeiro passo, retornar tudo como str. Passo realizado na criação do dataframe .option("inferSchema") com a opção false.
