import random
import calendar
from datetime import datetime
import sqlite3

def obtener_dias_laborables(anio, mes):
    """Devuelve una lista con los días laborables del mes (lunes a viernes)."""
    dias_laborables = []
    num_dias = calendar.monthrange(anio, mes)[1]
    
    for dia in range(1, num_dias + 1):
        fecha = datetime(anio, mes, dia)
        if fecha.weekday() < 5:  # 0=lunes, 1=martes, ..., 4=viernes
            dias_laborables.append(dia)
    
    return dias_laborables

def distribuir_cantidad(total, dias_laborables, dias_con_cifra, valores_posibles):
    """Distribuye la cantidad total asegurando que no quede restante y haya al menos 6 días con doble cantidad."""
    
    # Validaciones iniciales
    if total < (50 * dias_con_cifra):
        raise ValueError(f"El total debe ser al menos {50 * dias_con_cifra}€ para {dias_con_cifra} días")

    dias_elegidos = random.sample(dias_laborables, min(dias_con_cifra, len(dias_laborables)))
    cantidades_por_dia = {dia: [] for dia in dias_elegidos}
    restante = total

    # Primera distribución: una cantidad por día
    promedio_inicial = restante // (len(dias_elegidos) + 6)
    for dia in list(cantidades_por_dia.keys())[:-1]:  # Todos menos el último día
        valores_disponibles = [v for v in valores_posibles if v <= min(restante - 50, promedio_inicial)]
        if not valores_disponibles:
            valores_disponibles = [v for v in valores_posibles if v <= restante - 50]
        if not valores_disponibles:
            valores_disponibles = [50]
            
        cantidad_base = random.choice(valores_disponibles)
        cantidades_por_dia[dia].append(cantidad_base)
        restante -= cantidad_base

    # Garantizar al menos 6 días con doble cantidad si hay menos de 20 días
    if dias_con_cifra < 20:
        num_dias_dobles = max(6, len(cantidades_por_dia) // 3)
        dias_disponibles = [d for d in list(cantidades_por_dia.keys())[:-1]]  # Excluimos el último día
        dias_doble_cantidad = random.sample(dias_disponibles, min(num_dias_dobles, len(dias_disponibles))
        
        for dia in dias_doble_cantidad:
            valores_disponibles = [v for v in valores_posibles if v <= min(restante - 50, 300)]
            if valores_disponibles:
                segunda_cantidad = random.choice(valores_disponibles)
                cantidades_por_dia[dia].append(segunda_cantidad)
                restante -= segunda_cantidad

    # Distribuir el restante en el último día
    ultimo_dia = list(cantidades_por_dia.keys())[-1]
    if restante > 300:
        # Si el restante es mayor a 300, lo dividimos en dos cantidades
        primera_parte = 300
        segunda_parte = restante - 300
        cantidades_por_dia[ultimo_dia].extend([primera_parte, segunda_parte])
    else:
        cantidades_por_dia[ultimo_dia].append(restante)
    restante = 0

    # Mostrar resultados
    print(f"\nDistribución generada para {calendar.month_name[mes]} {anio}:")
    total_distribuido = 0
    for dia, cantidades in cantidades_por_dia.items():
        suma_dia = sum(cantidades)
        total_distribuido += suma_dia
        print(f"{dia}/{mes}/{anio}: {', '.join(map(str, cantidades))} € (Total: {suma_dia} €)")
    
    print(f"\nTotal distribuido: {total_distribuido}€")
    print(f"Días con doble cantidad: {sum(1 for cantidades in cantidades_por_dia.values() if len(cantidades) > 1)}")

    # Guardar en la base de datos
    guardar_distribucion(cantidades_por_dia, anio, mes)

def inicializar_bd():
    conn = sqlite3.connect('distribuciones.db')
    cursor = conn.cursor()
    
    cursor.execute('DROP TABLE IF EXISTS distribuciones')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS distribuciones (
            fecha DATE,
            cantidades TEXT,
            total_dia INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def guardar_distribucion(cantidades_por_dia, anio, mes):
    conn = sqlite3.connect('distribuciones.db')
    cursor = conn.cursor()
    
    # Limpiar datos existentes del mes
    fecha_inicio = f"{anio}-{mes:02d}-01"
    fecha_fin = f"{anio}-{mes:02d}-31"
    cursor.execute('DELETE FROM distribuciones WHERE fecha BETWEEN ? AND ?', 
                  (fecha_inicio, fecha_fin))
    
    # Insertar nuevos datos
    for dia, cantidades in sorted(cantidades_por_dia.items()):
        fecha = f"{anio}-{mes:02d}-{dia:02d}"
        cantidades_str = ' '.join(map(str, cantidades))
        total_dia = sum(cantidades)
        
        cursor.execute('''
            INSERT INTO distribuciones (fecha, cantidades, total_dia)
            VALUES (?, ?, ?)
        ''', (fecha, cantidades_str, total_dia))
    
    conn.commit()
    conn.close()

def mostrar_historial():
    """Muestra todas las distribuciones guardadas."""
    conn = sqlite3.connect('distribuciones.db')
    cursor = conn.cursor()
    
    print("\n=== HISTORIAL DE DISTRIBUCIONES ===")
    for anio in cursor.execute('SELECT DISTINCT anio FROM distribuciones ORDER BY anio'):
        anio = anio[0]
        print(f"\nAño: {anio}")
        
        for mes in cursor.execute('SELECT DISTINCT mes FROM distribuciones WHERE anio = ? ORDER BY mes', (anio,)):
            mes = mes[0]
            print(f"\n{calendar.month_name[mes]} {anio}:")
            
            for row in cursor.execute('''
                SELECT fecha, cantidades, total_dia 
                FROM distribuciones 
                WHERE anio = ? AND mes = ? 
                ORDER BY fecha
                ''', (anio, mes)):
                fecha = datetime.strptime(row[0], '%Y-%m-%d').strftime('%d/%m/%Y')
                print(f"{fecha}: {row[1]} € (Total: {row[2]} €)")
    
    conn.close()

def exportar_a_csv():
    conn = sqlite3.connect('distribuciones.db')
    cursor = conn.cursor()
    
    with open('distribuciones.csv', 'w', encoding='utf-8', newline='') as f:
        f.write("Fecha,Cantidades,Total del día\n")
        
        cursor.execute('SELECT fecha, cantidades, total_dia FROM distribuciones ORDER BY fecha')
        total_mes = 0
        mes_actual = None
        
        for row in cursor.fetchall():
            fecha = datetime.strptime(row[0], '%Y-%m-%d')
            
            if mes_actual and mes_actual != fecha.month:
                f.write(f"TOTAL MES,,{total_mes}\n\n")
                total_mes = 0
                
            mes_actual = fecha.month
            total_mes += row[2]
            
            f.write(f"{fecha.strftime('%d/%m/%Y')},{row[1]},{row[2]}\n")
        
        if mes_actual:
            f.write(f"TOTAL MES,,{total_mes}\n")
    
    conn.close()
    print("\nArchivo CSV generado correctamente")

if __name__ == "__main__":
    while True:
        print("\n=== MENÚ ===")
        print("1. Generar nueva distribución")
        print("2. Ver historial")
        print("3. Exportar a CSV")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            inicializar_bd()
            anio = int(input("Introduce el año: "))
            mes = int(input("Introduce el mes (1-12): "))
            total = int(input("Introduce la cantidad total (€): "))
            dias_con_cifra = int(input("Introduce la cantidad de días que recibirán una cifra: "))
            
            dias_laborables = obtener_dias_laborables(anio, mes)
            valores_posibles = [x for x in range(50, 301, 10)]
            distribuir_cantidad(total, dias_laborables, dias_con_cifra, valores_posibles)
            
        elif opcion == "2":
            mostrar_historial()
            
        elif opcion == "3":
            exportar_a_csv()
            
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break