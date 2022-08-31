# Introdução

Em 1946, era criada a Associação Americana de Basquetebol (ABA), organização na qual se tornou a Associação Nacional de Basquetebol (NBA) 3 anos depois.
Com o seu sucesso e longevidade, a NBA se tornou uma das ligas mais conhecidas e apreciadas no mundo todo. Uma parte desse sucesso é devido aos momentos únicos e emocionantes que apenas a NBA proporciona. Mas grande parte do brilho da NBA é devido aos jogadores, que se tornaram lendários, 
como Michael Jordan, Kobe Bryant, Lebron James e etc. 
		
E assim como na maioria dos esportes, todo final de temporada um jogador é eleito o jogador mais valioso da liga ou MVP (<i>Most Valuable Player</i>),
sendo tal prêmio visto como um dos parâmetros para avaliar se um jogador vai ser maior do que outros. É evidente que não é qualquer jogador 
que irá ser premiado com o MVP, poucos jogadores conseguem tal feito, mais raro ainda são os jogadores que vencem múltiplas vezes o tão glorioso prêmio. O motivo de um jogador ser agraciado com o prêmio de MVP, difere em alguns fatores, como pontos por jogo, assistências por jogo, rebotes por jogo, se um jogador é um líder em quadra ou não e assim por diante, não só atributos individuais, mas dependendo também do desempenho que seu time possui numa dada temporada. 

# Objetivos

Como visto acima, diversos fatores contribuem para um jogador da NBA ser eleito o MVP da temporada regular, portanto, este projeto visa criar um algoritmo de classificação com a intenção de prever o vencedor do mvp nas temporadas seguintes. Testarei diversos algoritmos supervisionados para 
realizar a predição. 
	
Os dados foram extraídos por mim, utilizando os scripts <i>main.py</i> e <i>nbastats.py</i> de minha autoria. Os mesmos scripts já possuem um tratamento 
de dados na qual agiliza os processos seguintes. Os algoritmos de machine Learning e avaliação dos mesmos serão todos executados 
utilizando o Scikit-Learn.

# Análise e Exploração dos Dados

Para compreender quais features podem ser determinantes para obter resultados ótimo nos algoritmos, é realizada uma análise dos dados.

Uma possível feature que pode ser importante para inserir no algoritmo são, os times que os jogadores jogam, com isso, vamos analisar os times com mais MVPs da temporada regular na história da NBA. Os times com mais jogadores vencedores do prêmio de MVP é a franquia do Boston Celtics. A Figura abaixo mostra as cinco franquias com mais vencedores do prêmio.

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/184778671-4e6a71a6-3482-42f0-9f14-a6d3ccee16bf.png" width="450px" />
</div>

Daqui, já podemos dizer que estatísticamente um jogador tem mais chances de ser MVP se jogar pelo time do Boston Celtics do que pelo Denver Nuggets, porém, é claro que tal afirmação é extremamente rude, já que a última vez que um jogador foi MVP da temporada regular vestindo a camisa do Boston foi em 1986 com Larry Bird, enquanto os últimos dois MVPs (2021 e 2022) foi dado ao jogador Nikola Jokic, que venceu a dobradinha vestindo a camisa do Denver Nuggets. Logo, o time não pode ser um fator tão relevante para a previsão de um jogador ser ou não ser MVP da NBA.

A Tabela abaixo mostra o número de vezes que cada time teve um jogador MVP pela temporada regular da NBA.

<table class="tg", align="center">
<thead>
  <tr>
    <th class="tg-7btt">Franquias<br></th>
    <th class="tg-7btt">MVPs</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Boston Celtics</td>
    <td class="tg-c3ow">10<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Los Angeles Lakers</td>
    <td class="tg-c3ow">8<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Chicago Bulls,<br>Philadelphia 76ers</td>
    <td class="tg-c3ow">6<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Milwaukee Bucks</td>
    <td class="tg-c3ow">5<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Houston Rockets</td>
    <td class="tg-c3ow">4<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Golden State Warriors,<br>Phoenix Suns,<br>San Antonio Spurs</td>
    <td class="tg-c3ow">3</td>
  </tr>
  <tr>
    <td class="tg-baqh">Atlanta Hawks,<br>Cleveland Cavaliers,<br>Denver Nuggets,<br>Miami Heat,<br>Oklahoma City Thunder,<br>Utah Jazz</td>
    <td class="tg-baqh">2</td>
  </tr>
  <tr>
    <td class="tg-baqh">Dallas Mavericks,<br>Los Angeles Clippers,<br>Minnesota Timberwolves,<br>New York Knicks,<br>Portland Trail Blazers,<br>Sacramento Kings,<br>Washigton Wizards</td>
    <td class="tg-baqh">1</td>
  </tr>
</tbody>
</table>

Como dito anteriormente, alguns jogadores conseguiram realizar a façanha de ganhar múltiplas vezes o prêmio de MVP da NBA, um deles é o astro Giannis Antetokounmpo, que venceu 2 vezes seguidas (2019 e 2020), outro exemplo, mais raro ainda é o do jogador Michael Jordan, considerado o melhor jogador de basquetebol de todos os tempos, que possui 5 prêmios de MVP (1988, 1991, 1992, 1996 e 1998).

