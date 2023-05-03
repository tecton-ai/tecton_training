from tecton import FeatureService
from features.user_transaction_counts import user_transaction_counts

FraudFeatureService = FeatureService(
    name='fraud',
    features=[user_transaction_counts],
    online_serving_enabled=True
)
