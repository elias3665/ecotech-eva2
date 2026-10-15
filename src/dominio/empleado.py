from typing import Optional

class Empleado:
    def __init__(self, nombre: str, email: str, id: Optional[int] = None):
        self.id = id
        self.nombre = nombre
        self.email = email

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        if value is not None and (not isinstance(value, int) or value <= 0):
            raise ValueError("El ID del empleado debe ser un número entero positivo.")
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre del empleado no puede estar vacío.")
        
        nombre_limpio = value.strip()
        # Modificación: Límite estricto ajustado a un máximo de 20 caracteres
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 20:
            raise ValueError("El nombre del empleado debe tener entre 2 y 20 caracteres.")
            
        self._nombre = nombre_limpio

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value or "@" not in value or "." not in value:
            raise ValueError("El correo electrónico proporcionado no es válido.")
        self._email = value.strip()

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.email}"
