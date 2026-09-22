from persistencia.conexion import abrir_conexion, obtener_motor

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"
        sql = f"""
            INSERT INTO empleado (nombre, email)
            VALUES ({marcador}, {marcador})
        """
        cursor.execute(sql, (empleado.nombre, empleado.email))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()

        return empleado 