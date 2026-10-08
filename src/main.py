from persistencia.crear_bd import crear_tablas
from menu.menu_empleado import menu_empleado
from menu.menu_proyecto import menu_proyecto
from menu.menu_registro import menu_registro

def main():
        try:
                crear_tablas()
        except Exception as e:
                print(f"Error crítico al inicializar la base de datos: {e}")


        while True:
                print("\n===== ECOTECH: SISTEMA DE CONTROL INTEGRADO =====")
                print("1. Módulo de Empleados")
                print("2. Módulo de Proyectos")
                print("3. Módulo de Registros de Tiempo (Relación Multi-Entidad)")
                print("0. Salir de la Aplicación")
                
                opcion = input("Seleccione una opción del sistema: ").strip()
                
                if opcion == "1":
                        menu_empleado()
                elif opcion == "2":
                        menu_proyecto()
                elif opcion == "3":
                        menu_registro()
                elif opcion == "0":
                        print("Cerrando sesión en EcoTech. Hasta luego.")
                        break
                else:
                        print("Opción no válida. Intente con los números del menú.")

if __name__ == "__main__":
        main()


