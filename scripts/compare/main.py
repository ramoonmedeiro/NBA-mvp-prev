import tool
import joblib

modelo = joblib.load('../../deploy/model-best.pkl')

tool.scrape()

tool.results(modelo)