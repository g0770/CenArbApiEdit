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

    # Insertar datos en la tabla Role
    roles = [
        {
            "role_name": "superuser",
            "can_manage_users": True,
            "can_manage_all_relevamientos": True,
            "can_create_relevamientos": True,
            "can_modify_own_relevamientos": True,
            "can_generate_reports": True
        },
        {
            "role_name": "admin_municipio",
            "can_manage_users": True,
            "can_manage_all_relevamientos": True,
            "can_create_relevamientos": True,
            "can_modify_own_relevamientos": False,
            "can_generate_reports": True
        },
        {
            "role_name": "relevador",
            "can_manage_users": False,
            "can_manage_all_relevamientos": False,
            "can_create_relevamientos": True,
            "can_modify_own_relevamientos": True,
            "can_generate_reports": False
        },
        {
            "role_name": "tecnico",
            "can_manage_users": False,
            "can_manage_all_relevamientos": True,
            "can_create_relevamientos": False,
            "can_modify_own_relevamientos": False,
            "can_generate_reports": True
        }
    ]

    for role in roles:
        response = requests.post("http://127.0.0.1:8000/api/roles/", json=role, headers=headers)
        if response.status_code == 201:
            print(f"Rol {role['role_name']} agregado exitosamente.")
        else:
            print(f"Error al agregar el rol {role['role_name']}: {response.status_code} - {response.text}")

else:
    print(f"Error al obtener el token: {token_response.status_code} - {token_response.text}")
