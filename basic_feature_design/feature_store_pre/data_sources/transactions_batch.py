from tecton import BatchSource, FileConfig

transactions_batch = BatchSource(
    name='transactions_batch',
    batch_config=FileConfig(
        timestamp_field="timestamp",
        uri="s3://tecton.ai.public/data/fraud_mini/transactions/transactions.parquet",
        file_format="parquet"
    ),
    owner='jack@tecton.ai',
    tags={'release': 'production'}
)
