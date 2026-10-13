from typing import Optional

from dominio.empleado import Empleado
from dominio.proyecto import Proyecto

class RegistroTrabajo:
    def __init__(
        self,
        empleado: Empleado,
        proyecto: Proyecto,
        fecha: str,
        horas: float,
        descripcion: str,
        id_registro: Optional[int] = None,
    ):
        self._id = id_registro
        self._empleado = empleado
        self._proyecto = proyecto
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def empleado(self) -> Empleado:
        return self._empleado

    @property
    def proyecto(self) -> Proyecto:
        return self._proyecto

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def horas(self) -> float:
        return self._horas

    @property
    def descripcion(self) -> str:
        return self._descripcion

    def mostrar_detalle(self) -> str:
        return f"[{self.fecha}] {self.empleado.nombre} -> {self.proyecto.nombre}: {self.horas} hrs ({self.descripcion})"
