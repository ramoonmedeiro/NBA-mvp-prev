import results
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold

# Modelos e scalers

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# MLFlow
import mlflow
import mlflow.sklearn

# Carregando base
df = pd.read_csv('../../datasets/stats-full.csv')

# Escolhendo as features desejadas
X = df.drop(['Player', 'Team', 'GP', 'YEAR', '3P%', 'MVP'], axis=1)
y = df['MVP']

# Separação entre treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=99)

# Definição dos modelos e scalers
modelos = [LogisticRegression(), SVC(probability=True), KNeighborsClassifier(), GaussianNB(), DecisionTreeClassifier(), RandomForestClassifier()]
modelos_balanced = [LogisticRegression(class_weight='balanced'), SVC(probability=True, class_weight='balanced'), DecisionTreeClassifier(class_weight='balanced'), RandomForestClassifier(class_weight='balanced')]
scalers = [StandardScaler(), MinMaxScaler()]

# Iniciando experimento com mlflow e executando funções

mlflow.set_experiment('baseline')

with mlflow.start_run():

    resultados = results.testes(k = 7, modelos = modelos, scalers = scalers, scoring = 'recall')

    # registrando métrica
    mlflow.log_metric('Recall', resultados)

mlflow.end_run()