# Introdução

Em 1946, era criada a Associação Americana de Basquetebol (ABA), organização na qual se tornou a Associação Nacional de Basquetebol (NBA) 3 anos depois.
Com o seu sucesso e longevidade, a NBA se tornou uma das ligas mais conhecidas e apreciadas no mundo todo. Uma parte desse sucesso é devido aos momentos únicos e emocionantes que apenas a NBA proporciona. Mas grande parte do brilho da NBA é devido aos jogadores, que se tornaram lendários, 
como Michael Jordan, Kobe Bryant, Lebron James e etc. 
		
E assim como na maioria dos esportes, todo final de temporada um jogador é eleito o jogador mais valioso da liga ou MVP (<i>Most Valuable Player</i>),
sendo tal prêmio visto como um dos parâmetros para avaliar se um jogador vai ser maior do que outros. É evidente que não é qualquer jogador 
que irá ser premiado com o MVP, poucos jogadores conseguem tal feito, mais raro ainda são os jogadores que vencem múltiplas vezes o tão glorioso prêmio. O motivo de um jogador ser agraciado com o prêmio de MVP, difere em alguns fatores, como pontos por jogo, assistências por jogo, rebotes por jogo, se um jogador é um líder em quadra ou não e assim por diante, não só atributos individuais, mas dependendo também do desempenho que seu time possui numa dada temporada. 

# Objetivos

Como visto acima, diversos fatores contribuem para um jogador da NBA ser eleito o MVP da temporada regular, portanto, este projeto visa criar um algoritmo de classificação com a intenção de prever o vencedor do mvp nas temporadas seguintes. Testarei diversos algoritmos para o aprendizado supervisionado para 
realizar a predição. 
	
Os dados foram extraídos por mim, utilizando os scripts <i>main.py</i> e <i>nbastats.py</i> de minha autoria. Os mesmos scripts já possuem um tratamento 
de dados na qual agiliza os processos seguintes. Os algoritmos de machine Learning e avaliação dos mesmos serão todos executados 
utilizando o Scikit-Learn.

# Análise e Exploração dos Dados

Para compreender quais features podem ser determinantes para obter resultados ótimo nos algoritmos, é realizada uma análise dos dados.

Uma possível feature que pode ser importante para inserir no algoritmo é, os times que os jogadores jogam, com isso, vamos analisar os times com mais MVPs da temporada regular na história da NBA. Os times com mais jogadores vencedores do prêmio de MVP é a franquia do Boston Celtics. A Figura abaixo mostra as cinco franquias com mais vencedores do prêmio.

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

Os dados extraídos não constam com todos os anos em que houve premiação da NBA, pois, no site da NBA existem dados oficiais a partir da temporada 1996-1997, logo, foi possível extrair dados das últimas 26 temporadas, portanto, o dataset criado não possui muitos dados e o mesmo está desbalanceado. A ideia por trás da extração e preparação dos dados é em virtude do MVP da temporada regular estar entre os 15 maiores cestinha da temporada, com exceção para Steve Nash em 2005 e 2006. Ou seja, das últimas 26 vezes que o prêmio de MVP foi dado a um atleta, apenas dois destes não estavam entre os 15 maiores pontuadores da temporada regular, logo, achei relevante usar este fato como ponto central da minha modelagem. 

As métricas utilizadas para este problema são: recall, precisão e f1 score, com enfâse no valor do recall (para uma dada precisão) já que estou dando mais importância para o falsos negativos (FN).


**PS: Esta versão consta com a exclusão da feature (Min) e a inclusão de uma nova feature (WIN%), que era difícil de extrair da internet, porém, foi realizado a extração e junção dos valores e o código pode ser encontrado na pasta /scraping**.

