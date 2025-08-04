import dlt

DQ_customers = {
    "rule_1" : "customer_id IS NOT NULL",
    "rule_2" : "customer_name IS NOT NULL"
}

@dlt.expect_all(DQ_customers)
@dlt.table(name="Stg_customers")

def Stg_customers():
  return spark.readStream.table("workspace.sales.customers")