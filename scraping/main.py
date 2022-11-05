import nbastats

# Pega as tabelas do site oficial da nba
nbastats.all_time()

# Pega tabels de wins rate de cada para cada temporada da nba
nbastats.wins_rate()

# Pega a tabela de mvps da temporada regular do site oficial da ESPN
nbastats.mvps()

# Insere o jogador Steve Nash no top 10 para o ano de 2005
nbastats.add_steve_nash()

# Adicionando uma coluna de MVP para resultado final
nbastats.add_mvp_param()

# Adicionando win rate para cada player
#nbastats.add_wins_rate()

# Concatena todas as tabela em uma só e exclui as outras 26
nbastats.concat_players()

# Concatena wins rates para cada season
nbastats.concat_wins_seasons()

# Adicionando o restante dos MVPs na tabela principal
nbastats.old_mvps()

# Finalizando a limpeza de dados
#nbastats.concat_old_new()