A model registry in MLOps is a centralized repository that manages the lifecycle of machine learning models. It serves as a version control and tracking system for models, organizing everything from initial development and testing to production deployment, staging, and archiving

Using the Model Registry offers the following benefits:
- **Version Control**: The registry automatically tracks versions of each model, allowing teams to compare iterations, roll back to previous states, and manage multiple versions in parallel (e.g., staging vs. production).
- **Model Lineage and Traceability**: Each registered model version is linked to the MLflow run, logged model or notebook that produced it, enabling full reproducibility. You can trace back exactly how a model was trained, with what data and parameters.
- **Production-Ready Workflows**: Features like model aliases (e.g., @champion) and tags make it easier to manage deployment workflows, promoting models to experimental, staging, or production environments in a controlled and auditable way.
- **Governance and Compliance**: With structured metadata, tagging, and role-based access controls (when used with a backend like Databricks or a managed MLflow service), the Model Registry supports governance requirements critical for enterprise-grade ML operations.

| Concept | Description |
|---------|-------------|
| **Model** | An MLflow Model is created using a flavor’s ``mlflow.<model_flavor>.log_model()`` method or ``mlflow.create_external_model()`` (since MLflow 3). Once logged, it can be registered with the Model Registry. |
| **Registered Model** | A named entity in the registry. Contains versions, aliases, tags, and metadata. Serves as a container for all versions of a particular model. |
| **Model Version** | Each registered model can have multiple versions. The first registered model is version 1, and subsequent registrations increment the version number. Versions can be tagged for tracking (e.g., ``pre_deploy_checks: ``"PASSED"``). |
| **Model URI** | A standardized reference to models. Format: ``models:/<model-name>/<model-version>``. Example: ``models:/MyModel/1``. |
| **Model Alias** | A mutable pointer to a specific version. Example: ``models:/MyModel@champion``. Aliases allow flexible deployment by reassigning them to different versions without changing code. |
| **Tags** | Key-value metadata for models and versions. Example: ``task:question-answering`` at the model level, or ``validation_status:approved`` at the version level. Useful for categorization and tracking. |
| **Annotations & Descriptions** | Markdown-based documentation attached to models or versions. Can include methodology, datasets used, algorithm details, or deployment notes to aid collaboration. |