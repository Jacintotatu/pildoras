import random
import calendar
from datetime import datetime, timedelta
import pandas as pd

def generar_fechas(año, mes, dias_fiesta, dias_cifras):
    # Obtener el número total de días en el mes
    _, num_dias_mes = calendar.monthrange(año, mes)

    # Generar todas las fechas del mes
    fechas = [datetime(año, mes, dia) for dia in range(1, num_dias_mes + 1)]

    # Filtrar los domingos y los días de fiesta
    dias_laborables = [fecha for fecha in fechas if fecha.weekday() != 6 and fecha.day not in dias_fiesta]

    # Seleccionar aleatoriamente los días que recibirán cifras
    dias_seleccionados = random.sample(dias_laborables, dias_cifras)

    return dias_seleccionados

def repartir_cantidad(cantidad_total, dias_cifras):
    cantidades = []
    while sum(cantidades) < cantidad_total:
        cantidad = random.randint(50, 300)
        if sum(cantidades) + cantidad <= cantidad_total:
            cantidades.append(cantidad)
        elif len(cantidades) < dias_cifras:
            cantidades.append(cantidad_total - sum(cantidades))
    return cantidades

def generar_excel(año, mes, cantidad_total, dias_fiesta, dias_cifras):
    # Generar fechas
    fechas = generar_fechas(año, mes, dias_fiesta, dias_cifras)

    # Repartir cantidad total
    cantidades = repartir_cantidad(cantidad_total, dias_cifras)

    # Crear DataFrame
    data = {
        'FACTURA SIMPLIFICADA': [],
        'CANTIDADES DIARIAS': [],
        'TOTAL': [],
        '': [],
        'FECHA': []
    }

    factura_num = 1
    for i, fecha in enumerate(fechas):
        if dias_cifras < 19 and random.random() < 0.2:  # 20% de probabilidad de dividir en dos filas
            cantidad1 = random.randint(50, cantidades[i] - 50)
            cantidad2 = cantidades[i] - cantidad1
            data['FACTURA SIMPLIFICADA'].append(factura_num)
            data['CANTIDADES DIARIAS'].append(f"{cantidad1}€")
            data['TOTAL'].append('')
            data[''].append('')
            data['FECHA'].append(fecha.strftime('%d-%m-%Y'))
            factura_num += 1

            data['FACTURA SIMPLIFICADA'].append('')
            data['CANTIDADES DIARIAS'].append(f"{cantidad2}€")
            data['TOTAL'].append(f"{cantidades[i]}€")
            data[''].append('')
            data['FECHA'].append('')
        else:
            data['FACTURA SIMPLIFICADA'].append(factura_num)
            data['CANTIDADES DIARIAS'].append(f"{cantidades[i]}€")
            data['TOTAL'].append(f"{cantidades[i]}€")
            data[''].append('')
            data['FECHA'].append(fecha.strftime('%d-%m-%Y'))
            factura_num += 1

    # Añadir fila de total
    data['FACTURA SIMPLIFICADA'].append('')
    data['CANTIDADES DIARIAS'].append(f"Total {calendar.month_name[mes]}")
    data['TOTAL'].append(f"{cantidad_total}€")
    data[''].append('')
    data['FECHA'].append('')

    # Crear DataFrame
    df = pd.DataFrame(data)

    # Guardar en Excel
    file_path = f"cantidades_{año}_{mes}.xlsx"
    if not pd.io.excel._xlrd.read_excel(file_path):
        df.to_excel(file_path, index=False)
    else:
        with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)

    print(f"Archivo Excel generado: {file_path}")

# Ejemplo de uso
año = int(input("Introduce el año: "))
mes = int(input("Introduce el mes: "))
cantidad_total = int(input("Introduce la cantidad total: "))
dias_fiesta = list(map(int, input("Introduce los días de fiesta separados por comas: ").split(',')))
dias_cifras = int(input("Introduce la cantidad de días del mes que van a recibir cifras: "))

generar_excel(año, mes, cantidad_total, dias_fiesta, dias_cifras)
