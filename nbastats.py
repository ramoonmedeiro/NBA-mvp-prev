import pandas as pd
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
	    df_full = df[['PLAYER', 'TEAM', 'AGE', 'GP', 'MIN', 'PTS', 'AST', 'REB', 'FG%', '3P%', 'FT%']].head(50).copy()
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
    df_full = df.iloc[2:28]
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

    # Mudando as posições para as 5 poisções originais
    df_full.loc[[2, 3, 15, 18, 23, 25],'POS'] = 'PF'
    df_full.loc[[4, 14, 24], 'POS'] = 'SG'
    df_full.loc[[5, 6, 7],'POS'] = 'PG'
    df_full.loc[[8, 9],'POS'] = 'SF'

    df_full.to_csv('./datasets/mvps.csv', index=False)

    return

#def add_players():

	# Inserindo Steve Nash no TOP 10 na temporada de 2004-05
#	df = pd.read_csv('./2004-05.csv')
#	df.drop(9)
#	df.loc[9]=['Steve Nash', 'PHX', 31, 75, 34.3, 15.5, 11.5, 3.3, 50.2, 43.1, 88.7, 2005]
#	df.to_csv('./2004-05.csv', index=False)

	# Inserindo Steve Nash no TOP 10 na temporada de 2005-06
#	df = pd.read_csv('./2005-06.csv')
#	df.drop(9)
#	df.loc[9]=['Steve Nash', 'PHX', 32, 79, 35.4, 18.8, 10.5, 4.2, 51.2, 43.9, 92.1, 2006]
#	df.to_csv('./2005-06.csv', index=False)

	# Inserindo Steve Nash no TOP 10 na temporada de 2005-06
#	df = pd.read_csv('./2006-07.csv')
#	df.drop(9)
#	df.loc[9]=['Dirk Nowitzki', 'DAL', 29, 78, 36.2, 24.6, 3.4, 8.9, 50.2, 41.6, 90.4, 2007]
#	df.to_csv('./2006-07.csv', index=False)

	# Inserindo Nikola Jokic no TOP 10 na temporada de 2020-21
#	df = pd.read_csv('./2020-21.csv')
#	df.drop(9)
#	df.loc[9]=['Nikola Jokic', 'DEN', 26, 72, 34.6, 26.4, 8.3, 10.8, 56.6, 38.8, 86.8, 2021]
#	df.to_csv('./2020-21.csv', index=False)

#	return

def add_mvp_param():

	seasons = ['2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14',
          	   '2012-13', '2011-12', '2010-11', '2009-10', '2008-09', '2007-08', '2006-07', '2005-06', '2004-05',
          	   '2003-04', '2002-03', '2001-02', '2000-01', '1999-00', '1998-99', '1997-98', '1996-97']

	df_mvps = pd.read_csv('./datasets/mvps.csv')
	mvps = list(df_mvps['PLAYER'])
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
