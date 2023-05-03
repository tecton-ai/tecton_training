from tecton import BatchSource, FileConfig


fraud_users_batch = BatchSource(
    name='users_batch',
    batch_config=FileConfig(
        uri="s3://tecton.ai.public/data/fraud_mini/users/users.parquet",
        file_format='parquet',
        timestamp_field="signup_date"
    ),
    owner='jack@tecton.ai',
    tags={'release': 'production'}
)
