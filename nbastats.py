import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os


def all_time():
    servico = Service(GeckoDriverManager().install())
    navegador = webdriver.Firefox(service=servico)

    year = 2022
    seasons = ['2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14',
          		'2012-13', '2011-12', '2010-11', '2009-10', '2008-09', '2007-08', '2006-07', '2005-06', '2004-05',
          		'2003-04', '2002-03', '2001-02', '2000-01', '1999-00', '1998-99', '1997-98', '1996-97']


    for season in seasons:
	    url = f'https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season={season}&SeasonType=Regular%20Season'	
	    navegador.get(url)
	    sleep(7)
	    element = navegador.find_element(By.XPATH, "//div[@class='nba-stat-table']")
	    html = element.get_attribute('outerHTML')
	    bs = BeautifulSoup(html, 'html.parser')
	    table = bs.find(name='table')

    # pandas step

	    df = pd.read_html(str(table))[0]
	    del df['Unnamed: 0']
	    df_full = df[['PLAYER', 'TEAM', 'AGE', 'GP', 'MIN', 'PTS', 'AST', 'REB', 'FG%', '3P%', 'FT%']].head(20).copy()
	    df_full['YEAR'] = year
	    df_full.to_csv(f'{season}.csv', index=False)
	    year -= 1

    navegador.quit()

    return


def mvps():
    
    servico = Service(GeckoDriverManager().install())
    navegador = webdriver.Firefox(service=servico)

    url = 'http://www.espn.com/nba/history/awards/_/id/33'
    navegador.get(url)
    sleep(10)
    element = navegador.find_element(By.XPATH, "//table[@class='tablehead']")
    html = element.get_attribute('outerHTML')
    bs = BeautifulSoup(html, 'html.parser')
    table = bs.find(name='table')
    navegador.close()

    # pandas step

    df = pd.read_html(str(table))[0]
    df.columns = ['YEAR', 'PLAYER', 'POS', 'TEAM', 'FG%', 'PPG', 'RPG', 'APG', 'BLKPG', 'DEL']
    df_full = df.iloc[2:69]
    df_full.reset_index(drop=True, inplace=True)
    del df_full['DEL']

    # Tranformando em numeros os objects
    df_full['YEAR'] = pd.to_numeric(df_full['YEAR'], errors='coerce')
    df_full['FG%'] = pd.to_numeric(df_full['FG%'], errors='coerce')
    df_full['RPG'] = pd.to_numeric(df_full['RPG'], errors='coerce')
    df_full['APG'] = pd.to_numeric(df_full['APG'], errors='coerce')
    df_full['BLKPG'] = pd.to_numeric(df_full['BLKPG'], errors='coerce')

    # FG * 100
    df_full.loc[:, 'FG%'] = df_full.loc[:, 'FG%']*100

    # Mudando as posições para as 5 posições originais
    df_full.loc[[2, 3, 15, 18, 23, 25, 29],'POS'] = 'PF'
    df_full.loc[[4, 14, 24, 26, 30, 31, 34], 'POS'] = 'SG'
    df_full.loc[[5, 6, 7, 32, 33, 35, 58, 65],'POS'] = 'PG'
    df_full.loc[[8, 9, 36, 37, 38, 41],'POS'] = 'SF'
    df_full.loc[[42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 66], 'POS'] = 'C'

    df_full.to_csv('./datasets/mvps.csv', index=False)

    return

def add_steve_nash():

	#Inserindo Steve Nash no TOP 10 na temporada de 2004-05 e 2005-06
	df = pd.read_csv('./2004-05.csv')
	df.drop(19)
	df.loc[19]=['Steve Nash', 'PHX', 31, 75, 34.3, 15.5, 11.5, 3.3, 50.2, 43.1, 88.7, 2005]
	df.to_csv('./2004-05.csv', index=False)

	df = pd.read_csv('./2005-06.csv')
	df.drop(19)
	df.loc[19]=['Steve Nash', 'PHX', 32, 79, 35.4, 18.8, 10.5, 4.2, 51.2, 43.9, 92.1, 2006]
	df.to_csv('./2005-06.csv', index=False)

	return

