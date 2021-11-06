# https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-inference-container.html
import logging, requests, os, io, glob, time
import joblib
import tecton
import json

JSON_CONTENT_TYPE = 'application/json'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

tecton_fs = None

# loads the model into memory from disk and returns it
def model_fn(model_dir):
    logger.info('model_fn')
    model = joblib.load(f'{model_dir}/model.joblib')
    
    # Get and set Tecton secrets
    secretcli = boto3.client('secretsmanager')
    api_service = secretcli.get_secret_value(SecretId='tecton-demo-copper-a/API_SERVICE')
    tecton.conf.set('API_SERVICE', api_service['SecretString'])
    tecton_api_key = secretcli.get_secret_value(SecretId='tecton-demo-copper-a/TECTON_API_KEY')
    tecton.conf.set('TECTON_API_KEY', tecton_api_key['SecretString'])
    
    tecton_fs = tecton.get_workspace('jack-workshop-intro').get_feature_service('fraud')
    return model

# Deserialize the Invoke request body into an object we can perform prediction on
def input_fn(request_body, content_type=JSON_CONTENT_TYPE):
    logger.info('Deserializing the input data.')
    logger.debug(request_body)
    return request_body

# Perform prediction on the deserialized object
def predict_fn(input_object, model):
    tecton_features = tecton_fs.get_feature_vector(join_keys={'user_id': input_object['user_id']})
    return model.predict(input_object + tecton_features)

# Serialize the prediction result into the desired response content type
def output_fn(prediction, accept=JSON_CONTENT_TYPE):
    logger.info('Serializing the generated output.')
    if accept == JSON_CONTENT_TYPE: return json.dumps(prediction), accept
    raise Exception('Requested unsupported ContentType in Accept: {}'.format(accept)) 