A razão para retirar a feature 'Min' é em virtude da minutagem em quadra dos jogadores ter diminuído com o tempo, tendência que pode ser observada em vários outros esportes. A diminuição dos minutos em quadra dos jogadores da NBA é em virtude da preservarção da integridade física para aguentar os diversos jogos da temporada. O Gráfico abaixo mostra a relação dos valores para as classes 0 (Não-MVP) e 1 (MVP):


<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/200566998-4787c97d-a48a-4157-abae-88d6dea1201d.png" width="600px" />
</div>


Apenas olhando este valor, poderia-se esperar que os minutos por jogo poderia ser uma feature importante para a classificação deste projeto, mas olhando os valores e comparando dados de 1997 até os dias de hoje com os valores de minutos por jogo para anos anteriores a 1997, chegamos ao gráfico abaixo:


<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/200567109-6d7fcc23-8592-41ba-83d5-8f46ade0ba78.png" width="600px" />
</div>


Nota-se que a mediana para valores anteriores à 1997, está entre 39 a 40 minutos por jogo e cerca de 75% dos jogadores para esta época jogaram abaixo de 44 minutos por jogo. Já para valores após o ano de 1997, a mediana tanto para classes 0 e 1 estão próximas e em torno de 37 a 38 minutos por jogo. Além disso, 75% dos jogadores desta época jogaram abaixo de 39 minutos por jogo. Para se ter uma noção, um jogo da NBA possui 48 minutos do período regular, em caso de empates, existe 5 min de prorrogação e se houver empates na prorrogação mais 5 minutos são inseridos e assim por diante. Na temporada de 1961-62, Wilt Chamberlain obteve o valor médio de minutos por jogo de 48.5, ou seja, meio minuto a mais do que um jogo normal da nba. E a explicação para isso é que Wilt Chamberlain jogou todos os minutos regulares de todos os jogos da temporada e alguns jogos teve prorrogação e o mesmo jogou também, por isso a média maior do que 48 minutos por jogo, porém, tal prática parece-me impossível 60 anos depois, em razão dos motivos discutido acima.

Seguindo em frente, os atributos selecionados para a realização da predição foram: PTS, AST, REB, FG%, FT% e WIN%, onde:

	- PTS : Média de pontos por jogo.
	- AST : Média de assistência por jogo.
	- REB : Média de rebotes por jogo.
	- FG% : Percentual de arremessos convertidos.
	- FT% : Percentual de lances livres convertidos.
	- WIN% : Porcentagem de vitória pelo clube.

O atributo 3P% foi retirado do processo, pois para MVPs mais antigos, não existem dados oficiais desta característica.

Já foi realizada a primeira troca de modelo, o modelo anterior estava com a técnica SMOTE para tratar dos dados desbalanceados. Tal técnica hoje em dia está se mostrando mais não efetiva do que sim, logo, treinei outros modelos para poder tratar o desbalanceamento de outras formas.

Na pasta scripts/testes, existem as classes e métodos que foram construídas para a automação do processo de treinamento e escolha dos modelos. Para organizar os dados, foi utilizado o MLFlow que possui uma interface gráfica para a manutenção e visualização dos valores das métricas, hiperparâmetros e etc.

O processo de validação foi com a validação cruzada, já que o dataset coletado é pequeno, ou seja, separei o conjunto dos dados entre treino e teste, usando a validação cruzada no conjunto de treino para realizar a classificação dos modelos.

De início, para achar o melhor modelo baseline (sem penalização da classe majoritária e com hiperparâmetros default), foi realizada a validação cruzada para todos os algoritmos listados no arquivo <i>results.py</i>. O que possuiu o maior recall foi o modelo regressão logística, com f1 score igual à 65.89 %, onde utilizou o standard scaler para padronizar os dados. 

Uma forma de acrescentar mais complexidade ao modelo é realizar a seleção das features e penalizar a classe majoritária, fazendo isso, houve uma melhora significativa. O melhor modelo novamente foi o SVC, com os seguintes valores:

- f1 score = 82.02 %
- recall = 92.00 %
- precisão = 73.69 %

