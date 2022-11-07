# Manipulação de dados e números
import pandas as pd
import numpy as np


# Libs do sklearn
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
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
def testes(X_treino, y_treino, k, modelos, scalers, scoring):

        for i in range(k, 0, -1):
            for scaler in scalers:
                for modelo in modelos:
                    mlflow.set_experiment('MELHORES')
                    with mlflow.start_run():

                        pipe = Pipeline(steps=[
                            ('select', SelectKBest(chi2, k=i)),
                            ('scaler', scaler),
                            ('model', modelo)
                        ])
                        skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=99)
                        resultados = cross_val_score(pipe, X_treino, y_treino, cv=skfold, scoring=scoring)
                        mlflow.log_metric('Recall', round(resultados.mean()*100,2))
                        mlflow.sklearn.log_model(pipe, 'modelo')
                    mlflow.end_run()