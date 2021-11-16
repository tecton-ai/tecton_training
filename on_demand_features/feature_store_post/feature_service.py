from tecton import FeatureService
from features.user_transaction_counts import user_transaction_counts
from features.transaction_amount_is_high import transaction_amount_is_high

FraudFeatureService = FeatureService(
    name='fraud',
    features=[
        user_transaction_counts,
        transaction_amount_is_high
    ],
    online_serving_enabled=True
)