Com isso, para alcançar um valor mais expressivo de f1 score, recall e precisão, houve a otimização dos hiperparâmetros com o GridSearchCV, já que não há muitos valores para hiperparâmetros do algoritmo SVC. Após a realização do <i>tunning</i> de hiperparâmetros, o resultado foi:

- f1 score = 83.34 %
- recall = 98.04 %
- precisão = 72.46 %

Os melhores hiperparâmetros para o classificador SVC foram os seguintes: 
```
{C = 1, gamma = 0.1, kernel = 'rbf'}
```

Em comparação com o modelo anterior, que era uma regressão logística, o recall máximo atingido foi de 81.15%, com precição de 42% e f1 score de 55.31 %. Abaixo está uma tabela resumindo os valores para cada modelo:


<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt">Modelos<br></th>
    <th class="tg-7btt">Recall<br></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Precisão</span></th>
    <th class="tg-7btt">F1 Score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">LogisticRegression(class_weight="balanced", max_iter=100, C=0.01, solver='liblinear', penalty='l2')<br></td>
    <td class="tg-c3ow">81.15%<br></td>
    <td class="tg-c3ow">42.00%</td>
    <td class="tg-c3ow">55.31 %</td>
  </tr>
  <tr>
    <td class="tg-c3ow">SVC(class_weight='balanced')<br></td>
    <td class="tg-c3ow">92.00%<br></td>
    <td class="tg-c3ow">73.69%</td>
    <td class="tg-c3ow">82.02%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">SVC(class_weight='balanced', C = 1, gamma = 0.1, kernel = 'rbf')<br></td>
    <td class="tg-c3ow">98.04%</td>
    <td class="tg-c3ow">72.46%<br></td>
    <td class="tg-c3ow">83.34%</td>
  </tr>
</tbody>
</table>

É importante ressaltar a importância de utilizar e extrair as features mais importantes para o problema, apenas com a adição de uma nova feature (WIN%), que na vida real é importante para a classificação de um MVP da NBA, houve uma melhora interessante no valor do recall e precisão.

Com isso, foi utilizado o conjunto de teste no modelo preditivo final para esta versão. O resultado foi:

- f1 score = 81.93 %
- recall = 96.63 %
- precisão = 71.12 %

O resultado em comparação ao resultado da versão anterior (com a regressão logística) foi substancialmente melhor e por isso o mesmo será colocado em produção. 

# Deploy

O deploy foi realizado na plataforma HuggingFace.co, para acessar basta entrar no link ao lado https://huggingface.co/spaces/ramonmedeiro1/NBA-MVP-PREDICTOR. Para montar a parte de design do aplicativo web, o gradio foi utilizado. A pasta deploy possui o que é necessário para deploy do projeto.

# Resultados

Esta seção visa comparar os resultados obtidos pelo modelo realizado nesse projeto e resultados liberados pela comunidade e pela própria NBA para o ranking de jogadores que estão disputando para MVP.

A pasta "compare" possui o script que irá realizar o scraping para obter os valores dos 30 melhores pontuadores da nba e classifica-los em um top 5 para fins de comparação.

--------------
* Mês 1:

```
# 4/11/2022:

     NBA (NBA.com)                                               ML
1 - Giannis Antetokounmpo (MIL)                       1 - Donovan Mitchell (CLE)
2 - Luka Doncic (DAL)                                 2 - Giannis Antetokounmpo (MIL)
3 - Donovan Mitchell (CLE)                            3 - Luka Doncic (DAL)
4 - Ja Morant (MEM)                                   4 - Nikola Jokic (DEN)
5 - Devin Booker (PHX)                                5 - Jrue Holiday (MIL)


# 18/11/2022:
      NBA.com                                                 ML
1 - Luka Doncic (DAL)                                 1 - Jayson Tatum (BOS)
2 - Jayson Tatum (BOS)                                2 - Nikola Jokic (DEN)
3 - Giannis Antetokounmpo (MIL)                       3 - Luka Doncic (DAL)
4 - Nikola Jokic (DEN)                                4 - Giannis Antetokounmpo (MIL)
5 - Ja Morant (MEM)                                   5 - Tyrese Haliburton (IND)
```

