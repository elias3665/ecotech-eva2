class Proyecto:
    def __init__(self, id_proyecto: str, nombre: str, fecha_inicio: str):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio

    @property
    def nombre(self)-> str:
        return self._nombre

    @property
    def fecha_inicio(self)-> str:
        return self._fecha_inicio

    @property
    def id_proyecto(self)-> str:
        return self._id_proyecto