def add_mvp_param():

	seasons = ['2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14',
          	   '2012-13', '2011-12', '2010-11', '2009-10', '2008-09', '2007-08', '2006-07', '2005-06', '2004-05',
          	   '2003-04', '2002-03', '2001-02', '2000-01', '1999-00', '1998-99', '1997-98', '1996-97']

	df_mvps = pd.read_csv('./datasets/mvps.csv')
	df_copy_mvps = df_mvps.loc[0:25].copy()
	mvps = list(df_copy_mvps['PLAYER'])
	for i in range(len(mvps)):
	    df = pd.read_csv(f'./{seasons[i]}.csv')
	    df['MVP'] = df['PLAYER'].apply(lambda linha: 1 if linha == mvps[i] else 0)
	    df.to_csv(f'./{seasons[i]}.csv', index=False)

	return 


def concat():

	df1 = pd.read_csv('./1996-97.csv')
	df2 = pd.read_csv('./1997-98.csv')
	df3 = pd.read_csv('./1998-99.csv')
	df4 = pd.read_csv('./1999-00.csv')
	df5 = pd.read_csv('./2000-01.csv')
	df6 = pd.read_csv('./2001-02.csv')
	df7 = pd.read_csv('./2002-03.csv')
	df8 = pd.read_csv('./2003-04.csv')
	df9 = pd.read_csv('./2004-05.csv')
	df10 = pd.read_csv('./2005-06.csv')
	df11 = pd.read_csv('./2006-07.csv')
	df12 = pd.read_csv('./2007-08.csv')
	df13 = pd.read_csv('./2008-09.csv')
	df14 = pd.read_csv('./2009-10.csv')
	df15 = pd.read_csv('./2010-11.csv')
	df16 = pd.read_csv('./2011-12.csv')
	df17 = pd.read_csv('./2012-13.csv')
	df18 = pd.read_csv('./2013-14.csv')
	df19 = pd.read_csv('./2014-15.csv')
	df20 = pd.read_csv('./2015-16.csv')
	df21 = pd.read_csv('./2016-17.csv')
	df22 = pd.read_csv('./2017-18.csv')
	df23 = pd.read_csv('./2018-19.csv')
	df24 = pd.read_csv('./2019-20.csv')
	df25 = pd.read_csv('./2020-21.csv')
	df26 = pd.read_csv('./2021-22.csv')

	df = pd.concat([df26, df25, df24, df23, df22, df21, df20, df19, df18, df17, 
           df16, df15, df14, df13, df12, df11, df10, df9, df8, df7, 
           df6, df5, df4, df3, df2, df1], ignore_index=True)

	df.to_csv(f'./datasets/stats-full.csv', index=False)

	# Apagando todos as tabelas
	os.system('rm 19* 20*')

	return

def old_mvps():
	df_mvps = pd.read_csv('./datasets/mvps.csv')
	df_old = df_mvps.loc[26:].copy()

# Inserindos valores NaN
	df_old['PPG'] = np.where(df_old['PPG'] == 'No stats available.', np.nan, np.nan)

