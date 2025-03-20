import pandas as pd

# Carregar os dados existentes
df = pd.read_csv("./data/prontuarios_ficticios.csv")

# Criar a coluna 'Alerta' com base no diagnóstico preliminar
df["Alerta"] = df["Diagnóstico Preliminar"].apply(lambda x: 1 if "Indeterminado" in x or "Suspeita de Câncer" in x else 0)

# Salvar novamente o CSV atualizado
df.to_csv("./data/prontuarios_ficticios.csv", index=False)

print("Arquivo atualizado com a coluna 'Alerta'.")
