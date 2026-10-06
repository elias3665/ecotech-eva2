from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO



crear_tablas()
# empleado = Empleado(nombre="Ana Pérez", email="ana@ecotech.cl")
# print("Antes:", empleado.id)
# # None
# EmpleadoDAO.insertar(empleado)
# print("Después:", empleado.id)


# encontrado = EmpleadoDAO.buscar_por_id(empleado.id)
# print("Encontrado:", encontrado.mostrar_datos())

# print("Listado:")
# for item in EmpleadoDAO.listar():
#         print(item) 

def mostrar_menu():
        print("\n===== ECOTECH =====")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Salir")
def main():
        while True:
                mostrar_menu()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                        registrar_empleado()
                elif opcion == "2":
                        listar_empleados()
                elif opcion == "0":
                        print("Hasta luego.")
                        break
                else:
                        print("Opción no válida.")
if __name__ == "__main__":
        main()

def registrar_empleado():
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        empleado = Empleado(nombre, correo)
        try:
                EmpleadoDAO.insertar(empleado)
                print("Empleado registrado correctamente.")
        except Exception:
                print("No fue posible registrar el empleado.")

def listar_empleados():
        empleados = EmpleadoDAO.listar()
        if not empleados:
                print("No hay empleados registrados.")
                return
        for e in empleados:
                print(f"{e.id} - {e.mostrar_datos()}")

def buscar_empleado():
        try:
                id_empleado =int(input("ID del empleado: "))
        except ValueError:
                print("El ID deber sel un número.")
                empleado = EmpleadoDAO.buscar_por_id(id_empleado)
                if empleado is None:
                        print("Empleado no encontrado.")
                else:
                        print(empleado.mostrar_datos())

def actualizar_empleado():
        try:
                id_empleado = int(input("ID del empleado a actualizar: "))
        except ValueError:
                print("el ID debe ser un numero.")
                return
        actual = EmpleadoDAO.buscar_por_id(id_empleado)
        if actual is None:
                print("Empleado no encontrado.")
                nombre = input(f"Nombre [{actual.nombre}]: ").strip() or actual.nombre
                email = input(f"email [{actual.email}]: ").strip() or actual.email
                try:
                        EmpleadoDAO.actualizar(Empleado(nombre, email, id_empleado))
                        print("Empleado actualizado correctamente.")
                except Exception:
                        print("No fue posible actualizar el empleado.")

def eliminar_empleado():
        try:
                id_empleado = int(input("ID del empleado a eliminar: "))
        except ValueError:
                print("El ID debe ser un numero.")
                return
        try:
                if EmpleadoDAO.eliminar(id_empleado):
                        print("Empleado eliminado correctamente.")
                else:
                        print("empleado no encontrado.")
        except Exception:
                print(" no fue posible eliminar el empleado.")

