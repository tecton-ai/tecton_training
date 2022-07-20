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
