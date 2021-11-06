# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Note that you need to be running Python 3.7
# %pip install tecton

# %% [markdown]
# ## Create endpoint

# %%
from sagemaker.sklearn.model import SKLearnModel

# %%
from sagemaker.predictor import Predictor, JSONDeserializer, IdentitySerializer

class FraudPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session):
        super().__init__(endpoint_name, sagemaker_session=sagemaker_session, 
                         serializer=JSONSerializer(),
                         deserializer=JSONDeserializer(), content_type='application/json')


# %%
smmodel = SKLearnModel(
  model_data='s3://tecton.ai.public/training/tecton_sagemaker/model-artifact.tar.gz',
  # Sagemaker IAM role + access to any buckets
  role=sagemaker.get_execution_role(),
  # This file should exist on the local machine
  entry_point='serve.py',
  py_version='py3',
  framework_version='0.23-1',
  source_dir='code',
  predictor_cls=FraudPredictor
)

# %%
predictor = smmodel.deploy(
    initial_instance_count=1,
#     instance_type='ml.m4.xlarge'
    instance_type='local',
    serializer=JSONSerializer(),
    deserializer=JSONDeserializer(),
    content_type='application/json'
)

# %%
import json

# %%
data = json.dumps({'user_id': 'C387780307', 'amount': 12345.67})
data

# %%
predictor.predict(data)

# %%
predictor.delete_endpoint()

# %% [markdown]
# # Test Tecton inference

# %%
import tecton

# %%
# Set Tecton secrets
secretcli = boto3.client('secretsmanager')

api_service = secretcli.get_secret_value(SecretId='tecton-demo-copper-a/API_SERVICE')
tecton.conf.set('API_SERVICE', api_service['SecretString'])

tecton_api_key = secretcli.get_secret_value(SecretId='tecton-demo-copper-a/TECTON_API_KEY')
tecton.conf.set('TECTON_API_KEY', tecton_api_key['SecretString'])

# %%
tecton.list_feature_services()

# %%
tecton.list_workspaces()

# %%
ws = tecton.get_workspace('jack-workshop-intro')

# %%
fs = ws.get_feature_service('fraud')

# %%
fs.summary()

# %%
fs.get_online_features(join_keys={'user_id': 'C809557940'}).to_dict()

# %%
