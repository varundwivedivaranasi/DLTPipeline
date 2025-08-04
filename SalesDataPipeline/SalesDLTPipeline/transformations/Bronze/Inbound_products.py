import dlt

DQ_products = {
    "rule_1" : "product_id IS NOT NULL",
    "rule_2" : "price >= 0"
}

@dlt.expect_all(DQ_products)
@dlt.table(name="Stg_products")

def Stg_products():
  return spark.readStream.table("workspace.sales.products")