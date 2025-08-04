import dlt

dlt.create_streaming_table(
    name="dim_customers"
)

dlt.create_auto_cdc_flow(
    target = "dim_customers",
    source = "VW_Stg_customers",
    keys = ["customer_id"],
    sequence_by = "last_updated",
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 2,
    track_history_column_list = None,
    track_history_except_column_list = None
)