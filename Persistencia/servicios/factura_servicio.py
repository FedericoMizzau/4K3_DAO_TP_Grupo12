from Persistencia.ConexionDB import ConexionDB

def registrar_factura(cliente_id, reserva_id, fecha_emision, total):
    conexion = ConexionDB().conectar()
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Factura (ClienteID, ReservaID, FechaEmision, Total) 
                      VALUES (?, ?, ?, ?)''', (cliente_id, reserva_id, fecha_emision, total))
    conexion.commit()
    print(f"Factura generada para el cliente {cliente_id} con un total de {total}.")
