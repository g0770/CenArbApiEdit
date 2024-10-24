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

    # Insertar datos en la tabla EstadoFitosanitario
    estados_fitosanitarios = [
        "Bueno",
        "Regular",
        "Malo"
    ]

    for estado in estados_fitosanitarios:
        response = requests.post("http://127.0.0.1:8000/api/estados-fitosanitarios/", json={"nombre_estado": estado}, headers=headers)
        if response.status_code == 201:
            print(f"Estado fitosanitario {estado} agregado exitosamente.")
        else:
            print(f"Error al agregar el estado fitosanitario {estado}: {response.status_code} - {response.text}")

    # Insertar datos en la tabla Altura
    alturas = [
        "0-0.5 m", 
        "0.5-1 m", 
        "1-2 m", 
        ">2 m"
    ]

    for altura in alturas:
        response = requests.post("http://127.0.0.1:8000/api/alturas/", json={"rango_altura": altura}, headers=headers)
        if response.status_code == 201:
            print(f"Altura {altura} agregada exitosamente.")
        else:
            print(f"Error al agregar la altura {altura}: {response.status_code} - {response.text}")

    # Insertar datos en la tabla DiametroTronco
    diametros = [
        "0-10 cm", 
        "10-20 cm", 
        "20-30 cm", 
        ">30 cm"
    ]

    for diametro in diametros:
        response = requests.post("http://127.0.0.1:8000/api/diametros-tronco/", json={"rango_diametro": diametro}, headers=headers)
        if response.status_code == 201:
            print(f"Diámetro {diametro} agregado exitosamente.")
        else:
            print(f"Error al agregar el diámetro {diametro}: {response.status_code} - {response.text}")

    # Insertar datos en la tabla CondicionesCrecimiento
    condiciones = [
        "Buena",
        "Regular",
        "Mala"
    ]

    for condicion in condiciones:
        response = requests.post("http://127.0.0.1:8000/api/condiciones-crecimiento/", json={"nombre_condicion": condicion}, headers=headers)
        if response.status_code == 201:
            print(f"Condición de crecimiento {condicion} agregada exitosamente.")
        else:
            print(f"Error al agregar la condición de crecimiento {condicion}: {response.status_code} - {response.text}")

else:
    print(f"Error al obtener el token: {token_response.status_code} - {token_response.text}")
