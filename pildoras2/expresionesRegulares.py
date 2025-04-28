import re
from collections import defaultdict                                             # Importamos defaultdict para crear un diccionario con listas como valores
from io import open                                                              # Importamos open para manejar archivos de forma compatible con Python 2 y 3
# Expresiones regulares

Peliculas = [
    "E.T., el extraterrestre",
    "El imperio contraataca",
    "Blade Runner",
    "Indiana Jones y los cazadores del arca perdida",
    "Regreso al futuro",
    "Aliens: El regreso",
    "Scarface",
    "Cazafantasmas",
    "Die Hard: La jungla de cristal",
    "El resplandor",
    "Los Goonies",
    "La historia sin fin",
    "Gremlins",
    "Los cazadores del arca perdida",
    "Gremlins 2: La nueva generación",
    "Cazadores del espacio perdido",
    "Top Gun",
    "RoboCop",
    "Platoon",
    "Karate Kid",
    "Batman",
    "La princesa prometida",
    "Desayuno con diamantes"
]



# Diccionario para agrupar las películas por la primera letra
peliculas_ordenadas = defaultdict(list)

for pelicula in sorted(Peliculas):                                               # Ordenamos alfabéticamente
    # Expresión regular para capturar la primera letra ignorando artículos
    match = re.match(r"^(?:El |La |Los )?(.)", pelicula, re.IGNORECASE)          # Captura la primera letra después de "El", "La" o "Los" si están presentes 
    if match:                                                                    # Si hay una coincidencia, extraemos la letra
        primera_letra = match.group(1).upper()                                    # Convertimos a mayúscula
        peliculas_ordenadas[primera_letra].append(pelicula)                       # Añadimos la película a la lista correspondiente

archivo_externo= open("primerarchivo.txt", "w")


# Mostrar las listas organizadas
for letra, lista in peliculas_ordenadas.items():                                 # Recorremos el diccionario
    orden = f"{letra}: {', '.join(lista)}\n"
    

    archivo_externo.write(orden)

archivo_externo.close()








