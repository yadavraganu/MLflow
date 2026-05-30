| Function | Purpose | Example | Notes |
| --- | --- | --- | --- |
| ``mlflow.set_tracking_uri()`` | Connect to a tracking server or database | ``mlflow.set_tracking_uri("http://localhost:5000")`` | This tells MLflow where to log runs. Can be a local file path, a database, or a remote server. |
| ``mlflow.get_tracking_uri()`` | Get the current tracking URI | ``uri ``= ``mlflow.get_tracking_uri()`` | Useful for debugging or confirming which backend MLflow is writing to. |
| ``mlflow.create_experiment()`` | Create a new experiment | ``exp_id ``= ``mlflow.create_experiment("my-experiment")`` | Returns an experiment ID. You can also specify an artifact location here. |
| ``mlflow.set_experiment()`` | Set the active experiment | ``mlflow.set_experiment("fraud-detection")`` | If the experiment doesn’t exist, MLflow will create it automatically. |