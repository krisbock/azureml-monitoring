import os
import pickle
import json
import numpy
from azureml.monitoring import ModelDataCollector
import joblib
from sklearn.linear_model import Ridge
import time

def init():
    global model
    global inputs_dc, prediction_dc
    inputs_dc = ModelDataCollector("sklearn_regression_model.pkl", designation="inputs", feature_names=["x1", "x2", "x3", "x4", "x5", "x6",  "x7", "x8", "x9", "x10"])
    prediction_dc = ModelDataCollector("sklearn_regression_model.pkl", designation="predictions", feature_names=["prediction1", "prediction2"])
    #Print statement for appinsights custom traces:
    print ("model initialized" + time.strftime("%H:%M:%S"))

    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # For multiple models, it points to the folder containing all deployed models (./azureml-models)
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sklearn_regression_model.pkl')

    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)


# note you can pass in multiple rows for scoring
def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = numpy.array(data)
        result = model.predict(data)
        inputs_dc.collect(data) #this call is saving our input data into Azure Blob
        prediction_dc.collect(result) #this call is saving our prediction data into Azure Blob
        print ("Prediction created" + time.strftime("%H:%M:%S"))
        # you can return any datatype as long as it is JSON-serializable
        return result.tolist()
    except Exception as e:
        error = str(e)
        print (error + time.strftime("%H:%M:%S"))
        return error
