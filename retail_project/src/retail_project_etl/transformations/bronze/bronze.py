from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark import pipelines as dp

@dp.table(
    name="retail.bronze.retail_sales_dataset"
)
def load_data():
  return (
    spark.readStream.table("retail.source.retail_sales_dataset")
  )
