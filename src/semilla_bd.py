import bcrypt
from persistencia.conexion import abrir_conexion, marcador_sql
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.usuario_dao import UsuarioDAO

def buscar_empleado_por_email(email: str):
    """Comprueba si el email ya existe y retorna el objeto si lo encuentra."""
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    try:
        marca = marcador_sql()
        sql = f"SELECT id, nombre, email FROM empleado WHERE email = {marca}"
        cursor.execute(sql, (email,))
        fila = cursor.fetchone()
        if fila:
            return Empleado(id=fila[0], nombre=fila[1], email=fila[2])
        return None
    finally:
        conexion.close()

def cargar_datos_semilla():
    print("\n=== [SEMILLA] Iniciando carga de infraestructura de datos ===")
    
    # 1. Asegurar que las tablas físicas existan (incluyendo la nueva tabla usuario)
    crear_tablas()

    # 2. Datos del Empleado destinado a ser Administrador
    nombre_emp = "Ana Torres"
    correo_emp = "ana@ecotech.cl"
    
    empleado_admin = buscar_empleado_por_email(correo_emp)
    
    if empleado_admin is not None:
        print(f"El empleado base '{correo_emp}' ya existe en el sistema. Recuperando ID.")
    else:
        try:
            nuevo_emp = Empleado(nombre=nombre_emp, email=correo_emp)
            empleado_admin = EmpleadoDAO.insertar(nuevo_emp)
            print(f"Empleado base creado con éxito. ID asignado: {empleado_admin.id}")
        except Exception as e:
            print(f"No se pudo crear el empleado base: {e}")
            return

    # 3. Preparación de la cuenta inicial Admin (Seguridad de la Clase 3)
    username_admin = "admin"
    clave_plana = "admin123"  # Contraseña inicial válida según las reglas de largo >= 6

    # Verificar si la cuenta de usuario ya fue sembrada anteriormente
    usuario_existente = UsuarioDAO.buscar_por_nombre(username_admin)
    
    if usuario_existente is not None:
        print(f"La cuenta de usuario '{username_admin}' ya se encuentra registrada. Omitiendo inserción.")
    else:
        try:
            # Validar las reglas del negocio de la contraseña desde el dominio
            clave_validada = Usuario.validar_clave(clave_plana)
            
            # Generar el Hash criptográfico usando bcrypt
            salt = bcrypt.gensalt()
            hash_bytes = bcrypt.hashpw(clave_validada.encode("utf-8"), salt)
            password_hash = hash_bytes.decode("utf-8")
            
            # Construir la entidad vinculándola con el id_empleado recuperado
            nuevo_usuario = Usuario(
                nombre_usuario=username_admin,
                password_hash=password_hash,
                empleado_id=empleado_admin.id
            )
            
            # Persistir en la base de datos
            UsuarioDAO.insertar(nuevo_usuario)
            print(f"Cuenta de acceso '{username_admin}' sembrada correctamente.")
            print(f"Credenciales iniciales de prueba -> Usuario: {username_admin} | Clave: {clave_plana}")
            
        except Exception as e:
            print(f"Fallo crítico al sembrar la cuenta de acceso seguro: {e}")

    print("=== [SEMILLA] Proceso de inicialización finalizado de forma limpia ===")

if __name__ == "__main__":
    cargar_datos_semilla()
