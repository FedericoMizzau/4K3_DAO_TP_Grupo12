from Persistencia.ConexionDB import ConexionDB

def asignar_empleado_habitacion(empleado_id, habitacion_numero):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''UPDATE Habitacion SET Estado = 'ocupada' WHERE Numero = ?''', (habitacion_numero,))
    # Aquí agregaríamos lógica para asignar el empleado a la habitación, si hubiera un sistema para ello.
    conexion.commit()
    print(f"Empleado {empleado_id} asignado a la habitación {habitacion_numero}.")
