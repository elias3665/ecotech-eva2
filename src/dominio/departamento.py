class Departamento:
    
    def __init__(self, id_dept: int, nombre: str, gerente:str):
        self._id_dept = id_dept
        self._nombre = nombre
        self._gerente = gerente

    @property
    def nombre(self)-> str:
        return self._nombre

    @property
    def id_dept(self)-> int:
        return self._id_dept

    @property
    def gerente(self)-> str:
        return self._gerente