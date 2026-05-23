MLflow generally organizes its data into two core directory structures: the local artifact/storage directory (often named mlruns or mlartifacts) and 
the MLflow Model package directory. The former captures experiments and tracking logs, while the latter packages individual models for deployment
## 1. Tracking Server & File System (mlruns)
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
## 2. MLflow Model Directory
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
