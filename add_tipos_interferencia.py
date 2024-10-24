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

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Insertar datos en la tabla TipoInterferencia
    tipos_interferencia = [
        "Cableado",
        "Edificio",
        "Otro"
    ]

    for tipo in tipos_interferencia:
        response = requests.post("http://127.0.0.1:8000/api/tipos-interferencia/", json={"nombre_tipo": tipo}, headers=headers)
        if response.status_code == 201:
            print(f"Tipo de interferencia {tipo} agregado exitosamente.")
        else:
            print(f"Error al agregar el tipo de interferencia {tipo}: {response.status_code} - {response.text}")

else:
    print(f"Error al obtener el token: {token_response.status_code} - {token_response.text}")
