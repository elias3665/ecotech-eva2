import requests
import math

def obtener_datos():
    respuesta = requests.get("https://mindicador.cl", timeout=(3, 5))
    respuesta.raise_for_status()
    return respuesta.json()

def extraer_primero(datos):
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")
    serie = datos.get("serie")
    if not isinstance(serie, list) or not serie:
        raise ValueError("No hay valores disponibles.")
    
    registro = serie[0]
    valor = registro["valor"]
    if type(valor) not in (int, float) or not math.isfinite(valor) or valor <= 0:
        raise ValueError("Valor del indicador inválido.")
        
    return registro["fecha"], valor
