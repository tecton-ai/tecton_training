from tecton import (
    batch_feature_view, 
    Aggregation, 
    Entity
)
from datetime import datetime, timedelta
from data_sources.transactions_batch import transactions_batch

user = Entity(
    name='fraud_user',
    join_keys=['user_id']
)

# Add feature view code from workshop here
@batch_feature_view(
    sources=[transactions_batch],
    entities=[user],
    mode='spark_sql',
    aggregations=[
        Aggregation(column='transaction', function='count', time_window=timedelta(hours=24)),
        Aggregation(column='transaction', function='count', time_window=timedelta(hours=72))
    ],
    aggregation_interval=timedelta(hours=24),
    online=True,
    offline=True,
    feature_start_time=datetime(2020, 10, 10)
)
def user_transaction_counts(transactions_batch):
    return f'''
        SELECT
        nameOrig AS user_id,
        1 AS transaction,
        timestamp
        FROM {transactions_batch}
    '''