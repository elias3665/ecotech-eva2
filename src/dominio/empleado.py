from typing import Optional


class Empleado:
    def __init__(self, nombre: str, email: str, id: Optional[int] = None):
        self._id = id
        self._nombre = nombre
        self._email = email

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.email}"