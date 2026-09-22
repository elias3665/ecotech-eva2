class Proyecto:
    def _init_(self, id_proyecto: str, nombre: str, fecha_inicio: str):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio


    def nombre(self)-> str:
        return self._nombre

    def fecha_inicio(self)-> str:
        return self._fecha_inicio

    def id_proyecto(self)-> str:
        return self._id_proyecto