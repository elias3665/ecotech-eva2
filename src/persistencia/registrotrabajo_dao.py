from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.registrotrabajo import RegistroTrabajo
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO

class RegistroTrabajoDAO:
    @staticmethod
    def insertar(registro: RegistroTrabajo) -> RegistroTrabajo:
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        try:
            marca = marcador_sql()
            sql = f"""INSERT INTO registro_trabajo (empleado_id, proyecto_id, fecha, horas, descripcion)
                        VALUES ({marca}, {marca}, {marca}, {marca}, {marca})"""
            cursor.execute(sql, (registro.empleado.id, registro.proyecto.id_proyecto, 
                                    registro.fecha, registro.horas, registro.descripcion))
            conexion.commit()
            registro.id = cursor.lastrowid
            return registro
        finally:
            conexion.close()

    @staticmethod
    def listar_completo() -> list[RegistroTrabajo]:
        """Obtiene las filas y reconstruye los objetos de dominio relacionados (hidratación)."""
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT id, empleado_id, proyecto_id, fecha, horas, descripcion FROM registro_trabajo")
            filas = cursor.fetchall()
            registros = []
            for f in filas:
                emp = EmpleadoDAO.buscar_por_id(f[1])
                proy = ProyectoDAO.buscar_por_id(f[2])
                if emp and proy:
                    reg = RegistroTrabajo(id_registro=f[0], empleado=emp, proyecto=proy, 
                                            fecha=f[3], horas=f[4], descripcion=f[5])
                    registros.append(reg)   
            return registros
        finally:
            conexion.close()
