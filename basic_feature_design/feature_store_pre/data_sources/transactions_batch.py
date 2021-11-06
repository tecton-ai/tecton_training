from tecton import BatchDataSource, FileDSConfig, inlined

@inlined
def cast_timestamp(df):
    from pyspark.sql import functions as F
    return df.withColumn("timestamp", F.to_timestamp("timestamp", "yyyy-MM-dd HH:mm:ss"))

transactions_batch = BatchDataSource(
    name='transactions_batch',
    batch_ds_config=FileDSConfig(
        timestamp_column_name="timestamp",
        uri="s3://tecton.ai.public/data/fraud_mini/transactions/transactions.parquet",
        file_format="parquet"
    ),
    family='fraud_detection',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)
