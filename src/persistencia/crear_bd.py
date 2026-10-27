from persistencia.conexion import abrir_conexion, obtener_motor

def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    motor = obtener_motor()
    
    try:
        if motor == "sqlite":
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_usuario TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    id_empleado INTEGER NOT NULL UNIQUE,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(id) ON DELETE CASCADE
    )
''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS empleado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS proyecto (
                    id TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS registro_trabajo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    empleado_id INTEGER NOT NULL,
                    proyecto_id TEXT NOT NULL,
                    fecha TEXT NOT NULL,
                    horas REAL NOT NULL,
                    descripcion TEXT NOT NULL,
                    FOREIGN KEY(empleado_id) REFERENCES empleado(id) ON DELETE CASCADE,
                    FOREIGN KEY(proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_usuario TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    id_empleado INTEGER NOT NULL UNIQUE,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(id) ON DELETE CASCADE
                )
            ''')
        else:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS empleado (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS proyecto (
                    id VARCHAR(50) PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    fecha_inicio VARCHAR(10) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS registro_trabajo (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    empleado_id INT NOT NULL,
                    proyecto_id VARCHAR(50) NOT NULL,
                    fecha VARCHAR(10) NOT NULL,
                    horas DECIMAL(5,2) NOT NULL,
                    descripcion TEXT NOT NULL,
                    FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE,
                    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre_usuario VARCHAR(40) NOT NULL UNIQUE,
                    password_hash VARCHAR(255) NOT NULL,
                    id_empleado INT NOT NULL UNIQUE,
                    FOREIGN KEY (id_empleado) REFERENCES empleado(id) ON DELETE CASCADE
                )
            ''')
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()

