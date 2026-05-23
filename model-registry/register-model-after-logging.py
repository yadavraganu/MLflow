from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment("register-model-after-logging-exp")
with mlflow.start_run(run_name="register-model-after-logging-run") as run:
    X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    params = {"max_depth": 2, "random_state": 42}
    model = RandomForestRegressor(**params)
    model.fit(X_train, y_train)

    # Log parameters and metrics using the MLflow APIs
    mlflow.log_params(params)

    y_pred = model.predict(X_test)
    mlflow.log_metrics({"mse": mean_squared_error(y_test, y_pred)})

    # Log the sklearn model
    mlflow.sklearn.log_model(
        sk_model=model,
        name="sklearn-model-after-logging",
        input_example=X_train,
    )

    mlflow.register_model(
        model_uri=f"runs:/{run.info.run_id}/sklearn-model-after-logging",
        name="sk-learn-random-forest-reg-model-after-logging"
        )