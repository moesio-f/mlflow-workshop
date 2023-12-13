"""Esse módulo contém as configurações necessárias
para execução da API.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Essa classe é utilizada para
    obtenção das credenciais do MlFlow.

    Valores padrão:
    - CELERY_BROKER_URL é amqp://guest:guest@localhost:5672//
    - CELERY_RESULT_BACKEND é rpc://
    """
    MLFLOW_TRACKING_URI: str
    MLFLOW_TRACKING_USERNAME: str
    MLFLOW_TRACKING_PASSWORD: str
    MODEL_SAVE_DIRECTORY: str = 'model'


settings = Settings()
