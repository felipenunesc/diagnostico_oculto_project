import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Carregar os dados
df = pd.read_csv('./data/prontuarios_ficticios.csv')

# Criar um vetorizador para transformar os sintomas em representações numéricas
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Sintomas'])

# Criar rótulos (1 = possível câncer, 0 = não suspeito)
df['Alerta'] = df['Diagnóstico Preliminar'].apply(lambda x: 1 if 'Indeterminado' in x else 0)
y = df['Sintomas']

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um modelo simples
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Testar o modelo
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia do Modelo: {acuracia*100:.2f}%")