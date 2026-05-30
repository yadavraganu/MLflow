## MLflow Components
MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It is built around four primary components: Tracking, Projects, Models, and the Model Registry.

#### MLflow Tracking
An API and UI for logging machine learning experiments. It records parameters, code versions, metrics, and output files (artifacts) to help you compare results and reproduce runs. 
- Parameters: Hyperparameters and configuration settings. 
- Metrics: Evaluation scores (e.g., accuracy, F1-score) logged over time. 
- Artifacts: Output files like model weights, datasets, and plots. 
- Tracking Server: A centralized server that stores your experiment data in a backend database (e.g., PostgreSQL) and artifacts in object storage (e.g., AWS S3).

#### MLflow Projects 
A format for packaging data science and machine learning code in a reusable and reproducible way. 
- Dependency Management: Projects use a standard format (like a  or Docker image) to define environment and library dependencies. 
- Reproducibility: Allows teams to easily share code and run it identically across different machines or cloud platforms.

#### MLflow Models
A standard format for packaging machine learning models from any library so they can be used across various downstream deployment, serving, and inference tools. 
- Flavors: MLflow uses "flavors" to explain to tools how a model should be treated (e.g., a "scikit-learn" model flavor vs. a generic "Python function" flavor). 
- Serving: Models can easily be spun up as local REST APIs, deployed to cloud platforms (like AWS SageMaker or Azure ML), or packaged as Docker containers. 

#### Model Registry
A centralized repository designed to collaboratively manage the full lifecycle of an MLflow Model. 
- Version Control: Automatically tracks model versions as they are updated. 
- Stage Transitions: Provides structured workflows to manage transitions through predefined stages (e.g., Staging, Production, or Archived). 
- Lineage: Keeps a clear history of which experiment run produced which registered model.


## 1. Tracking 
#### Environment & Setup

| Function | Purpose | Parameters | Example |
|----------|---------|------------|---------|
| `mlflow.set_tracking_uri(uri)` | Connect to a tracking server or database. | **uri (str)** → URI of tracking server. Options: `"file:/path/to/dir"`, `"http://host:port"`, `"databricks"` | `mlflow.set_tracking_uri("http://localhost:5000")` |
| `mlflow.get_tracking_uri()` | Get the current tracking URI. | *(no parameters)* | `uri = mlflow.get_tracking_uri()` |
| `mlflow.create_experiment(name, artifact_location=None, tags=None)` | Create a new experiment. | **name (str)** → Experiment name <br> **artifact_location (str, optional)** → Path/URI for artifacts <br> **tags (dict, optional)** → Metadata tags | `exp_id = mlflow.create_experiment("my-exp", artifact_location="/mnt/artifacts", tags={"team":"fraud"})` |
| `mlflow.set_experiment(name)` | Set the active experiment. Creates if missing. | **name (str)** → Experiment name | `mlflow.set_experiment("fraud-detection")` |
| `mlflow.get_experiment(experiment_id)` | Get metadata for an experiment. | **experiment_id (str)** | `exp = mlflow.get_experiment("1")` |
| `mlflow.get_experiment_by_name(name)` | Get experiment details by name. | **name (str)** | `exp = mlflow.get_experiment_by_name("fraud-detection")` |
| `mlflow.list_experiments()` | List all experiments. | *(no parameters)* | `experiments = mlflow.list_experiments()` |
| `mlflow.search_experiments(filter_string=None)` | Search experiments by filter criteria. | **filter_string (str, optional)** | `mlflow.search_experiments("tags.team = 'fraud'")` |


#### Run Lifecycle Management

| Function | Purpose | Parameters | Example |
|----------|---------|------------|---------|
| `mlflow.start_run(run_name=None, nested=False, tags=None)` | Start a new run. | **run_name (str, optional)** <br> **nested (bool, optional)** <br> **tags (dict, optional)** | `mlflow.start_run(run_name="baseline-model", tags={"stage":"dev"})` |
| `mlflow.end_run(status="FINISHED")` | End the active run. | **status (str, optional)** → `"FINISHED"`, `"FAILED"`, `"KILLED"` | `mlflow.end_run(status="FAILED")` |
| `mlflow.active_run()` | Get the currently active run object. | *(no parameters)* | `active_run = mlflow.active_run()` |

#### Logging (Manual & Automated)

