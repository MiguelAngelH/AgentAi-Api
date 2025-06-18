# Base para conectar la API de OpenAI desde Python
import requests

OPENAI_API_KEY = "TU-API-KEY"  # Reemplaza con tu clave real
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


def consultar_openai(prompt, modelo="gpt-4o-mini"):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": modelo,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"Error en la API de OpenAI: {response.status_code} - {response.text}")

# Alias para facilitar integración en otros archivos
consultar_ia = consultar_openai
