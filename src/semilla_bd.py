from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.registrotrabajo import RegistroTrabajo
from persistencia.conexion import abrir_conexion, marcador_sql
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registrotrabajo_dao import RegistroTrabajoDAO


def buscar_empleado_por_email(email: str) -> bool:
    """Comprueba si el email ya existe antes de insertar (Evita duplicados)."""
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    try:
        marca = marcador_sql()
        sql = f"SELECT id FROM empleado WHERE email = {marca}"
        cursor.execute(sql, (email,))
        return cursor.fetchone() is not None
    finally:
        conexion.close()

def buscar_registro_existente(empleado_id: int, proyecto_id: str, fecha: str) -> bool:
    """Verifica si ya existe un registro de trabajo idéntico para este día."""
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    try:
        marca = marcador_sql()
        sql = f"""
            SELECT id FROM registro_trabajo 
            WHERE empleado_id = {marca} AND proyecto_id = {marca} AND fecha = {marca}
        """
        cursor.execute(sql, (empleado_id, proyecto_id, fecha))
        return cursor.fetchone() is not None
    finally:
        conexion.close()


def cargar_datos_semilla():
    print("\n=== [SEMILLA] Iniciando carga de datos conocidos ===")

    empleados_datos = [
        ("Ana Torres", "ana@ecotech.cl"),
        ("Carlos Ruiz", "carlos@ecotech.cl")
    ]
    
    for nombre, email in empleados_datos:
        if buscar_empleado_por_email(email):
            print(f"El empleado con email '{email}' ya existe. Omitiendo.")
        else:
            nuevo_emp = Empleado(nombre=nombre, email=email)
            EmpleadoDAO.insertar(nuevo_emp)
            print(f"Empleado creado de forma segura: {email}")

    proyectos_datos = [
        ("PRY-01", "Filtros CO2", "2026-01-15"),
        ("PRY-02", "Paneles Eco", "2026-03-20")
    ]
    
    for id_proy, nombre, fecha in proyectos_datos:
        if ProyectoDAO.buscar_por_id(id_proy) is not None:
            print(f"El proyecto '{id_proy}' ya existe. Omitiendo.")
        else:
            nuevo_proy = Proyecto(id_proyecto=id_proy, nombre=nombre, fecha_inicio=fecha)
            ProyectoDAO.insertar(nuevo_proy)
            print(f"Proyecto creado de forma segura: {id_proy}")

    lista_empleados = EmpleadoDAO.listar()
    proyecto_ref = ProyectoDAO.buscar_por_id("PRY-01")
    
    if lista_empleados and proyecto_ref:
        empleado_ref = lista_empleados[0] 
        fecha_registro = "2026-10-15"
        
    
        if buscar_registro_existente(empleado_ref.id, proyecto_ref.id_proyecto, fecha_registro):
            print("El registro de trabajo para esta combinación de datos ya existe. Omitiendo.")
        else: 
            nuevo_registro = RegistroTrabajo(
                empleado=empleado_ref,
                proyecto=proyecto_ref,
                fecha=fecha_registro,
                horas=7.5,
                descripcion="Pruebas de flujo de aire en laboratorio"
            )
            RegistroTrabajoDAO.insertar(nuevo_registro)
            print(f"Registro de trabajo guardado correctamente para {empleado_ref.nombre}")

    print("=== [SEMILLA] Carga finalizada con éxito ===")

if __name__ == "__main__":
    cargar_datos_semilla()
