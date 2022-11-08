import gradio as gr
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

def previsao(PTS, AST, REB, FG, FT, RATE_WIN):
	model = joblib.load('model-best.pkl')

	val = np.array([PTS, AST, REB, FG, FT, RATE_WIN]).reshape(1,-1)
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
