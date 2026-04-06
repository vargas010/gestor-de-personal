import requests
from pocketbase import PocketBase

# este sistema esta hecho con pocketbase, es una base de datos ligera y rapida que se puede usar para proyectos pequeños y medianos, es una buena opcion para proyectos que no necesitan una base de datos compleja y que quieren una solucion rapida y facil de usar
POCKETBASE_URL = "http://127.0.0.1:8090"
pb = PocketBase(POCKETBASE_URL)

def get_collection(collection_name, filter_str=None):
    try:
        url = f"{POCKETBASE_URL}/api/collections/{collection_name}/records"

        if filter_str:
            url += f"?filter={filter_str}"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse con PocketBase: {e}")
        return None
#dentro de este archivo solo hare un comentario por que no quiero que mi sistema se caiga de algun modo
