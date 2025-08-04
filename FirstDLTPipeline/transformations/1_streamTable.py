import dlt

@dlt.table
def orders_stream_table():
    df = spark.readStream.table("workspace.myschema.orders")
    return df

@dlt.table
def materialized_orders():
    df = dlt.read("orders_stream_table")
    return df