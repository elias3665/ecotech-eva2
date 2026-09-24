class Empleado:
    def __init__(self, nombre, email, id=None):
        self.id = id
        self.nombre = nombre
        self.email = email

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.email}"