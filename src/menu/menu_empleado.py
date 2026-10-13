from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def mostrar_menu():
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    print("1. Registrar Empleado")
    print("2. Listar Empleados")
    print("3. Buscar Empleado por ID")
    print("4. Actualizar Empleado")
    print("5. Eliminar Empleado")
    print("0. Volver al menú principal")

def _correo_valido(correo: str) -> bool:
    if len(correo) > 150 or correo.count("@") != 1 or " " in correo:
        return False
    dominio = correo.rsplit("@", 1)[1]
    return bool(dominio and "." in dominio and not dominio.startswith(".") and not dominio.endswith("."))

def registrar():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    if not nombre or len(nombre) > 100 or not _correo_valido(correo):
        print("[Validación] El nombre es obligatorio (máximo 100 caracteres) y el correo debe ser válido.")
        return
    try:
        emp = EmpleadoDAO.insertar(Empleado(nombre, correo))
        print(f"Éxito: Empleado insertado con ID {emp.id}")
    except Exception as e:
        print(f"Error técnico de persistencia: {e}")

def listar():
    try:
        empleados = EmpleadoDAO.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return
        for e in empleados:
            print(f"ID: {e.id} | {e.mostrar_datos()}")
    except Exception as e:
        print(f"No se pudieron listar los empleados: {e}")

def buscar():
    id_txt = input("Ingrese ID a buscar: ").strip()
    if not id_txt.isdigit():
        print("[Validación] El ID debe ser un número entero.")
        return
    try:
        emp = EmpleadoDAO.buscar_por_id(int(id_txt))
        if emp:
            print(f"Encontrado -> Nombre: {emp.nombre}, Email: {emp.email}")
        else:
            print("Empleado no registrado.")
    except Exception as e:
        print(f"No se pudo buscar el empleado: {e}")

def actualizar():
    id_txt = input("ID del empleado a actualizar: ").strip()
    if not id_txt.isdigit():
        print("[Validación] El ID debe ser un número entero.")
        return
    try:
        existente = EmpleadoDAO.buscar_por_id(int(id_txt))
        if existente is None:
            print("Empleado no registrado.")
            return
        nombre = input(f"Nombre [{existente.nombre}]: ").strip()
        correo = input(f"Correo [{existente.email}]: ").strip()
        if not nombre or len(nombre) > 100 or not _correo_valido(correo):
            print("[Validación] El nombre es obligatorio (máximo 100 caracteres) y el correo debe ser válido.")
            return
        actualizado = EmpleadoDAO.actualizar(
            Empleado(nombre=nombre, email=correo, id=existente.id)
        )
        print("Empleado actualizado." if actualizado else "No se realizaron cambios.")
    except Exception as e:
        print(f"No se pudo actualizar el empleado: {e}")

def eliminar():
    id_txt = input("ID del empleado a eliminar: ").strip()
    if not id_txt.isdigit():
        print("[Validación] El ID debe ser un número entero.")
        return
    if input("¿Confirma la eliminación? (s/n): ").strip().lower() != "s":
        print("Eliminación cancelada.")
        return
    try:
        eliminado = EmpleadoDAO.eliminar(int(id_txt))
        print("Empleado eliminado." if eliminado else "Empleado no registrado.")
    except Exception as e:
        print(f"No se pudo eliminar el empleado: {e}")

def menu_empleado():
    while True:
        mostrar_menu()
        opc = input("Seleccione una opción: ").strip()
        if opc == "1": registrar()
        elif opc == "2": listar()
        elif opc == "3": buscar()
        elif opc == "4": actualizar()
        elif opc == "5": eliminar()
        elif opc == "0": break
        else: print("Opción no válida.")
