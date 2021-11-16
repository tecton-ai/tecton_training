from tecton import (
    batch_window_aggregate_feature_view, 
    Input,
    FeatureAggregation, 
    Entity
)
from datetime import datetime
from data_sources.transactions_batch import transactions_batch

user = Entity(
    name='fraud_user',
    default_join_keys=['user_id']
)

# Add feature view code from workshop here
@batch_window_aggregate_feature_view(
    inputs={'transactions': Input(transactions_batch)},
    entities=[user],
    mode='spark_sql',
    aggregations=[
        FeatureAggregation(column='transaction', function='count', time_windows=['24h', '72h'])
    ],
    aggregation_slide_period='24h',
    online=True,
    offline=True,
    feature_start_time=datetime(2020, 10, 10)
)
def user_transaction_counts(transactions):
    return f'''
    SELECT
  nameOrig AS user_id,
  1 AS transaction,
  timestamp
FROM {transactions}
'''