* Mês 2:

```
# 04/12/2022:

     NBA.com                                                   ML
1 - Jayson Tatum (BOS)                                1 - Jayson Tatum (BOS)
2 - Luka Doncic (DAL)                                 2 - Nikola Jokic (DEN)
3 - Nikola Jokic (DEN)                                3 - Giannis Antetokounmpo (MIL)
4 - Giannis Antetokounmpo (MIL)                       4 - Luka Doncic (DAL) 
5 - Devin Booker (PHX)                                5 - Devin Booker (PHX)

# 16/12/2022:

     NBA.com                                                  ML
1 - Jayson Tatum (BOS)                                1 - Nikola Jokic (DEN)
2 - Giannis Antetokounmpo (MIL)                       2 - Jayson Tatum (BOS)
3 - Nikola Jokic (DEN)                                3 - Giannis Antetokounmpo (MIL)
4 - Ja Morant (MEM)                                   4 - Joel Embiid (PHI)
5 - Kevin Durant (BKN)                                5 - Jaylen Brown (BOS)
6 - Luka Doncic (DAL)                                 6 - Luka Doncic (DAL)
7 - Zion Williamson (NOP)                             7 - Kevin Durant (BKN)
8 - Joel Embiid (PHI)                                 8 - James Harden (BKN)
9 - Stephen Curry (GSW)                               9 - Zion Williamson (NOP)
10 - Anthony Davis (LAL)                              10 - Anthony Davis (LAL)

# 24/12/2022:

       NBA.com                                                 ML
1 - Giannis Antetokounmpo (MIL)                       1 - Nikola Jokic (DEN)
2 - Nikola Jokic (DEN)                                2 - Joel Embiid (PHI)
3 - Jayson Tatum (BOS)                                3 - Giannis Antetokounmpo (MIL)
4 - Kevin Durant (BKN)                                4 - Jayson Tatum (BOS)
5 - Ja Morant (MEM)                                   5 - Kevin Durant (BKN)
6 - Zion Williamson (NOP)                             6 - Luka Doncic (DAL)
7 - Luka Doncic (DAL)                                 7 - Tyrese Haliburton (IND)
8 - Joel Embiid (PHI)                                 8 - Zion Williamson (NOP)
9 - Donovan Mitchell (CLE)                            9 - Donovan Mitchell (CLE)
10 - Devin Booker (PHX)                               10 - Jaylen Brown (BOS)

```

* Mês 3:

```
02/01/2023:

         NBA.com                                              ML
1 - Nikola Jokic (DEN)                                1 - Nikola Jokic (DEN)
2 - Jayson Tatum (BOS)                                2 - Luka Doncic (DAL)
3 - Luka Doncic (DAL)                                 3 - Joel Embiid (PHI)
4 - Kevin Durant (BKN)                                4 - Giannis Antetokounmpo (MIL)
5 - Giannis Antetokounmpo (MIL)                       5 - Kevin Durant (BKN)
6 - Joel Embiid (PHI)                                 6 - Jayson Tatum (BOS)
7 - Zion Williamson (NOP)                             7 - Tyrese Haliburton (IND)
8 - Ja Morant (MEM)                                   8 - Zion Williamson (NOP)
9 - Jaylen Brown (BOS)                                9 - Jaylen Brown (BOS)
10 - Donovan Mitchell (CLE)                           10 - Bam Adebayo (MIA)

```

# Considerações finais

O presente projeto será supervisionado para a manutenção com o decorrer do tempo.
Para entrar em contato para tratar de bugs ou coisas do tipo, mandar email para o seguinte endereço: **r.medeiro10@gmail.com**.
