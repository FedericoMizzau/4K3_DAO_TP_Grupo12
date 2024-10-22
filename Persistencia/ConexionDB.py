import sqlite3
from sqlite3 import Error

class ConexionDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConexionDB, cls).__new__(cls)
            cls._instance._conexion = None
        return cls._instance

    def conectar(self):
        if self._conexion is None:
            try:
                self._conexion = sqlite3.connect('hotel.db')
                self.crear_tablas()
                print("Conexión establecida correctamente.")
            except Error as e:
                print(f"Error al conectar con la base de datos: {e}")
        return self._conexion

    def crear_tablas(self):
        cursor = self._conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Habitacion (
            Numero INTEGER PRIMARY KEY,
            Tipo TEXT NOT NULL,
            Estado TEXT NOT NULL,
            PrecioPorNoche REAL NOT NULL
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Cliente (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            Direccion TEXT,
            Telefono TEXT,
            Email TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Reserva (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ClienteID INTEGER NOT NULL,
            HabitacionNumero INTEGER NOT NULL,
            FechaEntrada TEXT NOT NULL,
            FechaSalida TEXT NOT NULL,
            CantidadPersonas INTEGER NOT NULL,
            FOREIGN KEY (ClienteID) REFERENCES Cliente(ID),
            FOREIGN KEY (HabitacionNumero) REFERENCES Habitacion(Numero)
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Factura (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ClienteID INTEGER NOT NULL,
            ReservaID INTEGER NOT NULL,
            FechaEmision TEXT NOT NULL,
            Total REAL NOT NULL,
            FOREIGN KEY (ClienteID) REFERENCES Cliente(ID),
            FOREIGN KEY (ReservaID) REFERENCES Reserva(ID)
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Empleado (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            Cargo TEXT NOT NULL,
            Sueldo REAL NOT NULL
        )''')

        self._conexion.commit()
        print("Tablas creadas exitosamente.")

    def cerrar_conexion(self):
        if self._conexion:
            self._conexion.close()
            self._conexion = None
            print("Conexión cerrada correctamente.")
