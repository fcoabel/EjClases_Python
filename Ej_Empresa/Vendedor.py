from Empleado import *
from cocheEmpresa import *


class Vendedor(Empleado):
    Movil = 0
    areaVenta = ""
    listaClientes = []
    Comisiones = 0
    INCREMENTO = 10
    Coche("", "", "")

    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, movil, areaventa, comisiones):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, telefono, salario)
        self.Movil = movil
        self.areaVenta = areaventa
        self.Comisiones = comisiones

    def imprimir(self):
        print(super(Vendedor, self).imprimir(),
              "\nPuesto: Vendedor")

    def nuevoCliente(self, cliente):
        self.listaClientes.append(cliente)

    def bajaCliente(self, cliente):
        self.listaClientes.remove(cliente)

    def cambiarCoche(self, matricula, marca, modelo):
        self.Coche.__init__(self, matricula, marca, modelo)

    def getCoche(self):
        return Coche
