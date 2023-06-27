import requests
import os
import json

'''
La librería requests se utiliza para realizar solicitudes HTTP
de manera sencilla y eficiente. Proporciona una interfaz de alto nivel que simplifica 
la comunicación con servidores web y permite realizar tareas comunes como enviar
solicitudes, recibir respuestas y administrar cookies.

'''

'''
La librería os proporciona una forma de interactuar
con el sistema operativo subyacente en el que se está ejecutando el programa. 
Permite realizar diversas operaciones relacionadas
con el sistema de archivos, variables de entorno, procesos. 

'''
'''
La biblioteca json se utiliza para intercambiar datos
estructurados entre diferentes aplicaciones o servicios. También se usa 
para comunicarse con APIs que devuelven datos en formato JSON,
almacenar datos estructurados en archivos o bases de datos,
o realizar transformaciones y análisis de datos JSON en aplicaciones Python.

'''

def obtener_datos_pokemon(nombre_pokemon):
    # Se construye la URL para obtener información sobre el Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    
    # Se envía una solicitud GET a la PokeAPI
    response = requests.get(url)

    # Se verifica si el Pokémon existe (código de estado 404 indica que no existe)
    if response.status_code == 404:
        print("¡El Pokémon no existe!")
        return None

    # Se analizan los datos JSON de la respuesta
    data = response.json()

    # Se obtiene la URL de la imagen frontal del Pokémon
    imagen = data['sprites']['front_default']

    # Se extraen estadísticas, peso, tamaño, movimientos, habilidades y tipos del Pokémon
    estadisticas = data['stats']
    peso = data['weight']
    tamaño = data['height']
    movimientos = [movimiento['move']['name'] for movimiento in data['moves']]
    habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
    tipos = [tipo['type']['name'] for tipo in data['types']]

    # Se crea un diccionario que contenga la información del Pokémon
    pokemon_info = {
        'nombre': nombre_pokemon,
        'imagen': imagen,
        'estadisticas': estadisticas,
        'peso': peso,
        'tamaño': tamaño,
        'movimientos': movimientos,
        'habilidades': habilidades,
        'tipos': tipos
    }

    return pokemon_info

def guardar_pokemon_en_archivo(pokemon_info):
    # Se extrae el nombre del Pokémon del diccionario de información
    nombre_pokemon = pokemon_info['nombre']

    # Se crea un directorio llamado "pokedex" si no existe
    carpeta_pokedex = 'pokedex'
    if not os.path.exists(carpeta_pokedex):
        os.makedirs(carpeta_pokedex)
    
    # Se construye la ruta del archivo JSON del Pokémon
    archivo_json = f"{carpeta_pokedex}/{nombre_pokemon}.json"

    # Se guarda la información del Pokémon como JSON en el archivo
    with open(archivo_json, 'w') as file:
        json.dump(pokemon_info, file, indent=4)
    
    print(f"El Pokémon {nombre_pokemon} ha sido guardado en {archivo_json}")

# Se solicita al usuario que ingrese el nombre de un Pokémon
nombre_pokemon = input("Ingrese el nombre de un Pokémon: ")

# Se obtienen los datos del Pokémon
pokemon_info = obtener_datos_pokemon(nombre_pokemon)

if pokemon_info:
    # Se muestra la imagen y estadísticas del Pokémon
    print(f"Imagen del Pokémon {nombre_pokemon}: {pokemon_info['imagen']}")
    print(f"Peso: {pokemon_info['peso']}")
    print(f"Tamaño: {pokemon_info['tamaño']}")
    print(f"Movimientos: {pokemon_info['movimientos']}")
    print(f"Habilidades: {pokemon_info['habilidades']}")
    print(f"Tipos: {pokemon_info['tipos']}")
    
    # Se guarda la información del Pokémon como archivo JSON
    guardar_pokemon_en_archivo(pokemon_info)
