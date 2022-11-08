import gradio as gr
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

def previsao(MIN, RATE_WIN , PTS, AST, REB, FG, FT):
	model = joblib.load('model-best.pkl.pkl')

	val = np.array([MIN, RATE_WIN, PTS, AST, REB, FG, FT]).reshape(1,-1)
	prev = model.predict_proba(val)

	return {"Chances de ser MVP": prev[0][1]}

demo = gr.Interface(fn=previsao,
					inputs=["number",
					"number",
					"number"
					"number",
					"number",
					"number",
					"number"], outputs="label")

demo.launch()
