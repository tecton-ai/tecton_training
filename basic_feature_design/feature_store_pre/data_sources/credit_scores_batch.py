from tecton import BatchSource, FileConfig


credit_scores_batch = BatchSource(
    name='credit_scores_batch',
    batch_config=FileConfig(
        uri="s3://tecton.ai.public/data/fraud_mini/credit_scores/credit_scores.parquet",
        file_format='parquet',
        timestamp_field='timestamp'
    ),
    owner='jack@tecton.ai',
    tags={'release': 'production'}
)
