from Persistencia.ConexionDB import ConexionDB
from Persistencia.servicios.habitacion_servicio import registrar_habitacion, consultar_disponibilidad
from Persistencia.servicios.cliente_servicio import registrar_cliente
from Persistencia.servicios.reserva_servicio import registrar_reserva
from Persistencia.servicios.factura_servicio import registrar_factura
from Persistencia.servicios.empleado_servicio import asignar_empleado_habitacion

def insertar_datos_prueba(conexion):

    cursor = conexion.cursor()

    # Insertar datos en la tabla Habitacion
    cursor.execute('''INSERT INTO Habitacion (Numero, Tipo, Estado, PrecioPorNoche) 
                      VALUES (101, 'simple', 'disponible', 50.0),
                             (102, 'doble', 'ocupada', 80.0),
                             (103, 'suite', 'disponible', 150.0)''')

    # Insertar datos en la tabla Cliente
    cursor.execute('''INSERT INTO Cliente (Nombre, Apellido, Direccion, Telefono, Email) 
                      VALUES ('Juan', 'Pérez', 'Calle Falsa 123', '123456789', 'juan.perez@gmail.com'),
                             ('Ana', 'López', 'Av. Siempre Viva 456', '987654321', 'ana.lopez@gmail.com')''')

    # Insertar datos en la tabla Reserva
    cursor.execute('''INSERT INTO Reserva (ClienteID, HabitacionNumero, FechaEntrada, FechaSalida, CantidadPersonas) 
                      VALUES (1, 101, '2024-10-22', '2024-10-25', 1),
                             (2, 102, '2024-10-20', '2024-10-22', 2)''')

    # Insertar datos en la tabla Factura
    cursor.execute('''INSERT INTO Factura (ClienteID, ReservaID, FechaEmision, Total) 
                      VALUES (1, 1, '2024-10-22', 150.0),
                             (2, 2, '2024-10-21', 160.0)''')

    # Insertar datos en la tabla Empleado
    cursor.execute('''INSERT INTO Empleado (Nombre, Apellido, Cargo, Sueldo) 
                      VALUES ('Carlos', 'Ramírez', 'recepcionista', 1200.0),
                             ('Laura', 'Gómez', 'servicio de limpieza', 1000.0)''')

    # Confirmar cambios
    conexion.commit()
    print("Datos de prueba insertados correctamente.")


if __name__ == "__main__":
    # Obtener la instancia única de la conexión a la base de datos
    conexion = ConexionDB()
    conn = conexion.conectar()

    # Insertar datos de prueba
    insertar_datos_prueba(conn)
    
    # Registro de una nueva habitación
    registrar_habitacion(104, 'suite', 'disponible', 200.0)

    # Registro de un nuevo cliente
    registrar_cliente('Pedro', 'Martínez', 'Av. Las Flores 789', '654321987', 'pedro.martinez@gmail.com')

    # Registro de una reserva
    registrar_reserva(1, 104, '2024-10-24', '2024-10-26', 2)

    # Generación de una factura
    registrar_factura(1, 1, '2024-10-26', 400.0)

    # Asignación de un empleado a una habitación
    asignar_empleado_habitacion(1, 104)

    # Consulta de disponibilidad de habitaciones
    consultar_disponibilidad('2024-10-24', '2024-10-26')

    # Cerrar la conexión
    conexion.cerrar_conexion()
