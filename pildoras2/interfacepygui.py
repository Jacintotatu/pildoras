import dearpygui.dearpygui as dpg
from openpyxl import Workbook
from datetime import date
import calendar
import random
import os

def nombre_mes_en_espanol(mes):
    """Devuelve el nombre del mes en español."""
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[mes - 1]

def generar_fechas_laborables(año, mes, dias_reciben_cifras, dias_fiesta, festivos):
    """Genera las fechas laborables del mes, excluyendo domingos y festivos."""
    fechas = []

    # Validar los días festivos
    festivos_validos = []
    _, num_dias = calendar.monthrange(año, mes)
    for dia in festivos:
        if 1 <= dia <= num_dias:
            fecha_festivo = date(año, mes, dia)
            if fecha_festivo.weekday() != 6:  # Excluir domingos
                festivos_validos.append(fecha_festivo)

    # Generar todas las fechas del mes
    for dia in range(1, num_dias + 1):
        fecha = date(año, mes, dia)
        if fecha.weekday() != 6 and fecha not in festivos_validos:
            fechas.append(fecha)

    # Seleccionar solo los días que recibirán cifras
    if dias_reciben_cifras > len(fechas):
        dias_reciben_cifras = len(fechas)

    return sorted(random.sample(fechas, dias_reciben_cifras))

def distribuir_cantidad(cantidad_total, fechas_seleccionadas):
    """Distribuye la cantidad total entre las fechas seleccionadas."""
    datos = []
    dias_con_dos_cantidades = random.randint(4, 8) if len(fechas_seleccionadas) < 19 else 0
    dias_una_cantidad = len(fechas_seleccionadas) - dias_con_dos_cantidades
    cantidades_diarias = []

    for _ in range(dias_una_cantidad):
        cantidad = round(random.randint(50, min(350, int(cantidad_total))) / 10) * 10
        cantidades_diarias.append([int(cantidad)])

    for _ in range(dias_con_dos_cantidades):
        cantidad1 = round(random.randint(50, 300) / 10) * 10
        cantidad2 = round(random.randint(50, min(350 - cantidad1, 350)) / 10) * 10
        cantidades_diarias.append([int(cantidad1), int(cantidad2)])

    factura_num = 1
    for i, fecha in enumerate(fechas_seleccionadas):
        facturas = []
        for j, cantidad in enumerate(cantidades_diarias[i]):
            if j == 0:
                facturas.append({
                    'factura_num': factura_num,
                    'cantidad': cantidad,
                    'total': None if len(cantidades_diarias[i]) > 1 else sum(cantidades_diarias[i]),
                    'fecha': fecha.strftime("%d/%m/%Y")
                })
                factura_num += 1
            else:
                facturas.append({
                    'factura_num': None,
                    'cantidad': cantidad,
                    'total': sum(cantidades_diarias[i]),
                    'fecha': fecha.strftime("%d/%m/%Y")
                })
        datos.extend(facturas)

    return datos

def crear_o_actualizar_excel(datos, año, mes, cantidad_total):
    """Crea o actualiza el archivo Excel con los datos proporcionados."""
    nombre_archivo = f"Facturacion_{año}.xlsx"
    mes_nombre = nombre_mes_en_espanol(mes)

    if not os.path.exists(nombre_archivo):
        wb = Workbook()
        ws = wb.active
        ws.title = mes_nombre
    else:
        from openpyxl import load_workbook
        wb = load_workbook(nombre_archivo)
        if mes_nombre in wb.sheetnames:
            del wb[mes_nombre]
            ws = wb.create_sheet(mes_nombre)
        else:
            ws = wb.create_sheet(mes_nombre)

    ws['A1'] = "FACTURA SIMPLIFICADA"
    ws['B1'] = "CANTIDADES DIARIAS"
    ws['C1'] = "TOTAL"
    ws['D1'] = ""
    ws['E1'] = "FECHA"

    fila = 2
    for registro in datos:
        if registro['factura_num'] is not None:
            ws[f'A{fila}'] = registro['factura_num']
        if registro['cantidad'] is not None:
            ws[f'B{fila}'] = f"{registro['cantidad']} €"
        if registro['total'] is not None:
            ws[f'C{fila}'] = f"{registro['total']} €"
        if registro['fecha'] is not None:
            ws[f'E{fila}'] = registro['fecha']
        fila += 1

    fila += 2
    ws[f'B{fila}'] = f"Total {mes_nombre}"
    ws[f'C{fila}'] = f"{int(cantidad_total)} €"

    for col in ['A', 'B', 'C', 'D', 'E']:
        ws.column_dimensions[col].width = 20

    wb.save(nombre_archivo)
    print(f"\nDatos guardados en {nombre_archivo}, hoja '{mes_nombre}'.")
    return nombre_archivo

def callback(sender, app_data, user_data):
    """Callback para manejar el evento del botón."""
    try:
        año = int(dpg.get_value("año"))
        mes = int(dpg.get_value("mes"))
        cantidad_total = float(dpg.get_value("cantidad_total"))
        dias_reciben_cifras = int(dpg.get_value("dias_reciben_cifras"))
        festivos_input = dpg.get_value("festivos")

        # Convertir los días festivos introducidos en una lista de enteros
        festivos = [int(dia.strip()) for dia in festivos_input.split(",") if dia.strip().isdigit()]

        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12.")
        if cantidad_total <= 0:
            raise ValueError("La cantidad total debe ser mayor que 0.")
        if dias_reciben_cifras < 0:
            raise ValueError("Los días que reciben cifras no pueden ser negativos.")

        fechas_seleccionadas = generar_fechas_laborables(año, mes, dias_reciben_cifras, len(festivos), festivos)
        datos = distribuir_cantidad(cantidad_total, fechas_seleccionadas)
        archivo = crear_o_actualizar_excel(datos, año, mes, cantidad_total)

        dpg.set_value("output", f"✅ Datos guardados: {archivo}")
    except ValueError as e:
        dpg.set_value("output", f"❌ Error: {str(e)}")
    except Exception as e:
        dpg.set_value("output", f"❌ Error inesperado: {str(e)}")

# Interfaz gráfica con Dear PyGui
dpg.create_context()

with dpg.window(label="Generador de Facturación", width=500, height=600):
    dpg.add_input_text(label="Año", tag="año", default_value="2025")
    dpg.add_input_text(label="Mes (1-12)", tag="mes", default_value="5")
    dpg.add_input_text(label="Cantidad Total (€)", tag="cantidad_total", default_value="1000")
    dpg.add_input_text(label="Días que reciben cifras", tag="dias_reciben_cifras", default_value="10")
    dpg.add_input_text(label="Días festivos (separados por comas)", tag="festivos", default_value="1, 15")
    dpg.add_button(label="Generar Excel", callback=callback)
    dpg.add_text("", tag="output")

dpg.create_viewport(title='Generador de Facturación', width=520, height=640)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()