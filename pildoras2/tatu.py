import random

def distribuir_cantidad(total, dias, valores_posibles):
    # Generar una lista con días y sus respectivas cantidades
    cantidades_por_dia = {i: [] for i in range(1, dias + 1)}
    restante = total

    while restante > 0:
        # Elegir un día aleatorio
        dia = random.randint(1, dias)

        # Elegir una cantidad válida
        posibles_cantidades = [v for v in valores_posibles if v <= restante]
        if posibles_cantidades:
            cantidad = random.choice(posibles_cantidades)
            cantidades_por_dia[dia].append(cantidad)
            restante -= cantidad

    return cantidades_por_dia

# Solicitar entrada del usuario
total = int(input("Introduce la cantidad total (€): "))
dias = int(input("Introduce el número de días laborables: "))

# Generar valores posibles terminados en 0 o 5 dentro del rango 50-300 €
valores_posibles = [x for x in range(50, 301, 5)]

# Generar la distribución
distribucion = distribuir_cantidad(total, dias, valores_posibles)

# Mostrar los resultados
print("\nDistribución generada:")
for dia, cantidades in distribucion.items():
    print(f"Día {dia}: {', '.join(map(str, cantidades))} €")