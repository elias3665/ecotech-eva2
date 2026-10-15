class Departamento:
    def __init__(self, id_dept: int, nombre: str, gerente: str):
        self.id_dept = id_dept
        self.nombre = nombre
        self.gerente = gerente

    @property
    def id_dept(self) -> int:
        return self._id_dept

    @id_dept.setter
    def id_dept(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID del departamento debe ser un número entero positivo.")
        self._id_dept = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre del departamento no puede estar vacío.")
        self._nombre = value.strip()

    @property
    def gerente(self) -> str:
        return self._gerente

    @gerente.setter
    def gerente(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre del gerente no puede estar vacío.")
        self._gerente = value.strip()




