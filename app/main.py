"""Esse módulo contém a definição de API.
"""
from fastapi import FastAPI

from model import Model
from schemas import ModelInfo, Prediction, PredictionRequest

app = FastAPI()
model = Model()


@app.post("/predict")
def predict(request: PredictionRequest) -> Prediction:
    """Endpoint para realizar predições com o modelo.

    Args:
        request (PredictionRequest): parâmetros de predição.

    Returns:
        Prediction: resultado.
    """
    return model.predict(request)


@app.get("/info")
def info() -> ModelInfo:
    """Endpoint para obter informações (meta-dados) do modelo.

    Returns:
        ModelInfo: informações do modelo.
    """
    return model.info()
