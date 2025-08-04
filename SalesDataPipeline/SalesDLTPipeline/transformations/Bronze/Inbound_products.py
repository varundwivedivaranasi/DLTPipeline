import dlt

@dlt.table(name="Stg_products")

def Stg_products():
  return spark.readStream.table("workspace.sales.products")