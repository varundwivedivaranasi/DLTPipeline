import dlt

@dlt.view(
    name = "VW_Stg_customers"
)

def VW_Stg_customers():
    df = spark.readStream.table("Stg_customers")
    return df

dlt.create_streaming_table(
    name = "Silver_Customers"
)

dlt.create_auto_cdc_flow(
    target = "Silver_Customers",
    source = "VW_Stg_customers",
    keys = ["customer_id"],
    sequence_by = "last_updated",
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 1,
    track_history_column_list = None,
    track_history_except_column_list = None
)