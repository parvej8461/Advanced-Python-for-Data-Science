'''
MLOps Integration
Experiment Tracking with MLflow
Track experiments for reproducibility.
'''

import mlflow
from sklearn.linear_model import LogisticRegression

with mlflow.start_run():
    model = LogisticRegression(C=1.0)
    model.fit(X_train, y_train)
    mlflow.log_param("C", 1.0)
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
    mlflow.sklearn.log_model(model, "model")


'''
Model Deployment with FastAPI
Serve models as APIs.
'''   
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load('model.pkl')

@app.post("/predict")
async def predict(data: dict):
    X = [data['features']]
    return {"prediction": model.predict(X).tolist()}