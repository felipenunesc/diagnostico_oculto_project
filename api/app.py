from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI()

# Carregar os dados processados
df = pd.read_csv('./data/prontuarios_ficticios.csv')

@app.get('/alertas')
def get_alertas():
    if 'Alerta' not in df.columns:
        return {"error": "A coluna 'Alerta' não existe no banco de dados. Verifique a geração do CSV."}
    alertas = df[df['Alerta'] == 1][['Nome', 'Sintomas', 'Diagnóstico Preliminar']].to_dict(orient='records')
    return {'alertas': alertas}

@app.get("/", response_class=HTMLResponse)
def alertas_ui():
    with open("api/templates/alertas.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)