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

    # Paso 2: Añadir las especies
    url = "http://127.0.0.1:8000/api/especies/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    especies = [
      {
        "nombre_cientifico": "Acacia floribunda",
        "nombre_comun": "Acacia Blanca/Floribunda",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Albizia julibrissin",
        "nombre_comun": "Acacia de constantinopla",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Robinia pseudoacacia umbraculifera",
        "nombre_comun": "Acacia globosa",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acacia dealbata",
        "nombre_comun": "Acacia mimosa",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Gleditsia triacanthos",
        "nombre_comun": "Acacia tres espinas",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Robinia pseudoacacia",
        "nombre_comun": "Falsa acacia",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acacia melanoxylon",
        "nombre_comun": "Acacia negra",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acacia visco",
        "nombre_comun": "Visco",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Acer buergerianum",
        "nombre_comun": "Acer buergeriano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acer palmatum",
        "nombre_comun": "Acer japones",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acer negundo",
        "nombre_comun": "Acer negundo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Schinus areira",
        "nombre_comun": "Aguaribay",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Populus deltoides",
        "nombre_comun": "Alamo Carolino",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Populus alba",
        "nombre_comun": "Alamo palateado",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cinnamomum camphora",
        "nombre_comun": "Alcanforero",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Neltuma alba",
        "nombre_comun": "Algarrobo blanco",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Neltuma nigra",
        "nombre_comun": "Algarrobo negro",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Hibiscus syriacus",
        "nombre_comun": "Altea/Rosa de siria",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Araucaria bidwillii",
        "nombre_comun": "Araucaria bidwillii",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cercis siliquastrum",
        "nombre_comun": "Árbol de judea",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ailanthus altissima",
        "nombre_comun": "Arbol del cielo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Acacia Dealbata",
        "nombre_comun": "Aromo frances",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Bauhinia forficata",
        "nombre_comun": "Bauhinia forficata",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Bauhinia variegata",
        "nombre_comun": "Bauhinia variegata",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Brachychiton populneus",
        "nombre_comun": "Brachichito",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Camellia sp.",
        "nombre_comun": "Camelia",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Castanea sativa",
        "nombre_comun": "Castaño europeo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Casuarina cunninghamiana",
        "nombre_comun": "Casuarina",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Catalpa sp.",
        "nombre_comun": "Catalpa",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cedrela odorata",
        "nombre_comun": "Cedro americano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cedrus deodara",
        "nombre_comun": "Cedro del himalaya",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cedrus libani",
        "nombre_comun": "Cedro del libano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Erythrina crista-galli",
        "nombre_comun": "Ceibo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Geoffroea decorticans",
        "nombre_comun": "Chañar",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Taxodium distichum",
        "nombre_comun": "Cipres calvo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Cupressus sempervirens",
        "nombre_comun": "Cipres Piramidal",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Prunus cerasifera",
        "nombre_comun": "Ciruelo de flor",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Lagerstroemia indica",
        "nombre_comun": "Crespon",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Sapium haematospermum",
        "nombre_comun": "Curupí o Lecherón",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Kageneckia lanceolata",
        "nombre_comun": "Durazno del campo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Vachellia caven",
        "nombre_comun": "Espinillo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Eucalyptus",
        "nombre_comun": "Eucaliptus",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Eucalyptus",
        "nombre_comun": "Eucaliptus Medicinal",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Manihot grahamii",
        "nombre_comun": "Falso cafeto",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ficus benjamina",
        "nombre_comun": "Ficus Benjamina",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Fraxinus americana",
        "nombre_comun": "Fresno Americano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Fraxinus excelsior aurea",
        "nombre_comun": "Fresno dorado",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Fraxinus pennsylvanica",
        "nombre_comun": "Fresno rojo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ginkgo biloba",
        "nombre_comun": "Ginkgo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ficus elastica",
        "nombre_comun": "Gomero",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Punica granatum",
        "nombre_comun": "Granado de adorno",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Grevillea robusta",
        "nombre_comun": "Grevillea/roble sedoso",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Tecoma stans",
        "nombre_comun": "Guaran Amarillo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Sebastiania commersoniana",
        "nombre_comun": "Guindillo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Hovenia dulcis",
        "nombre_comun": "Hovenia",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Peltophorum dubium",
        "nombre_comun": "Ibirá Pitá",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Jacaranda mimosifolia",
        "nombre_comun": "Jacarandá",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Paulownia tomentosa",
        "nombre_comun": "Kiri",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Handroanthus chrysotrichus",
        "nombre_comun": "Lapacho amarillo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Tabebuia roseo-alba",
        "nombre_comun": "Lapacho blanco",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Handroanthus heptaphyllus",
        "nombre_comun": "Lapacho negro",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Handroanthus impetiginosus",
        "nombre_comun": "Lapacho Rosado",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Nerium oleander",
        "nombre_comun": "Laurel de jardin",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Leucaena leucocephala",
        "nombre_comun": "Leucaena",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ligustrum lucidum",
        "nombre_comun": "Ligustro disciplinado",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Callistemon",
        "nombre_comun": "Limpiatubos",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Liquidambar styraciflua",
        "nombre_comun": "Liquidambar",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Magnolia grandiflora",
        "nombre_comun": "Magnolia",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Malus domestica",
        "nombre_comun": "Manzano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Broussonetia papyrifera",
        "nombre_comun": "Mora de papel",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Morus alba",
        "nombre_comun": "Mora negra-blanca",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Citrus × sinensis",
        "nombre_comun": "Naranjo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Eriobotrya japonica",
        "nombre_comun": "Níspero",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Juglans regia",
        "nombre_comun": "Nogal",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Eugenia uniflora",
        "nombre_comun": "Ñangapiri/Pitanga",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Ulmus minor",
        "nombre_comun": "Olmo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Phytolacca dioica",
        "nombre_comun": "Ombú",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Enterolobium contortisiliquum",
        "nombre_comun": "Pacará/timbó colorado",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Trachycarpus fortunei",
        "nombre_comun": "Palmera Fortunei",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Roystonea oleracea",
        "nombre_comun": "Palmera imperial",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Phoenix canariensis",
        "nombre_comun": "Palmera Phoenix",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Syagrus romanzoffiana",
        "nombre_comun": "Palmera Pindó",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Washingtonia filifera",
        "nombre_comun": "Palmera Washingtonia",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ceiba speciosa",
        "nombre_comun": "Palo Borracho",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Elaeagnus angustifolia",
        "nombre_comun": "Paraíso",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Melia azedarach",
        "nombre_comun": "Paraiso Sombrilla",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Pyrus calleryana",
        "nombre_comun": "Peral de flor",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Pinus",
        "nombre_comun": "Pino",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Platanus x hispanica",
        "nombre_comun": "Platano",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Citrus paradisi",
        "nombre_comun": "Pomelo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Rhus sp.",
        "nombre_comun": "Rhus",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Quercus palustris",
        "nombre_comun": "Roble de los pantanos",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Quercus robur",
        "nombre_comun": "Roble Europeo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Croton urucurana",
        "nombre_comun": "Sangre de drago",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Salix humboldtiana",
        "nombre_comun": "Sauce Criollo",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Salix babylonica",
        "nombre_comun": "Sauce llorón",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Salix x erythroflexuosa",
        "nombre_comun": "Sauce Tortuoso o Eléctrico",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ficus sycomorus",
        "nombre_comun": "Sicomoro",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Ligustrum lucidum",
        "nombre_comun": "Siempre Verde/Ligustro",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Styphnolobium japonicum",
        "nombre_comun": "Sófora",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Celtis ehrenbergiana",
        "nombre_comun": "Tala",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Thevetia peruviana",
        "nombre_comun": "Thevetia",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Tilia",
        "nombre_comun": "Tilo",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Tipuana tipu",
        "nombre_comun": "Tipa Blanca",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Pterogyne nitens",
        "nombre_comun": "Tipa colorada",
        "origen": "nativa"
      },
      {
        "nombre_cientifico": "Liriodendron tulipifera",
        "nombre_comun": "Tulipanero",
        "origen": "exótica"
      },
      {
        "nombre_cientifico": "Yucca",
        "nombre_comun": "Yuca",
        "origen": "exótica"
      }
    ]


    for especie in especies:
        response = requests.post(url, headers=headers, json=especie)
        if response.status_code == 201:
            print(f"Especie {especie['nombre_cientifico']} añadida exitosamente.")
        else:
            print(f"Error al añadir especie {especie['nombre_cientifico']}: {response.status_code}, {response.text}")
else:
    print("Error al obtener el token:", token_response.status_code, token_response.text)