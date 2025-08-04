import dlt
from pyspark.sql import functions as fn
from pyspark.sql.window import Window

@dlt.table
def orders_stream_table():
    df = spark.readStream.table("workspace.myschema.orders")
    return df

@dlt.view
def order_transformations():
    df = spark.read.table("orders_stream_table")
    tns_df = df.withColumn("Number_of_order_per_customer", fn.count("*").over(Window.partitionBy("customer_id")))
    return tns_df

@dlt.table
def materialized_orders():
    df = dlt.read("order_transformations")
    return df