from Empleado import *


class Secretario(Empleado):
    Despacho = 0
    Fax = 0
    INCREMENTO = 5  # anual

    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, fax):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, telefono, salario)
        self.Despacho = despacho
        self.Fax = fax

    def imprimir(self):
        print(super(Secretario, self).imprimir(),
              "\nPuesto: Secretario")
