from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

def mostrar_menu():
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    print("1. Registrar Empleado")
    print("2. Listar Empleados")
    print("3. Buscar Empleado por ID")
    print("0. Volver al menú principal")

def registrar():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    if not nombre or not correo: 
        print("[Validación] El nombre y el correo son obligatorios.")
        return
    try:
        emp = EmpleadoDAO.insertar(Empleado(nombre, correo))
        print(f"Éxito: Empleado insertado con ID {emp.id}")
    except Exception as e:
        print(f"Error técnico de persistencia: {e}")

def listar():
    for e in EmpleadoDAO.listar():
        print(f"ID: {e.id} | {e.mostrar_datos()}")

def buscar():
    id_txt = input("Ingrese ID a buscar: ").strip()
    if not id_txt.isdigit(): # Validación preventiva de tipos
        print("[Validación] El ID debe ser un número entero.")
        return
    emp = EmpleadoDAO.buscar_por_id(int(id_txt))
    if emp:
        print(f"Encontrado -> Nombre: {emp.nombre}, Email: {emp.email}")
    else:
        print("Empleado no registrado.")

def menu_empleado():
    while True:
        mostrar_menu()
        opc = input("Seleccione una opción: ").strip()
        if opc == "1": registrar()
        elif opc == "2": listar()
        elif opc == "3": buscar()
        elif opc == "0": break
        else: print("Opción no válida.")
