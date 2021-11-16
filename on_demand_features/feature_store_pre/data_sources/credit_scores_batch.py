from tecton import BatchDataSource, FileDSConfig


credit_scores_batch = BatchDataSource(
    name='credit_scores_batch',
    batch_ds_config=FileDSConfig(
        uri="s3://tecton.ai.public/data/fraud_mini/credit_scores/credit_scores.parquet",
        file_format='parquet',
        timestamp_column_name='timestamp'
    ),
    family='fraud_detection',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)
