"""Esse módulo define o modelo utilizado pela
API.
"""
from pathlib import Path

import numpy as np
import mlflow
import mlflow.entities

from schemas import ModelInfo, Prediction, PredictionRequest
from settings import settings


class Model:
    """Essa classe representa o modelo manipulado
    pela API.
    """

    def __init__(self) -> None:
        """Inicializa o modelo, obtendo as informações
        relativas à sua run e experimento.
        """
        # Informações do experimento que contém
        #   o modelo que vamos utilizar.
        self._run_id = '1b93978f384b4be5b369c2b5edee2612'
        run = mlflow.get_run(self._run_id)
        run_info: mlflow.entities.RunInfo = run.info
        run_data: mlflow.entities.RunData = run.data

        # Conseguimos obter as demais informações automaticamente
        self._run_name = run_info.run_name
        self._experiment_id = run_info.experiment_id
        self._experiment_name = mlflow.get_experiment(self._experiment_id).name

        # Agora, definimos as informações do modelo
        self._model_name = 'extra_trees'

        # Conseguimos obter os parâmetros e métricas diretamente da run
        self._model_metrics = run_data.metrics
        self._model_params = run_data.params

        # Carregamento e salvamento do modelo no sistema de arquivos local
        self._save_path = Path(settings.MODEL_SAVE_DIRECTORY)
        self._save_path.mkdir(exist_ok=True, parents=True)
        self._model = mlflow.sklearn.load_model(f'runs:/{self._run_id}/{self._model_name}',
                                                dst_path=str(self._save_path))

    def predict(self, request: PredictionRequest) -> Prediction:
        """Recebe uma solicitação de predição, e retorna
        os resultados da avaliação do modelo nas features
        de entrada.

        Args:
            input (PredictionRequest): solicitação de predição.

        Returns:
            Prediction: resultado da avaliação.
        """
        features = request.input_features
        output = self._model.predict(features).tolist()
        return Prediction(request=request, output=output)

    def info(self) -> ModelInfo:
        """Retorna meta-dados e informações 
        sobre o modelo.

        Returns:
            ModelInfo: informações do modelo.
        """
        return ModelInfo(experiment_name=self._experiment_name,
                         experiment_id=self._experiment_id,
                         run_name=self._run_name,
                         run_id=self._run_id,
                         m_name=self._model_name,
                         m_metrics=self._model_metrics,
                         m_params=self._model_params)
