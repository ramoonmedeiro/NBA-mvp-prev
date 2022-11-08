# Manipulação de dados e números
import pandas as pd
import numpy as np

# Libs do sklearn
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline

# MLFlow
import mlflow
import mlflow.sklearn


# Iniciando modelo baseline

class Baseline():

    def __init__(self, X_treino, y_treino, k, modelos, scalers, scoring, name):
        self.X_treino = X_treino
        self.y_treino = y_treino
        self.k = k
        self.modelos = modelos
        self.scalers = scalers
        self.scoring = scoring
        self.name = name


    def testes(self):
        for i in range(self.k, 0, -1):
            for scaler in self.scalers:
                for modelo in self.modelos:
                    mlflow.set_experiment(f'{self.name}')
                    with mlflow.start_run():

                        pipe = Pipeline(steps=[
                            ('select', SelectKBest(chi2, k=i)),
                            ('scaler', scaler),
                            ('model', modelo)
                        ])
                        skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=99)
                        resultados = cross_val_score(pipe, self.X_treino, self.y_treino, cv=skfold, scoring=self.scoring)
                        mlflow.log_metric('Recall', round(resultados.mean()*100,2))
                        mlflow.sklearn.log_model(pipe, 'modelo')
                    mlflow.end_run()

class Melhores(Baseline):

    def __init__(self, X_treino, y_treino, k, modelos, scalers, scoring, name):
        super().__init__(X_treino, y_treino, k, modelos, scalers, scoring, name)


class Otimizacao():

    def __init__(self, X_treino, y_treino, modelo, params, scoring):
        self.X_treino = X_treino
        self.y_treino = y_treino
        self.modelo = modelo
        self.params = params
        self.scoring = scoring

    def opt(self):
        pipe_best = self.modelo

        skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=99)
        pipe_grid = GridSearchCV(self.modelo, self.params , scoring=self.scoring, cv=skfold)
        pipe_grid.fit(self.X_treino, self.y_treino)

        # Apresentado resultados
        print(pipe_grid.best_params_)
        print(pipe_grid.best_score_)