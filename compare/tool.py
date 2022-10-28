import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os


def scrape():
	servico = Service(GeckoDriverManager().install())
	navegador = webdriver.Firefox(service=servico)

	url = f'https://www.nba.com/stats/players/traditional?sort=PTS&dir=-1&Season=2022-23&SeasonType=Regular+Season'
	navegador.get(url)
	sleep(7)
	element = navegador.find_element(By.XPATH, "//div[@class='Crom_base__f0niE']")
	#element = navegador.find_element(By.XPATH, "//div[@class='nba-stat-table']") new name to <div><table>
	html = element.get_attribute('outerHTML')
	bs = BeautifulSoup(html, 'html.parser')
	table = bs.find(name='table')


	df = pd.read_html(str(table))[0]
	del df['Unnamed: 0']
	df_full = df[['Player', 'Min', 'PTS', 'AST', 'REB', 'FG%', 'FT%']].head(50).copy()
	df_full.to_csv(f'prever.csv', index=False)

	navegador.quit()

	return

def results(modelo):
	df = pd.read_csv('./prever.csv')
	names = df['Player']
	X_prev = df.drop(['Player'], axis=1)


	# Realizando a predição
	pred = modelo.predict_proba(X_prev)

	# guardando valores
	d = {}
	for player, proba in zip(names, pred):
		d[round(proba[1]*100, 2)] = player

	val = sorted(d, reverse=True)

	for i in range(0, 10, 1):
		print(f'{i+1} - {d[val[i]]}')

	

	return
	