#%%
import json
import azureml
from azureml.core.model import Model
from azureml.core import Workspace, Run, Datastore, Experiment
from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.compute import BatchAiCompute
from azureml.core.compute import ComputeTarget
from azureml.train.dnn import TensorFlow
from azureml.train.widgets import RunDetails

# check core SDK version number
print("Azure ML SDK Version: ", azureml.core.VERSION)

#%%
# use this code to set up config file
#subscription_id ='<SUB_ID>'
#resource_group ='<RESOURCE_GROUP>'
#workspace_name = '<WORKSPACE>'

#try:
#   ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
#   ws.write_config()
#   print('Workspace configuration succeeded. You are all set!')
#except:
#   print('Workspace not found. TOO MANY ISSUES!!!')
ws = Workspace.from_config()

#%%
# Checking Compute Targets
ws.compute_targets