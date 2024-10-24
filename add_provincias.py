import requests

# Paso 1: Obtener el token
token_url = "http://127.0.0.1:8000/api/token/"
token_data = {
    "username": "Desarrollo",  # Reemplaza con tu nombre de usuario
    "password": "Ramcc202323@"  # Reemplaza con tu contraseña
}
token_response = requests.post(token_url, data=token_data)

if token_response.status_code == 200:
    token = token_response.json().get("access")
    print("Token obtenido:", token)

    # Paso 2: Lista de provincias con su georeferencia
    provincias = [
        {"nombre": "Buenos Aires", "georeferencia": "-36.685093, -60.078898"},
        {"nombre": "Ciudad Autónoma de Buenos Aires", "georeferencia": "-34.613150, -58.377230"},
        {"nombre": "Catamarca", "georeferencia": "-28.468920, -65.783740"},
        {"nombre": "Chaco", "georeferencia": "-27.451970, -60.737840"},
        {"nombre": "Chubut", "georeferencia": "-43.307440, -65.107380"},
        {"nombre": "Córdoba", "georeferencia": "-31.417130, -64.183370"},
        {"nombre": "Corrientes", "georeferencia": "-27.475820, -58.823980"},
        {"nombre": "Entre Ríos", "georeferencia": "-31.723480, -59.240600"},
        {"nombre": "Formosa", "georeferencia": "-26.183440, -58.175820"},
        {"nombre": "Jujuy", "georeferencia": "-24.185590, -65.299490"},
        {"nombre": "La Pampa", "georeferencia": "-36.615060, -64.291630"},
        {"nombre": "La Rioja", "georeferencia": "-29.413050, -66.856800"},
        {"nombre": "Mendoza", "georeferencia": "-32.890840, -68.844310"},
        {"nombre": "Misiones", "georeferencia": "-27.366670, -55.897780"},
        {"nombre": "Neuquén", "georeferencia": "-38.951630, -68.059100"},
        {"nombre": "Río Negro", "georeferencia": "-40.807440, -62.996670"},
        {"nombre": "Salta", "georeferencia": "-24.788250, -65.410480"},
        {"nombre": "San Juan", "georeferencia": "-31.537500, -68.536390"},
        {"nombre": "San Luis", "georeferencia": "-33.295020, -66.335650"},
        {"nombre": "Santa Cruz", "georeferencia": "-51.622680, -69.218110"},
        {"nombre": "Santa Fe", "georeferencia": "-31.633330, -60.700000"},
        {"nombre": "Santiago del Estero", "georeferencia": "-27.795110, -64.261460"},
        {"nombre": "Tierra del Fuego, Antártida e Islas del Atlántico Sur", "georeferencia": "-54.801910, -68.302950"},
        {"nombre": "Tucumán", "georeferencia": "-26.816670, -65.216670"}
    ]

    # Paso 3: URL de tu API para agregar provincias
    url = "http://127.0.0.1:8000/api/provincias/"

    # Encabezados de la solicitud, incluyendo el token de autenticación
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Iterar sobre las provincias y enviar una solicitud POST para cada una
    for provincia in provincias:
        response = requests.post(url, json=provincia, headers=headers)
        if response.status_code == 201:
            print(f"Provincia {provincia['nombre']} agregada exitosamente.")
        else:
            print(f"Error al agregar la provincia {provincia['nombre']}: {response.status_code} - {response.text}")
else:
    print(f"Error al obtener el token: {token_response.status_code} - {token_response.text}")
