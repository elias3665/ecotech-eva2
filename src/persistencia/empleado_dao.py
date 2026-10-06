from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado

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
    
    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = f"""
                SELECT id, nombre, email 
                FROM empleado WHERE id = {marca}
            """
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
            return None
        return Empleado(id=fila[0], nombre=fila[1], email=fila[2])
    
    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, email FROM empleado")
        filas = cursor.fetchall()
        conexion.close()
        return [Empleado(id=f[0], nombre=f[1], email=f[2])for f in filas]
    
    @staticmethod
    def actualizar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
            UPDATE empleado
            SET nombre = {marca}, email = {marca}
            WHERE id = {marca}
"""
        cursor.execute(sql, (empleado.nombre, empleado.email, empleado.id, ))
        conexion.commit()
        filas = cursor.rowcount
        conexion.close()
        return filas > 0
    
    @staticmethod
    def eliminar(id:Empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        cursor.execute(f"DELETE FROM empleado WHERE id = {marca}", (id_empleado,))
        conexion.commit()
        filas = cursor.rowcount
        conexion.close()
        return filas > 0