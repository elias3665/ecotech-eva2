class Empleado:
    def __init__(self,id_empleado:str, nombre: str, salario: float):
        self._id_empleado = id_empleado
        self.nombre = nombre
        self.email = email
        self.salario = salario

    def id_empleado(self)->str:
        return self.id_empleado

    def nombre(self)->str:
        return self.nombre

    def email(self)->str:
        return self.email

    def salario(self)->float:
        return self.salario