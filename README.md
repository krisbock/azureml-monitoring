
# This repository contains a collection of sample notebooks to learn about ML monitoring with the Azure Machine Learning service:
1. [Datadrift](./datadrift-tutorial/datadrift-tutorial.ipynb): tutorial on how to use the Datadrift service to monitor your data

## Use monitoring API with Azure Machine Learning service
1. [Logging API](./logging-api/logging-api.ipynb): experiment with various logging functions to create runs and automatically generate graphs.
2. [Manage runs](./manage-runs/manage-runs.ipynb): learn different ways how to start runs and child runs, monitor them, and cancel them.
3. [Tensorboard to monitor runs](./tensorboard/tensorboard.ipynb)

## Use MLflow with Azure Machine Learning service (Preview)

[MLflow](https://mlflow.org/) is an open-source platform for tracking machine learning experiments and managing models. You can use MLflow logging APIs with Azure Machine Learning service: the metrics and artifacts are logged to your Azure ML Workspace.

Try out the sample notebooks:
1. [Use MLflow with Azure Machine Learning for Local Training Run](./using-mlflow/train-local/train-local.ipynb)
2. [Use MLflow with Azure Machine Learning for Remote Training Run](./using-mlflow/train-remote/train-remote.ipynb)
3. [Use MLflow with Azure Machine Learning to submit runs locally with MLflow projects](./using-mlflow/train-projects-local/train-projects-local.ipynb)
4. [Use MLflow with Azure Machine Learning to submit runs on AzureML compute with MLflow projects](./using-mlflow/train-projects-remote/train-projects-remote.ipynb)
