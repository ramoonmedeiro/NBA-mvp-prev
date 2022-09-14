import gradio as gr
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler

def previsao(GP, MIN, PTS, AST, REB, FG, FT):
	model = joblib.load('modelo.pkl')
	X_treino = joblib.load('X_treino.pkl')

# Normalizando variáveis
	norm = MinMaxScaler()
	norm.fit(X_treino)

	val = np.array([GP, MIN, PTS, AST, REB, FG, FT]).reshape(1,-1)
	X_val_norm = norm.transform(val)
	prev = model.predict_proba(X_val_norm)

	return {"MVP%": prev[0][1]}

demo = gr.Interface(fn=previsao,
					inputs=["number",
					"number",
					"number",
					"number",
					"number",
					"number",
					"number"], outputs="label")

demo.launch()
