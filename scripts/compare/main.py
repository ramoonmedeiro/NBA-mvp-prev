import tool
import joblib

modelo = joblib.load('../deploy/modelo-versao2.pkl')

tool.scrape()

tool.results(modelo)