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
import boto3

# %%
emr = boto3.client('emr', region_name='us-west-2')

# %%
start_resp = emr.start_notebook_execution(
    EditorId='<your notebook instance, starts with e->',
    RelativePath='test.ipynb',
    ExecutionEngine={'Id': '<your Tecton EMR notebook cluster, starts with j->'},
    ServiceRole='EMR_Notebooks_DefaultRole'
)

# %%
execution_id = start_resp["NotebookExecutionId"]
execution_id

# %% [markdown]
# Wait until the notebook cluster is finished executing, will take ~2-3 mins to spin up the cluster plus execution time

# %%
import time

while True:
    describe_response = emr.describe_notebook_execution(NotebookExecutionId=execution_id)
    status = describe_response['NotebookExecution']['Status']
    print(status)
    
    # status codes documented here: https://docs.aws.amazon.com/cli/latest/reference/emr/describe-notebook-execution.html
    if status in ['FINISHED', 'STOPPED', 'FAILED']:
        break
    
    time.sleep(5)

# %%
try:
    emr.stop_notebook_execution(NotebookExecutionId=execution_id)
except:
    print('Tried to stop notebook, but notebook is not running')
