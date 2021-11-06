import sagemaker
from sagemaker.sklearn.model import SKLearnModel

smmodel = SKLearnModel(
  model_data='s3://tecton-demo-copper-a-jack-fraud-model-output/fraud_model_artifact/tecton-jack-artifact.tar.gz',
  # Sagemaker IAM role + access to any buckets
    role=sagemaker.get_execution_role(),
    # This file should exist on the local machine
  entry_point='serve.py',
  py_version='py3',
  framework_version='0.23-1',
  source_dir='code'
)

from sagemaker.predictor import Predictor, JSONDeserializer

class FraudPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session):
        super().__init__(endpoint_name, sagemaker_session=sagemaker_session)

smmodel.deploy(
    initial_instance_count=1, 
#     instance_type='ml.m4.xlarge'
    instance_type='local'
)
