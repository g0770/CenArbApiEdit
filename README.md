
# API Documentation

## Description
This API provides endpoints to manage municipalities, provinces, roles, and users. The endpoints support standard CRUD operations (Create, Read, Update, Delete).

## Base URL
`/api/v1`

## Endpoints
### /alturas/
- **GET**: Obtiene una lista de todas las alturas
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Altura`

### /alturas/{id}/
- **GET**: Obtiene detalles de una altura por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Altura`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Altura`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Altura`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /arboles/
- **GET**: Obtiene una lista de todos los árboles
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Arbol`

### /arboles/{id}/
- **GET**: Obtiene detalles de un árbol por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Arbol`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Arbol`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Arbol`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /condiciones-crecimiento/
- **GET**: Obtiene una lista de todas las condiciones de crecimiento
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `CondicionesCrecimiento`

### /condiciones-crecimiento/{id}/
- **GET**: Obtiene detalles de una condición de crecimiento por su ID
  - **Responses**:
    - `200`: 
      - Schema: `CondicionesCrecimiento`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `CondicionesCrecimiento`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `CondicionesCrecimiento`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /diametros-tronco/
- **GET**: Obtiene una lista de todos los diámetros de tronco
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `DiametroTronco`

### /diametros-tronco/{id}/
- **GET**: Obtiene detalles de un diámetro de tronco por su ID
  - **Responses**:
    - `200`: 
      - Schema: `DiametroTronco`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `DiametroTronco`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `DiametroTronco`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /especies/
- **GET**: Obtiene una lista de todas las especies
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Especie`

### /especies/{id}/
- **GET**: Obtiene detalles de una especie por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Especie`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Especie`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Especie`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /estados-fitosanitarios/
- **GET**: Obtiene una lista de todos los estados fitosanitarios
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `EstadoFitosanitario`

### /estados-fitosanitarios/{id}/
- **GET**: Obtiene detalles de un estado fitosanitario por su ID
  - **Responses**:
    - `200`: 
      - Schema: `EstadoFitosanitario`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `EstadoFitosanitario`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `EstadoFitosanitario`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /fotos/
- **GET**: Obtiene una lista de todas las fotos
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Foto`

### /fotos/{id}/
- **GET**: Obtiene detalles de una foto por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Foto`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Foto`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Foto`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /interferencias/
- **GET**: Obtiene una lista de todas las interferencias
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Interferencia`

### /interferencias/{id}/
- **GET**: Obtiene detalles de una interferencia por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Interferencia`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Interferencia`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Interferencia`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /mediciones/
- **GET**: Obtiene una lista de todas las mediciones
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Medicion`

### /mediciones/{id}/
- **GET**: Obtiene detalles de una medición por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Medicion`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Medicion`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Medicion`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /municipios/
- **GET**: Obtiene una lista de todos los municipios
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Municipio`

### /municipios/{id}/
- **GET**: Obtiene detalles de un municipio por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Municipio`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Municipio`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Municipio`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /provincias/
- **GET**: Obtiene una lista de todas las provincias
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Provincia`

### /provincias/{id}/
- **GET**: Obtiene detalles de una provincia por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Provincia`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Provincia`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Provincia`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /roles/
- **GET**: Obtiene una lista de todos los roles
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `Role`

### /roles/{id}/
- **GET**: Obtiene detalles de un rol por su ID
  - **Responses**:
    - `200`: 
      - Schema: `Role`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Role`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `Role`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /tipos-interferencia/
- **GET**: Obtiene una lista de todos los tipos de interferencia
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `TipoInterferencia`

### /tipos-interferencia/{id}/
- **GET**: Obtiene detalles de un tipo de interferencia por su ID
  - **Responses**:
    - `200`: 
      - Schema: `TipoInterferencia`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `TipoInterferencia`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `TipoInterferencia`

- **DELETE**: 
  - **Responses**:
    - `204`: 

### /token/
- **POST**: Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `TokenObtainPair`

### /token/refresh/
- **POST**: Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `TokenRefresh`

### /users/
- **GET**: Obtiene una lista de todos los usuarios
  - **Parameters**:
    - `page` (query, optional): A page number within the paginated result set.
  - **Responses**:
    - `200`: 
    - `400`: Bad Request

- **POST**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `201`: 
      - Schema: `User`

### /users/{id}/
- **GET**: Obtiene detalles de un usuario por su ID
  - **Responses**:
    - `200`: 
      - Schema: `User`
    - `404`: Not Found

- **PUT**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `User`

- **PATCH**: 
  - **Parameters**:
    - `data` (body, required): No description.
  - **Responses**:
    - `200`: 
      - Schema: `User`

- **DELETE**: 
  - **Responses**:
    - `204`: 


## Data Models

### Municipio
- `id` (integer): Unique identifier.
- `nombre` (string): Name of the municipality.
- `provincia` (integer): Province ID.

### Provincia
- `id` (integer): Unique identifier.
- `nombre` (string): Name of the province.

### Role
- `id` (integer): Unique identifier.
- `name` (string): Name of the role.

### User
- `id` (integer): Unique identifier.
- `username` (string): Username of the user.
- `email` (string): Email of the user.
- `role` (integer): Role ID associated with the user.
