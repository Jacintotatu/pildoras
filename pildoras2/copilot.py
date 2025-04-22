from collections import defaultdict

peliculas = ["El padrino", "Avatar", "Titanic", "Gladiador", "Interestelar", "El señor de los anillos", "Amélie", "Casablanca", "El gran Gatsby"]

# Crear un diccionario donde las claves son la primera letra de cada película
peliculas_ordenadas = defaultdict(list)

for pelicula in sorted(peliculas):  # Ordenamos alfabéticamente
    primera_letra = pelicula[0].upper()
    peliculas_ordenadas[primera_letra].append(pelicula)

# Mostrar las listas organizadas
for letra, lista in peliculas_ordenadas.items():
    print(f"{letra}: {lista}")