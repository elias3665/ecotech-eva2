from typing import list, Optional
from dominio.empleado import Empleado
class Departamento:
    
    def _init_(self, id_dept: int, nombre: str, gerente:str):
        self._id_dept = id_dept
        self._nombre = nombre
        self._gerente = gerente

    def nombre(self)-> str:
        return self.nombre

    def id_dept(self)-> str:
        return self.id_dept

    def gerente(self)-> str:
        return self.gerente