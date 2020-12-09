import JefeZona
import Secretario
import Vendedor
from cocheEmpresa import Coche

if __name__ == '__main__':
    se = Secretario.Secretario("Juan", "Lope", "12345678p", "calle 1", 965874125, 1230, 3, 76)
    ve = Vendedor.Vendedor("Victor", "Sanchez", "87654321q", "Calle 2", 874563214, 1500, 658741147, "area A", "10")
    je = JefeZona.jefeZona("Hugo", "Torres", "58468548h", "Calle 3", 632587454, 2000, 4)

    # Comprobando salario del Secretario
    se.setAños(3)

    if se.Años > 0:
        se.setSalario()

    # Comprobando salario del #Comprobando salario del Vendedor
    ve.setAños(5)

    if ve.Años > 0:
        ve.setSalario()

    # Comprobando salario del #Comprobando salario del Vendedor
    je.setAños(5)

    if je.Años > 0:
        je.setSalario()

    #Comprobando dar de alta y baja a clientes desde la case vendedor y cambiar de coche

    ve.nuevoCliente("Cliente 1")
    print("Lista de clientes de Vendedor:")
    for i in ve.listaClientes:
        print(i)

    ve.bajaCliente("Cliente 1")
    print("Lista de clientes de Vendedor:")
    for i in ve.listaClientes:
        print(i)

    # # ve.cambiarCoche("1234HTJ", "Seat", "Leon")
    # # ve.getCoche()

    #Combrobando metodos de JefeZona
    je.nuevoVendedor("Juan")
    print("Lista de Vendedores:")
    for i in je.listaVendedores:
        print(i)

    je.bajaVendedor("Juan")
    print("Lista de Vendedores:")
    for i in je.listaVendedores:
        print(i)

    je.setSecretario("Juan")
    print("Secretario del jefe de zona: ",je.getSecretario())

    je.setCoche("1524", "seat", "leon")
    print(je.getCoche())

    # Creando lista de empleados e imprimirlo
    listaEmpleados = [se, ve, je]

    for i in listaEmpleados:
        i.imprimir()
        print("\n")
