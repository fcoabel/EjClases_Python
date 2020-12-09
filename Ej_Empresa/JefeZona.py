from Empleado import *
from Secretario import Secretario
from cocheEmpresa import Coche


class jefeZona(Empleado):
    Despacho = 0
    INCREMENTO = 20
    Secretario = ""
    listaVendedores = []
    Coche = Coche("", "", "")

    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, telefono, salario)
        self.Despacho = despacho

    def imprimir(self):
        print(super(jefeZona, self).imprimir(),
              "\nPuesto: Jefe De Zona")

    def setSecretario(self, nombre):
        self.Secretario = nombre

    def setCoche(self, matricula, marca, modelo):
        self.Coche.__init__(self, matricula, marca, modelo)

    def nuevoVendedor(self, vendedor):
        self.listaVendedores.append(vendedor)

    def bajaVendedor(self, v):
        self.listaVendedores.remove(v)

    def getSecretario(self):
        return self.Secretario

    def getCoche(self):
        return str(Coche)