# --- Asegúrate de tener un Api de openAI configurada en api.py ---
import subprocess
from tools import tool_horario, tool_reiniciar_router, tool_direccion, tool_empleados # Importa las herramientas definidas en tools.py
from api import consultar_ia

# --- Llama a la API de OpenAI (reemplaza la version anterior con ollama)---
def consultar_ollama(prompt, modelo="gpt-4o-mini"):
    """
    Esta función consulta la API de OpenAI.
    Cambia el modelo si lo deseas (por ejemplo: "gpt-4").
    Requiere tener configurado el archivo api.py con tu API key.
    """
    return consultar_ia(prompt, modelo)

# --- Ejecutar tool según respuesta del modelo ---
def ejecutar_tools(tools_list):
    datos = {}
    for tool in set(tools_list):
        if tool == "horario":
            datos["horario"] = tool_horario()
        elif tool == "reiniciar_router":
            datos["reiniciar_router"] = tool_reiniciar_router()
        elif tool == "direccion":
            datos["direccion"] = tool_direccion()
        elif tool == "empleados":
            datos["empleados"] = tool_empleados()
    return datos

def extraer_tools(respuesta):
    if "[USAR TOOL:" in respuesta:
        contenido = respuesta.split("[USAR TOOL:")[1].split("]")[0].strip()
        nombres = [n.strip().replace("tool_", "") for n in contenido.split(",")]
        return nombres
    return []

# --- Prompt base del agente ---
rol = """
Eres un técnico de computadoras de un local de reparación. Solo respondes preguntas técnicas relacionadas con computadoras, redes, hardware, software, impresoras, problemas de conexión, etc. Si el usuario pregunta algo fuera de ese ámbito, responde: 'Solo puedo responder consultas técnicas de computadoras.'

Antes de responder, si necesitas información de tools, indícalo con [USAR TOOL:tool1, tool2, ...] según corresponda. Luego, cuando recibas los datos, genera la respuesta usando solo esa información.
Las tools solo contienen los datos, tú debes crear la respuesta usando esos datos.
Las tools disponibles son: tool_horario, tool_reiniciar_router, tool_direccion, tool_empleados.
"""

# --- Conversación ---
pregunta_usuario = input("Usuario: ")

prompt = f"{rol}\n\nUsuario: {pregunta_usuario}\nAsistente:"
respuesta = consultar_ollama(prompt)
tools_needed = extraer_tools(respuesta)

# Si el modelo no indica tools, forzamos a que lo haga
if not tools_needed:
    prompt_tools = f"{rol}\n\nUsuario: {pregunta_usuario}\nAntes de responder, indica explícitamente qué tools necesitas usando el formato [USAR TOOL:tool1, tool2, ...].\nAsistente:"
    respuesta_tools = consultar_ollama(prompt_tools)
    tools_needed = extraer_tools(respuesta_tools)

if tools_needed:
    datos_tools = ejecutar_tools(tools_needed)
    print("Datos obtenidos de las tools:")
    print(datos_tools)
    print("Respuesta generada por el modelo:")
    prompt_final = f"{rol}\n\nUsuario: {pregunta_usuario}\nDatos: {datos_tools}\nAsistente:"
    respuesta_final = consultar_ollama(prompt_final)
    print(respuesta_final)
else:
    print("Respuesta:")
    print(respuesta)
