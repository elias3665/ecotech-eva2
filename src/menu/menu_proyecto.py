from dominio.proyecto import Proyecto
from persistencia.proyecto_dao import ProyectoDAO

def mostrar_submenu():
    print("\n--- GESTIÓN DE PROYECTOS ---")
    print("1. Crear Proyecto")
    print("2. Listar Proyectos")
    print("0. Volver al menú principal")

def crear():
    id_proy = input("Código/ID único del Proyecto: ").strip()
    nombre = input("Nombre del Proyecto: ").strip()
    fecha = input("Fecha Inicio (AAAA-MM-DD): ").strip()
    
    if not id_proy or not nombre or not fecha:
        print("[Validación] Todos los campos son estrictamente requeridos.")
        return
        
    try:
        ProyectoDAO.insertar(Proyecto(id_proyecto=id_proy, nombre=nombre, fecha_inicio=fecha))
        print("Proyecto guardado de manera exitosa.")
    except Exception as e:
        print(f"No se pudo guardar el proyecto. Error: {e}")

def listar():
    for p in ProyectoDAO.listar():
        print(f"Código: {p.id_proyecto} | Proyecto: {p.nombre} | Inicio: {p.fecha_inicio}")

def menu_proyecto():
    while True:
        mostrar_submenu()
        opc = input("Seleccione una opción: ").strip()
        if opc == "1": crear()
        elif opc == "2": listar()
        elif opc == "0": break
        else: print("Opción inválida.")
