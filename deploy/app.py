import gradio as gr
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

def previsao(MIN, PTS, AST, REB, FG, FT):
	model = joblib.load('modelo-versao2.pkl')

	val = np.array([MIN, PTS, AST, REB, FG, FT]).reshape(1,-1)
	prev = model.predict_proba(val)

	return {"Chances de ser MVP": prev[0][1]}

demo = gr.Interface(fn=previsao,
					inputs=["number",
					"number",
					"number",
					"number",
					"number",
					"number"], outputs="label")

demo.launch()
