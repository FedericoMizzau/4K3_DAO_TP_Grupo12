from Persistencia.ConexionDB import ConexionDB

def registrar_habitacion(numero, tipo, estado, precio_por_noche):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Habitacion (Numero, Tipo, Estado, PrecioPorNoche) 
                      VALUES (?, ?, ?, ?)''', (numero, tipo, estado, precio_por_noche))
    conexion.commit()
    print(f"Habitación {numero} registrada correctamente.")
    
def consultar_disponibilidad(fecha_entrada, fecha_salida):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM Habitacion 
                      WHERE Estado = 'disponible' 
                      AND Numero NOT IN 
                      (SELECT HabitacionNumero FROM Reserva 
                      WHERE FechaEntrada <= ? AND FechaSalida >= ?)''', (fecha_salida, fecha_entrada))
    habitaciones_disponibles = cursor.fetchall()
    if habitaciones_disponibles:
        print(f"Habitaciones disponibles entre {fecha_entrada} y {fecha_salida}:")
        for habitacion in habitaciones_disponibles:
            print(f" - Habitación {habitacion[0]}: {habitacion[1]}, Precio por noche: {habitacion[3]}")
    else:
        print("No hay habitaciones disponibles en esas fechas.")

