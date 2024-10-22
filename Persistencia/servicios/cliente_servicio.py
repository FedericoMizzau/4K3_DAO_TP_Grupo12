from Persistencia.ConexionDB import ConexionDB

def registrar_cliente(nombre, apellido, direccion, telefono, email):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Cliente (Nombre, Apellido, Direccion, Telefono, Email) 
                      VALUES (?, ?, ?, ?, ?)''', (nombre, apellido, direccion, telefono, email))
    conexion.commit()
    print(f"Cliente {nombre} {apellido} registrado correctamente.")
