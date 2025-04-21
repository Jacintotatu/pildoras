import csv                                    # Importamos la biblioteca csv
with open('ejemplo.csv', newline='') as csvfile:                # Abrimos el archivo ejemplo.csv en modo lectura
    miCsv = csv.reader(csvfile, delimiter=';', quotechar='|')    # Leemos el archivo csv y lo guardamos en la variable miCsv
    for linea in miCsv:                                             # Recorremos el archivo linea por linea
        print('-'.join(linea))