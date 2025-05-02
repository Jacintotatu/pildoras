import pandas as pd
import random
import calendar
import locale
import os

# Configurar el idioma a español para obtener los nombres de los meses
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

# Constante para el nombre del archivo Excel
ARCHIVO_EXCEL = "facturas.xlsx"

def solicitar_entero(mensaje, minimo=None, maximo=None):
    """Solicita un número entero al usuario con validación."""
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Por favor, introduce un valor entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

def solicitar_float(mensaje, minimo=None):
    """Solicita un número flotante al usuario con validación."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Por favor, introduce un valor mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

def generar_excel():
    try:
        # Solicitar datos al usuario
        año = solicitar_entero("Introduce el año: ", minimo=1900)
        mes = solicitar_entero("Introduce el mes (1-12): ", minimo=1, maximo=12)
        cantidad_total = solicitar_float("Introduce la cantidad total (€): ", minimo=0)
        dias_festivos = input("Introduce los días de fiesta separados por coma: ").strip()
        dias_festivos = list(map(int, dias_festivos.split(','))) if dias_festivos else []
        dias_con_cifras = solicitar_entero("Introduce la cantidad de días que recibirán cifras (sin contar domingos): ", minimo=0)

        # Generar las fechas del mes
        num_dias = calendar.monthrange(año, mes)[1]
        fechas = [f"{año}-{mes:02d}-{dia:02d}" for dia in range(1, num_dias + 1)]

        # Filtrar solo días laborables (sin domingos)
        fechas_laborables = [fecha for fecha in fechas if calendar.weekday(año, mes, int(fecha.split('-')[2])) < 6]

        # Filtrar días con cifras, evitando domingos y festivos
        dias_cifras = [fecha for fecha in fechas_laborables if int(fecha.split('-')[2]) not in dias_festivos]
        dias_cifras = random.sample(dias_cifras, min(dias_con_cifras, len(dias_cifras)))  # Selección aleatoria

        # Generar cantidades aleatorias entre 50€ y 300€
        valores_diarios = {fecha: [] for fecha in dias_cifras}
        for fecha in dias_cifras:
            if dias_con_cifras < 19 and random.random() < 0.4:  # 40% de los días tienen dos cifras
                valores_diarios[fecha] = [random.randint(50, 300), random.randint(50, 300)]
            else:
                valores_diarios[fecha] = [random.randint(50, 300)]

        # Ajustar valores para que sumen cantidad_total
        suma_actual = sum(sum(valores) for valores in valores_diarios.values())
        ajuste = cantidad_total - suma_actual
        if ajuste != 0:
            fecha_ajuste = random.choice(list(valores_diarios.keys()))
            valores_diarios[fecha_ajuste][-1] += ajuste

        # Construcción de la tabla
        datos = []
        factura_simplificada = 1

        for fecha in fechas_laborables:
            if fecha in valores_diarios:
                valores = valores_diarios[fecha]
                for i, valor in enumerate(valores):
                    fila = [
                        factura_simplificada if i == 0 else "",  # Número de factura
                        f"{valor:.2f} €",
                        f"{sum(valores):.2f} €" if i == len(valores) - 1 else "",  # Total del día en última fila
                        "",
                        fecha
                    ]
                    datos.append(fila)
                factura_simplificada += 1
            else:
                datos.append(["", "", "", "", fecha])  # Día sin cifras

        # Agregar fila de total
        datos.append(["", "", "", "", ""])
        datos.append(["", f"Total {calendar.month_name[mes]}", f"{cantidad_total:.2f} €", "", ""])

        # Convertir a DataFrame y guardar en Excel
        columnas = ["FACTURA SIMPLIFICADA", "CANTIDADES DIARIAS", "TOTAL", "COLUMNA EN BLANCO", "FECHA"]
        df = pd.DataFrame(datos, columns=columnas)

        # Guardar en el archivo Excel
        nombre_mes = calendar.month_name[mes].capitalize()  # Nombre del mes en español

        # Verificar si el archivo existe
        if not os.path.exists(ARCHIVO_EXCEL):
            with pd.ExcelWriter(ARCHIVO_EXCEL, mode="w") as writer:
                df.to_excel(writer, sheet_name=nombre_mes, index=False)
        else:
            with pd.ExcelWriter(ARCHIVO_EXCEL, mode="a", if_sheet_exists="replace") as writer:
                df.to_excel(writer, sheet_name=nombre_mes, index=False)

        print(f"Archivo {ARCHIVO_EXCEL} actualizado correctamente con los datos del mes {nombre_mes}.")

    except Exception as e:
        print(f"Se produjo un error: {e}")

# Llamar a la función
if __name__ == "__main__":
    generar_excel()