Na Figura abaixo é apresentado os 5 maiores vencedores do MVP da temporada regular da NBA. Kareem-Abdul-Jabbar ganhou 6 MVPs, sendo o seu último conquistado no ano de 1980, desde lá, ninguém conseguiu superar tal marca. 
	
<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/184779118-4de88b98-8631-4686-930c-ee7ed11a08be.png" width="600px" />
</div>

A Tabela abaixo mostra todos os jogadores que já venceram o prêmio de MVP da temporada regular da NBA.

Concluí-se que o nome do jogador neste caso não importaria tanto para utilizarmos como atributo relevante para criarmos o nosso modelo de machine learning, já que qualquer jogador pode se superar em uma temporada e conseguir se tornar o melhor jogador da liga. Não é o nome em si, mas sim os seus números nos fundamentos do jogo que importam para um atleta ser eleito MVP.

<table class="tg", align="center">
<thead>
  <tr>
    <th class="tg-7btt">Jogador</th>
    <th class="tg-7btt">MVPs</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Kareem Abdul-Jabbar</td>
    <td class="tg-c3ow">6</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Bill Russell,<br>Michael Jordan<br></td>
    <td class="tg-c3ow">5</td>
  </tr>
  <tr>
    <td class="tg-c3ow">LeBron James,<br>Wilt Chamberlain<br></td>
    <td class="tg-c3ow">4</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Larry Bird,<br>Magic Johnson,<br>Moses Malone</td>
    <td class="tg-c3ow">3</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Bob Pettit,<br>Giannis Antetokounmpo,<br>Karl Malone,<br>Nikola Jokic,<br>Steve Nash,<br>Stephen Curry,<br>Tim Duncan</td>
    <td class="tg-c3ow">2</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Allen Iverson,<br>Bill Walton,<br>Bob Cousy,<br>Bob McAdoo,<br>Charles Barkley,<br>David Cowens,<br>David Robinson,<br>Derrick Rose,<br>Dirk Nowitzki,<br>Hakeem Olajuwon,<br>James Harden,<br>Julius Erving,<br>Kevin Durant,<br>Kevin Garnett,<br>Kobe Bryant,<br>Oscar Robertson,<br>Russell Westbrook,<br>Shaquille O'Neal,<br>Westley Unseld,<br>Willis Reed</td>
    <td class="tg-c3ow">1</td>
  </tr>
</tbody>
</table>

Um ultimo fator a se considerar é se a posição do jogador em quadra é relevante ou se beneficia os jogadores a ganharem o prêmio de MVP. A Figura abaixo mostra tal relação, onde os índices: C, PG, SF, PF e SG, significam <i>Center, Point-Guard, Shooting-Forward, Power-Foward</i> e <i>Shooting-Guard</i>, respectivamente, sendo aqui no Brasil traduzido como: Pivô, Armador, Ala, Ala-Pivô e Ala-Armador, respectivamente.

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/184778868-f4d9a751-1753-4557-9f71-e69dc2ae9bd8.png" width="600px" />
</div>

Olhando a Figura acima nota-se que o atributo posição é substancial, 31 jogadores que ganharam o MVP são ou eram da posição de pivô ou <i>center</i>, a segunda posição que mais se beneficia é a posição de armador ou <i>Point Guard</i>. Portanto, para treinar o modelo, o atributo posição deveria ser utilizado, onde a posição "C" possui mais chances do que a posição "SG", por exemplo. Porém, fazer o scrape dos dados no site oficial da NBA (Link no script <i>nbastats.py</i>), consta muitos valores de fundamentos dos jogadores, mas não fornece a posição de todos. Seria um trabalho bastante maçante tentar automatizar esse processo, logo, nesse primeiro momento tal atributo será descartado. Se os modelos não ficarem bons com outros atributos, posso tentar recorrer ao atributo posição.

# Etapa de Machine Learning

Os dados extraídos não constam com todos os anos em que houve premiação da NBA, pois, no site da NBA existem dados oficiais a partir da temporada 1996-1997, logo, foi possível extrair dados das últimas 26 temporadas, portanto, o dataset criado não possui muitos dados e o mesmo está desbalanceado, mas isso será tratado mais adiante. A ideia por trás da extração e preparação dos dados é em virtude do MVP da temporada regular estar entre os 50 maiores cestinha da temporada, com exceção para Steve Nash em 2005. Ou seja, das últimas 26 vezes que o prêmio de MVP foi dado a um atleta, apenas um destes não estavam entre os 50 maiores cestinhas da temporada regular, logo, achei relevante usar este fato como ponto central da minha modelagem.

Abaixo estão os passos para carregamento do dataset e separação das features:
```
# Carregando os datasets
$ df = pd.read_csv('./datasets/stats-full.csv')
$ X = df.iloc[:, 2:11]
$ y = df['MVP']
```

Os atributos selecionados para a realização da predição foram: AGE, GP, MIN, PTS, AST, REB, FG%, 3P% e FT%, onde:
	
	- AGE : Idade do jogador.
	- GP  : Jogos que o jogador participou na temporada.
	- MIN : Minutos em quadra.
	- PTS : Média de pontos por jogo.
	- AST : Média de assistência por jogo.
	- REB : Média de rebotes por jogo.
	- FG% : Percentual de arremessos convertidos.
	- 3P% : Percentual de arremessos na linha de 3 convertidos.
	- FT% : Percentual de lances livres convertidos.

