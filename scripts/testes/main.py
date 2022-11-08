# Lib criada
from results import Baseline, Melhores, Otimizacao

# Manipulação de dados
import pandas as pd

# Joblib lib
import joblib

# Separação entre treino e teste
from sklearn.model_selection import train_test_split

# Modelos e scalers
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Carregando base
df = pd.read_csv('../../datasets/stats-full.csv')

# Escolhendo as features desejadas
X = df.drop(['Player', 'Min', 'Team', 'GP', 'YEAR', '3P%', 'MVP'], axis=1)
y = df['MVP']

# Separação entre treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.4, random_state=99)

# Definição dos modelos e scalers
modelos = [LogisticRegression(), SVC(probability=True), KNeighborsClassifier(), 
            GaussianNB(), DecisionTreeClassifier(), RandomForestClassifier()]

# Mdoelos com melhores desempenhos com hiperparametros default.
modelos_balanced = [SVC(probability=True, class_weight='balanced'), DecisionTreeClassifier(class_weight='balanced'), 
                    RandomForestClassifier(class_weight='balanced')]

scalers = [StandardScaler(), MinMaxScaler()]

# Instanciação e armazenando informações com o MLFlow
baseline = Baseline(X_treino, y_treino, k = 6, modelos = modelos, scalers = scalers, scoring = 'recall', name='Baseline')
best = Melhores(X_treino, y_treino, k = 6, modelos = modelos_balanced, scalers = scalers, scoring = 'recall', name='Melhores') 
baseline.testes()
best.testes()


# Carregando o melhor modelo com hiperparametros default

modelo = joblib.load('model.pkl')

# Etapa de otimização com GridSearchCV

params = { 
    'model__C': [0.01, 1, 10, 100, 1000],  
   'model__gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
   'model__kernel': ['rbf','linear','sigmoid']
}


# Instaciacao
grid = Otimizacao(X_treino, y_treino, modelo = modelo, params = params, scoring = 'recall')

#Apresentado melhores parametros e resultado.
grid.opt()