import dlt

@dlt.table(name="Stg_customers")

def Stg_customers():
  return spark.readStream.table("workspace.sales.customers")