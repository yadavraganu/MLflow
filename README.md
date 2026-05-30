## MLflow Components
MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It is built around four primary components: Tracking, Projects, Models, and the Model Registry.

### 1. MLflow Tracking
An API and UI for logging machine learning experiments. It records parameters, code versions, metrics, and output files (artifacts) to help you compare results and reproduce runs. 
- Parameters: Hyperparameters and configuration settings. 
- Metrics: Evaluation scores (e.g., accuracy, F1-score) logged over time. 
- Artifacts: Output files like model weights, datasets, and plots. 
- Tracking Server: A centralized server that stores your experiment data in a backend database (e.g., PostgreSQL) and artifacts in object storage (e.g., AWS S3).

### 2. MLflow Projects 
A format for packaging data science and machine learning code in a reusable and reproducible way. 
- Dependency Management: Projects use a standard format (like a  or Docker image) to define environment and library dependencies. 
- Reproducibility: Allows teams to easily share code and run it identically across different machines or cloud platforms.

### 3. MLflow Models
A standard format for packaging machine learning models from any library so they can be used across various downstream deployment, serving, and inference tools. 
- Flavors: MLflow uses "flavors" to explain to tools how a model should be treated (e.g., a "scikit-learn" model flavor vs. a generic "Python function" flavor). 
- Serving: Models can easily be spun up as local REST APIs, deployed to cloud platforms (like AWS SageMaker or Azure ML), or packaged as Docker containers. 

### 4. Model Registry
A centralized repository designed to collaboratively manage the full lifecycle of an MLflow Model. 
- Version Control: Automatically tracks model versions as they are updated. 
- Stage Transitions: Provides structured workflows to manage transitions through predefined stages (e.g., Staging, Production, or Archived). 
- Lineage: Keeps a clear history of which experiment run produced which registered model.
---
MLflow generally organizes its data into two core directory structures: the local artifact/storage directory (often named mlruns or mlartifacts) and 
the MLflow Model package directory. The former captures experiments and tracking logs, while the latter packages individual models for deployment
### 1. Tracking Server & File System (mlruns)
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
### 2. MLflow Model Directory
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
