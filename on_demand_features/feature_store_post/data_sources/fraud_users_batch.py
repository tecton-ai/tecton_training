from tecton import BatchDataSource, FileDSConfig


fraud_users_batch = BatchDataSource(
    name='users_batch',
    batch_ds_config=FileDSConfig(
        uri="s3://tecton.ai.public/data/fraud_mini/users/users.parquet",
        file_format='parquet',
        timestamp_column_name="signup_date"
    ),
    family='fraud',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)
