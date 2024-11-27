# Utilização do bow juntamente com o TF-IDF

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
import nltk
import pandas as pd

# Permitir que haja stopwords em português
nltk.download("stopwords")
stop_words = stopwords.words("portuguese")

# Sempre o mesmo texto de exemplo
texto = """
A Traço Têxtil, S.A. pretende um sistema de software para suportar o seu negócio. A
Traço Têxtil dedica-se ao fabrico manual e customizado de fatos (ternos) de alta-
costura, para homem e mulher. Cada fato é fabricado em resposta a uma encomenda
de um cliente, através de um processo manual que envolve diversos funcionários.
Primeiramente, um(a) Consultor(a) atende o cliente, percebe o que o mesmo
pretende e cria no sistema uma nova Ordem de Fabrico, a qual tem associada um
Número de Série. Se for a primeira “consulta” do cliente, o/a consultor(a) tira ao
cliente as medidas necessárias (altura, peso, distância entre ombros, perímetro do
tórax, perímetro do abdómen, distância entre pescoço e polegar, medida do pescoço,
comprimento das calças) e cria o cliente no sistema.
Da informação da Ordem de Fabrico faz ainda parte o tipo de tecido, botões, e notas
sobre os acabamentos desejados.
Depois, um(a) especialista em corte de confecção efetua os cortes de peças
individuais (mangas, corpo, pernas, etc.) no tecido escolhido e nas dimensões
corretas. Esta atividade de corte de confecção, assim como todas as outras eventuais
atividades (ex.: consulta, costura, etc...) para produção deste fato, fica associada à
Ordem de Fabrico. Uma atividade tem informação sobre a data, descrição da
atividade, e observações, e está sempre associada a uma Ordem de Fabrico.
Seguidamente, um(a) costureiro/a efetua a costura das várias peças para montar o
casaco, jaqueta e calças do fato.
Após esta atividade, uma nova consulta deve ocorrer, onde um(a) Consultor(a)
atende o cliente, este prova o fato, e o/a consultor(a) associa ao Processo de Fabrico
as informações recolhidas nesta nova atividade de consulta. Podem ocorrer várias
consultas ao longo do processo de fabrico, e cada uma deverá ficar associada à
respetiva Ordem de Fabrico.
Entre cada consulta, um(a) costureiro/a efetua a costura e correções necessárias
para aproximar o produto final dos objetivos e gosto do cliente.
Após uma última consulta, onde o cliente aceita o produto final, o fato produzido
será entregue ao cliente, juntamente com a fatura a pagar.
Antes de iniciar uma Ordem de Fabrico, um planeador de processo define as
atividades planeadas e associadas à Ordem de Fabrico (ex.: corte de peças, costura,
acabamentos, estampagem, tricotagem, etc...) e que funcionário irá efetuar cada
atividade. No decorrer da execução da Ordem de Fabrico, mais atividades, mesmo
não planeadas, poderão ser associadas a essa Ordem de Fabrico.
"""

# Vetorização usando CountVectorizer (Bag of Words)
vectorizer = CountVectorizer(stop_words=stop_words)
X_bow = vectorizer.fit_transform([texto])
df_bow = pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out())

# Vetorização usando TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)
X_tfidf = tfidf_vectorizer.fit_transform([texto])
df_tfidf = pd.DataFrame(
    X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out()
)

# Exibir as palavras mais relevantes com TF-IDF
top_terms = df_tfidf.T.sort_values(by=0, ascending=False).head(10)

print("Top palavras mais relevantes com TF-IDF:")
print(top_terms)
