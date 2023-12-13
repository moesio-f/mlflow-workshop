"""
"""
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """Essa classe representa uma solicitação
    de predição/avaliação do modelo para um 
    conjunto de entrada.
    """
    input_features: list[list[float]]


class Prediction(BaseModel):
    """Essa classe representa a resposta
    produzida pela API contendo as predições
    do modelo para uma dada entrada.
    """
    request: PredictionRequest
    output: list[int]


class ModelInfo(BaseModel):
    """Essa classe representa o conjunto
    de informações sobre o modelo utilizado
    pela API.
    """
    experiment_name: str
    experiment_id: str
    run_name: str
    run_id: str
    m_name: str
    m_metrics: dict
    m_params: dict