| Function | Purpose | Parameters | Example |
|----------|---------|------------|---------|
| `mlflow.autolog()` | Automatically log params, metrics, and models for supported frameworks. | **disable (bool)** + framework-specific configs | `mlflow.autolog()` |
| `mlflow.log_param(key, value)` | Log a single parameter. | **key (str)**, **value (any)** | `mlflow.log_param("learning_rate", 0.01)` |
| `mlflow.log_params(params)` | Log multiple parameters. | **params (dict)** | `mlflow.log_params({"lr":0.01, "batch_size":32})` |
| `mlflow.log_metric(key, value, step=None)` | Log a single metric. | **key (str)**, **value (float)**, **step (int, optional)** | `mlflow.log_metric("accuracy", 0.95, step=10)` |
| `mlflow.log_metrics(metrics, step=None)` | Log multiple metrics. | **metrics (dict)**, **step (int, optional)** | `mlflow.log_metrics({"loss":0.2, "accuracy":0.95}, step=5)` |
| `mlflow.set_tags(tags)` | Add metadata tags to a run. | **tags (dict)** | `mlflow.set_tags({"framework":"pytorch", "owner":"anurag"})` |
| `mlflow.log_artifact(local_path, artifact_path=None)` | Log a single file. | **local_path (str)**, **artifact_path (str, optional)** | `mlflow.log_artifact("model.pkl", artifact_path="models")` |
| `mlflow.log_artifacts(local_dir, artifact_path=None)` | Log all files in a directory. | **local_dir (str)**, **artifact_path (str, optional)** | `mlflow.log_artifacts("plots", artifact_path="figures")` |
| `mlflow.get_artifact_uri()` | Get artifact URI for current run. | *(no parameters)* | `uri = mlflow.get_artifact_uri()` |

#### Querying Past Runs

| Function | Purpose | Parameters | Example |
|----------|---------|------------|---------|
| `mlflow.get_run(run_id)` | Get metadata, params, metrics for a run. | **run_id (str)** | `run = mlflow.get_run("run_id_123")` |
| `mlflow.search_runs(experiment_ids, filter_string=None, order_by=None)` | Search/filter runs. Returns Pandas DataFrame. | **experiment_ids (list)** <br> **filter_string (str, optional)** <br> **order_by (list, optional)** | `df = mlflow.search_runs(["1"], filter_string="metrics.accuracy > 0.9")` |

#### Model Registry & Deployment

| Function | Purpose | Parameters | Example |
|----------|---------|------------|---------|
| `mlflow.register_model(model_uri, name)` | Register a model into the Model Registry. | **model_uri (str)**, **name (str)** | `mlflow.register_model("runs:/123/model", "Fraud_Model")` |
| `mlflow.transition_model_version_stage(name, version, stage)` | Move a model version between stages. | **name (str)**, **version (int)**, **stage (str)** → `"Staging"`, `"Production"`, `"Archived"` | `mlflow.transition_model_version_stage("Fraud_Model", 1, "Production")` |
| `mlflow.search_model_versions(filter_string)` | Search for model versions. | **filter_string (str)** | `mlflow.search_model_versions("name='Fraud_Model'")` |
| `mlflow.get_model_version(name, version)` | Get details of a specific model version. | **name (str)**, **version (int)** | `mv = mlflow.get_model_version("Fraud_Model", 1)` |

## Directory Structure
MLflow generally organizes its data into two core directory structures: the local artifact/storage directory (often named mlruns or mlartifacts) and 
the MLflow Model package directory. The former captures experiments and tracking logs, while the latter packages individual models for deployment
#### 1. Tracking Server & File System (mlruns)
By default, MLflow stores your experiment runs, parameters, metrics, tags, and large artifacts (like model weights) locally in an mlruns/ directory.
The hierarchical directory layout follows this structure:
```
mlruns/
├── 0/                           # Experiment ID (0 is the default experiment)
│   ├── meta.yaml                # Experiment metadata (name, artifact location)
│   ├── a1b2c3d4.../             # Run UUID
│   │   ├── artifacts/           # Directory for large files (model pickles, images)
│   │   │   └── model/           # Saved MLflow model folder (see structure below)
│   │   ├── metrics/             # Directory containing logged metrics (e.g., loss, accuracy)
│   │   ├── params/              # Directory containing logged parameters (e.g., learning_rate)
│   │   ├── tags/                # Directory containing run tags (e.g., user, source)
│   │   └── meta.yaml            # Metadata about the run (start_time, status, etc.)
│   └── ...                      # Additional runs
└── models/                      # (Optional) Registered Models directory depending on configuration
```
#### 2. MLflow Model Directory
When you log or save an MLflow model (usually via flavors like mlflow.sklearn, mlflow.pytorch, etc.), the model itself becomes a structured, reproducible directory. This bundle includes both the binary payload and the metadata required to reload or serve it in any environment.
The model directory structure typically looks like this:
```
model/
├── MLmodel                      # The core MLflow MLmodel configuration file
├── model.pkl                    # The serialized model binary (or model.yaml/model.h5)
├── conda.yaml                   # Conda environment definition with dependencies
├── python_env.yaml              # Requirements formatted for Python environment managers (e.g., pip)
├── requirements.txt             # Exact pip dependencies for inference
└── input_example.json           # (Optional) Example input payload to test predictions
```
