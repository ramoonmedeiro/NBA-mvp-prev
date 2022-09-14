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

Os dados extraídos não constam com todos os anos em que houve premiação da NBA, pois, no site da NBA existem dados oficiais a partir da temporada 1996-1997, logo, foi possível extrair dados das últimas 26 temporadas, portanto, o dataset criado não possui muitos dados e o mesmo está desbalanceado, mas isso será tratado mais adiante. A ideia por trás da extração e preparação dos dados é em virtude do MVP da temporada regular estar entre os 15 maiores cestinha da temporada, com exceção para Steve Nash em 2005 e 2006. Ou seja, das últimas 26 vezes que o prêmio de MVP foi dado a um atleta, apenas dois destes não estavam entre os 15 maiores pontuadores da temporada regular, logo, achei relevante usar este fato como ponto central da minha modelagem.

Os atributos selecionados para a realização da predição foram: AGE, GP, MIN, PTS, AST, REB, FG% e FT%, onde:
	
	- AGE : Idade do jogador.
	- GP  : Jogos que o jogador participou na temporada.
	- MIN : Minutos em quadra.
	- PTS : Média de pontos por jogo.
	- AST : Média de assistência por jogo.
	- REB : Média de rebotes por jogo.
	- FG% : Percentual de arremessos convertidos.
	- FT% : Percentual de lances livres convertidos.

O atributo 3P% foi retirado do processo, pois para MVPs mais antigos, não existem dados oficiais desta característica.

Abaixo estão os passos para carregamento do dataset e separação das features:
```
# Carregando os datasets
import pandas as pd
import numpy as np

df = pd.read_csv('./datasets/stats-full.csv')
X = df.drop(['PLAYER', 'TEAM', '3P%', 'YEAR', 'MVP'], axis = 1)
y = df['MVP']
```
como dito mais acima, o dataset criado não é balanceado, possuindo mais instâncias da classe negativa para MVP (0) do que para a classe positiva pra MVP (1). Abaixo pode-se observar a porcentagem de cada classe e graficamente como as quantidade das classes 0 e 1 são distantes.

```
df['MVP'].value_counts(normalize=True)*100

0    84.454756
1    15.545244
Name: MVP, dtype: float
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/190220487-e5a03ab0-476c-4477-b4c0-bb7926bcae4f.png" width="450px" />
</div>


Para tratar de tal empecilho, realizei seleção de features, uso do parâmetro class_weight para penalização do modelo, porém, nenhum forneceu melhores resultados do que o modelo base. Com este fato, recorri ao oversampling com SMOTE, onde iguala-se a quantidade de instâncias da classe minoritária (1)
com a da classe majoritária (0) por meio da sintetização dos dados, são dados novos criados a partir de outros. A desvantagem de utilizar este método é a justamente os dados criados serem sintéticos, não são dados nativos da história da NBA, o que pode causar um viés nos resultados. Já a vantagem é que agora possímos um dataset totalmente balanceado. Nas Figuras seguintes, observa-se a ação do oversampling no dataset deste projeto:


<div align="center">
  <img src="https://user-images.githubusercontent.com/102380417/190220776-d1865d4e-43b8-4e20-82ac-2bd40e513dba.png" width="450px" />
</div>

A métrica utilizada neste projeto é a acurácia, já que os dados serão balanceados, porém, com foco também no recall, já que minimizar os falsos negativos (FN) é mais importante do que minimizar os falsos postivos (FP).

# Bibliotecas necessárias

```
# Carregando modelos
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Carregando kfold e cross_val_score
from sklearn.model_selection import KFold, cross_val_score

# Carregando pré-processamento
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Carreganbdo SMOTE
from imblearn.over_sampling import SMOTE

# Carregando métricas
from sklearn.metrics import classification_report, accuracy_score
```

# Separação entre treino e teste

É realizada a separação do dataset em treino e teste utilizando a função train_test_split. Usei 33 % para o tamanho da base de testes, já que o dataset não é grande.

```
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.33, random_state=99, stratify=y)
```

A validação cruzada foi utilizada para validar o modelo, já que não foi possível separar o conjunto de treino em mais cnjuntos, como o de validação. Um erro muito comum ao usar SMOTE e a validação cruzada é realizar o oversampling no conjunto de treino inteiro para depois realizar a validação cruzada, com isso, a função abaixo foi criada para ultrapassar essa dificuldade, onde o oversampling é realizado apenas nas instâncias de treino e não na validação. 

```
def validacao_cruzada(modelo, X, y):
    kfold = KFold(n_splits = 5, shuffle=True, random_state=99)
    results = []

    for linhas_treino, linhas_valid in kfold.split(X):
        #Pegando índices
        X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
        y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]
        
        # Usando SMOTE apenas no conjunto de treino e não na validação
        smt = SMOTE(random_state=98)
        X_treino_smt, y_treino_smt = smt.fit_resample(X_treino, y_treino)
        
        # Treinando modelo
        modelo.fit(X_treino_smt, y_treino_smt)
        
        # Prevendo valores para os conjunto de validação e obtendo acurácia
        prev_valid = modelo.predict(X_valid)
        results.append(accuracy_score(y_valid, prev_valid))
    
    return np.array(results)
