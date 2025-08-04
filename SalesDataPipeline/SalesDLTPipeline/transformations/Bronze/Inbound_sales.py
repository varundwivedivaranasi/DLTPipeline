# Importing required libraries
import dlt
from pyspark.sql import DataFrame

#Empty streaming table
dlt.create_streaming_table(name = "Stg_Sales")

# Define a flow to append East region sales data
@dlt.append_flow(target="Stg_Sales")
def east_sales() -> DataFrame:
    """
    Reads streaming data from the 'sales_east' source table
    and returns it as a DataFrame.
    """
    df = spark.readStream.table("workspace.sales.sales_east")
    return df

# Define a flow to append West region sales data
@dlt.append_flow(target="Stg_Sales")
def west_sales() -> DataFrame:
    """
    Reads streaming data from the 'sales_west' source table
    and returns it as a DataFrame.
    """
    df = spark.readStream.table("workspace.sales.sales_west")
    return df