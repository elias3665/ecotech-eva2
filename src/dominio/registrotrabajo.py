from dominio.empleado import Empleado
from dominio.proyecto import Proyecto

class RegistroTrabajo:
    def __init__(self, empleado: Empleado, proyecto: Proyecto, fecha: str, horas: float, descripcion: str, id_registro: int = None):
        self.id = id_registro
        self.empleado = empleado
        self.proyecto = proyecto
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion

    def mostrar_detalle(self) -> str:
        return f"[{self.fecha}] {self.empleado.nombre} -> {self.proyecto.nombre}: {self.horas} hrs ({self.descripcion})"
