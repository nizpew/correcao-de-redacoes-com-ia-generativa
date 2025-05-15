import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def analisar_redacao(texto):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "nousresearch/deephermes-3-mistral-24b-preview:free",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Corrija a redação a seguir como um corretor do ENEM. "
                    "Retorne um JSON com as chaves: nota_total (0-1000), "
                    "comentarios_por_competencia (lista de strings), sugestoes_melhoria (string).\n\n"
                    f"Redação: {texto}"
                )
            }
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        resposta_texto = response.json()['choices'][0]['message']['content']
        try:
            return json.loads(resposta_texto)
        except Exception:
            return {
                "nota_total": None,
                "comentarios_por_competencia": [],
                "sugestoes_melhoria": resposta_texto
            }
    except Exception as e:
        return {
            "nota_total": 0,
            "comentarios_por_competencia": ["Erro na análise"],
            "sugestoes_melhoria": str(e)
        }