```


Os dois modelos que serão testados são : Regressão Logística e SVC. Abaixo são mostrados os valores para o modelo base:

```
modelos = [LogisticRegression(max_iter=300), SVC(probability=True)]


# Sem nada (baseline)
d = {}
for modelo in modelos:
    d[modelo] = validacao_cruzada(modelo, X_treino, y_treino).mean()
print(d)


{LogisticRegression(max_iter=300): 0.853901996370236, SVC(probability=True): 0.8335753176043557}
```

As duas modificações que foi feita nesta etapa foi a padronização e normalização dos dados com StandardScaler e MinMaxScaler, respectivamente.

```
# Definindo objetos
scaler = StandardScaler()
norm = MinMaxScaler()

# Ajustando e transformando colunas
X_scaler = scaler.fit_transform(X_treino) 
X_norm = norm.fit_transform(X_treino)

# Transformando para DataFrame para utilizar na função acima
scaler_df = pd.DataFrame(X_scaler)
norm_df = pd.DataFrame(X_norm)
```

Resultados para os dados padronizados:

```
# Com padronização

d_scaler = {}
for modelo in modelos:
    d_scaler[modelo] = validacao_cruzada(modelo, scaler_df, y_treino).mean()
print(d_scaler)


{LogisticRegression(max_iter=300): 0.8678160919540229, SVC(probability=True): 0.8778175979530289}
```

Resultados para os dados normalizados:

```
# Com normalização

d_norm = {}
for modelo in modelos:
    d_norm[modelo] = validacao_cruzada(modelo, norm_df, y_treino).mean()
print(d_norm)

{LogisticRegression(max_iter=300): 0.8295825771324864, SVC(probability=True): 0.8817906836055656}
```

Nota-se que para os dados padronizados, os valores de acurácia melhoraram para ambos os modelos. Já para os dados normalizados, a acurácia piorou para a regressão logística enquanto para SVC melhorou mais ainda. Observando todos os valores, decide-se que o modelo escolhido foi o SVC com dados normalizados, com acurácia de aproximadamente 90%.

# Conjunto de Teste

Agora que já sabemos o modelo totalmente validado e sem overfitting, é hora de ver como o mesmo irá se comportar ao receber dados totalmente novos do conjunto de teste. 

```
# Definindo o modelo
modelo_final = SVC(probability=True)

# Realizando apenas a transformação dos dados de teste
X_teste_norm = norm.transform(X_teste)

# Prevendo valores
prev_teste = modelo_final.predict(X_teste_norm)

# Observando o comportamento geral do modelo com os dados de teste
print(classification_report(y_teste, prev_teste))



              precision    recall  f1-score   support

           0       0.96      0.88      0.92       121
           1       0.55      0.82      0.65        22

    accuracy                           0.87       143
   macro avg       0.75      0.85      0.79       143
weighted avg       0.90      0.87      0.88       143
```

A acurácia se manteve em 87%, porém, como dito antes, o foco era no recall. Conseguiu-se um recall alto sem que ncessariamente a precisão fosse muit baixa.
Portanto, para o presente projeto, esses resultados foram bom o suficiente. Foi realizada a otimzação dos hiperparâmetros com o BayesSearchCV, mas para todos os casos, ocorria o overfitting, então abandonei a ideia e mantive os resultados obtidos acima.

# Deploy

O deploy foi realizado na plataforma HuggingFace.co, para acessar basta entrar no link ao lado https://huggingface.co/spaces/ramonmedeiro1/NBA-MVP-PREDICTOR. Para montar a parte de design do aplicativo web, o gradio foi utilizado. A pasta deploy possui o que é necessário para deploy do projeto.

# Considerações finais

O presente projeto segue em observação na fase Beta, além disso, o mesmo será supervisionado para a manutenção com o decorrer do tempo.
Para entrar em contato para tratar de bugs ou coisas do tipo, mandar email para o seguinte endereço: **r.medeiro10@gmail.com**.