# Inserindo siglas npos times
	times_unicos = list(df_old['TEAM'].unique())
	siglas = ['CHI', 'SAS', 'HOU', 'PHX', 'LAL', 'BOS', 'PHI', 'POR', 'LAC', 'MIL', 'NYK', 'WAS', 'SAC', 'GSW', 'ATL']

	df_old['TEAM'] = df_old['TEAM'].replace(times_unicos, siglas)

	# Inserindo dados faltantes. Créditos ao site statsmuse ( que possui todos os dados de MVP que eu necessitava )
	gp = [82, 81, 80, 76, 80, 82, 79, 77, 82, 80, 82, 80, 79, 78, 81, 82, 82, 82, 58, 82, 82, 82, 81, 82, 81, 82, 81, 82, 82, 81, 79, 78, 79, 78, 76, 78, 72, 72, 69, 64, 72]
	mins = [37.7, 38.0, 41.0, 37.6, 38.8, 37.0, 37.2, 37.5, 40.4, 36.3, 38.0, 39.5, 38.3, 37.5, 42.0, 35.0, 38.3, 41.3, 33.3, 36.8, 41.2, 43.2, 43.8, 41.8, 44.2, 40.1, 38.1, 36.2, 46.8, 45.5, 47.3, 44.4, 45.1, 44.9, 45.2, 44.3, 46.4, 39.9, 38.3, 36.9, 38.8]
	pts = [30.4, 27.6, 27.3, 25.6, 30.1, 31.5, 22.3, 22.5, 35.0, 23.9, 25.8, 28.7, 24.2, 24.5, 31.1, 24.6, 24.8, 24.8, 18.9, 26.2, 27.7, 34.5, 27.0, 20.5, 34.8, 31.7, 21.7, 13.8, 24.3, 24.1, 33.5, 14.1, 31.4, 16.8, 18.9, 16.9, 37.6, 29.2, 16.6, 20.6, 25.7]
	ast = [4.3, 2.9, 3.6, 5.1, 6.1, 5.5, 11.5, 12.8, 5.9, 12.2, 6.8, 6.6,  6.6, 1.3, 1.8, 4.4, 4.5, 1.8, 5.0, 3.9, 5.0, 2.2, 4.8, 4.1, 4.6, 3.3, 2.0, 2.6, 8.6, 7.8, 5.2, 5.3, 11.0, 4.5, 4.5, 3.4, 2.3, 3.1, 2.9, 7.5, 2.6]
	reb = [6.6, 10.8, 11.9, 12.2, 6.4, 6.0, 6.6, 7.9, 5.5, 6.3, 9.8, 10.5, 10.1, 15.3, 14.7, 8.0, 10.8, 17.6, 13.2, 13.3, 16.9, 14.1, 14.5, 16.2, 16.6, 16.0, 13.9, 18.2, 23.8, 24.2, 24.6, 24.1, 9.9, 23.6, 23.6, 23.9, 27.0, 16.4, 22.7, 4.8, 16.2]
	fg = [49.5, 53.0, 52.8, 52.0, 51.9, 53.9, 48.0, 50.9, 53.5, 52.2, 49.6, 52.2, 49.2, 50.1, 51.9, 52.1, 60.4, 54.0, 52.2, 57.9, 52.9, 51.2, 53.9, 45.2, 57.4, 57.7, 50.7, 47.6, 59.5, 68.3, 54.0, 43.8, 48.3, 43.2, 45.7, 42.6, 46.1, 43.8, 44.2, 37.8, 42.9]
	p3 = [42.7, 30.0, 42.1, 30.5, 27.0, 31.2, 38.4, 31.4, 13.2, 20.5, 42.3, 42.7, 24.7, 0.0, 0.0, 22.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	ft = [83.4, 77.4, 71.6, 76.5, 83.2, 85.1, 89.0, 91.1, 84.1, 84.8, 89.6, 88.2, 88.8, 76.1, 76.2, 78.7, 76.5, 73.9, 72.0, 70.1, 70.3, 80.5, 70.2, 77.9, 68.9, 69.0, 75.6, 60.5, 38.0, 44.1, 51.3, 57.3, 85.3, 55.5, 59.5, 55.0, 58.2, 75.9, 51.9, 82.1, 73.6]
	ano = df_old['YEAR']

	df_old['MVP'] = 1
	df_old.drop(['YEAR', 'FG%', 'PPG', 'RPG', 'APG', 'BLKPG', 'POS'], axis = 1 , inplace=True)

	df_old.insert(2, 'GP', gp)
	df_old.insert(3, 'MIN', mins)
	df_old.insert(4, 'PTS', pts)
	df_old.insert(5, 'AST', ast)
	df_old.insert(6, 'REB', reb)
	df_old.insert(7, 'FG%', fg)
	df_old.insert(8, '3P%', p3)
	df_old.insert(9, 'FT%', ft)
	df_old.insert(10, 'YEAR', ano)

	df_old.to_csv(f'./datasets/old.csv', index=False)

def concat_old_new():

	# Carregando os dados
	df_old = pd.read_csv('./datasets/old.csv')
	df_new = pd.read_csv('./datasets/stats-full.csv')

	# Excluindo coluna que não é necessária neste primeiro momento
	df_new.drop('AGE', axis=1, inplace = True)

	# Concatenando todos os dados
	df_final = pd.concat([df_new, df_old], ignore_index=True)

	# Tabela final
	df_final.to_csv(f'./datasets/stats-full.csv', index=False)