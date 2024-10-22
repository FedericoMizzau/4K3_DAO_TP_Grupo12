from Persistencia.ConexionDB import ConexionDB

def registrar_reserva(cliente_id, habitacion_numero, fecha_entrada, fecha_salida, cantidad_personas):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Reserva (ClienteID, HabitacionNumero, FechaEntrada, FechaSalida, CantidadPersonas) 
                      VALUES (?, ?, ?, ?, ?)''', (cliente_id, habitacion_numero, fecha_entrada, fecha_salida, cantidad_personas))
    conexion.commit()
    print(f"Reserva registrada para el cliente {cliente_id} en la habitación {habitacion_numero}.")
