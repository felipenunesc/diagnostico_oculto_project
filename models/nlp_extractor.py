import spacy
import pandas as pd

# Carregando o modelo de linguagem do spaCy
nlp = spacy.blank("pt")

# Função para extrair sintomas e histórico médico
def extrair_informacoes(texto):
    doc = nlp(texto)
    entidades = [ent.text for ent in doc.ents]
    return entidades

# Lendo os prontuários fictícios
df = pd.read_csv("./data/prontuarios_ficticios.csv")

# Extraindo sintomas
df["Sintomas Extraídos"] = df["Sintomas"].apply(extrair_informacoes)

print(df.head())
