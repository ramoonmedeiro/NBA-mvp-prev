import nbastats

# Pega as tabelas do site oficial da nba
#nbastats.all_time()

# Pega a tabela de mvps da temporada regular do site oficial da ESPN
nbastats.mvps()

# Insere o jogador Steve Nash no top 10 para os anos 2004-2006, Jokic no ano de 2020-2021 e Nowitzki em 2007
#nbastats.add_players()

# Adicionando uma coluna de MVP para resultado final
nbastats.add_mvp_param()

# Concatena todas as tabela em uma só e exclui as outras 26
nbastats.concat()
