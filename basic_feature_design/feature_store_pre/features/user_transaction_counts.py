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
