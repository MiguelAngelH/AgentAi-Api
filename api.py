# ------ Base para conectar la API de Gemini desde Python----
import requests

GEMINI_API_KEY = "TU-API"  # Reemplaza con tu clave real
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY


def consultar_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    else:
        raise Exception(f"Error en la API de Gemini: {response.status_code} - {response.text}")

# Alias para facilitar integración en otros archivos
consultar_ia = consultar_gemini
