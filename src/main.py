from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

crear_tablas()
empleado = Empleado(nombre="Ana Pérez", email="ana@ecotech.cl")
print("Antes:", empleado.id)
# None
EmpleadoDAO.insertar(empleado)
print("Después:", empleado.id)


encontrado = EmpleadoDAO.buscar_por_id(empleado.id)
print("Encontrado:", encontrado.mostrar_datos())

print("Listado:")
for item in EmpleadoDAO.listar():
        print(item) 