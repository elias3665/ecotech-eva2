import getpass
from entradas import pedir_dato
from servicios.autenticacion import registrar_usuario, autenticar
from servicios.indicadores import obtener_datos, extraer_primero
from dominio.usuario import Usuario
import requests

def solicitar_registro():
    print("\n--- REGISTRO DE NUEVA CUENTA DE ACCESO ---")
    try:
        empleado_id = pedir_dato("ID del empleado asociado: ", int)
        nombre = pedir_dato("Ingrese nuevo nombre de usuario: ", Usuario.normalizar_usuario)
        clave = pedir_dato("Ingrese contraseña de seguridad: ", Usuario.validar_clave, getpass.getpass)
        
        if clave != getpass.getpass("Repita la contraseña: "):
            print("Las contraseñas no coinciden. Vuelva al registro.")
            return None
            
        usuario_id = registrar_usuario(empleado_id, nombre, clave)
        print(f"Cuenta creada correctamente. ID de Registro: {usuario_id}")
        return usuario_id
    except (TypeError, ValueError) as error:
        print(f"No se pudo completar el registro: {error}")
        return None

def solicitar_login():
    print("\n====== CONTROL DE ACCESO ECOTECH ======")
    nombre = input("Usuario: ").strip()
    clave = getpass.getpass("Contraseña: ")
    try:
        usuario = autenticar(nombre, clave)
        if usuario is None:
            print("Usuario o contraseña incorrectos.")
        else:
            print("Sesión iniciada correctamente.")
        return usuario
    except (TypeError, ValueError):
        print("No se pudo validar el acceso.")
        return None

def consultar_indicador_economico():
    print("\n--- CONSULTA DE REFERENCIA EXTERNA ---")
    try:
        datos = obtener_datos()
        fecha, valor = extraer_primero(datos)
        print(f"Dólar observado: {valor:.2f} CLP por USD")
        print(f"Fecha del registro: {fecha}")
        print("Origen: mindicador.cl")
    except requests.exceptions.RequestException:
        print("No pudimos consultar el servicio externo. Compruebe su conexión.")
    except (ValueError, KeyError, TypeError):
        print("La respuesta de la API no contiene un indicador válido.")

def menu_privado(usuario_actual):
    if usuario_actual is None:
        print("Debe iniciar sesión para operar el sistema.")
        return "9"
    while True:
        print(f"\nSESIÓN ACTIVA: {usuario_actual['nombre_usuario'].upper()}")
        print("1. Registrar nueva cuenta de empleado")
        print("2. Consultar Indicador de Cambio Financiero (API)")
        print("9. Cerrar Sesión")
        print("0. Salir de la Aplicación")
        
        opcion = input("Opción: ").strip()
        if opcion in ("0", "9"):
            return opcion
        elif opcion == "1":
            solicitar_registro()
        elif opcion == "2":
            consultar_indicador_economico()
        else:
            print("Opción no válida en el entorno privado.")
