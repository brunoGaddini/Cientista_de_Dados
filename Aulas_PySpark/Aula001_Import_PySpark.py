# from pyspark.sql import SparkSession  #Na cor cinza significa que não estamos utilizando

"""
def main():
    pass

if __name__ == "__main__":
    main()
"""

"""
# Primeira forma
# [] definir quantas treads - * = 1 ou mais
# definindo o appName

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local") \
        .appName("estudando-dataframes") \
        .getOrCreate()

    print(spark)
"""


# Segunda forma
from pyspark import SparkConf
from pyspark.sql import SparkSession

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

df.show(100)