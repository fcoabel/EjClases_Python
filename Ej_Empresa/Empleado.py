class Empleado:
    Nombre = ""
    Apellidos = ""
    Dni = ""
    Direccion = ""
    Años = 0
    Telefono = 0
    Salario = 0
    Supervisor = ""

    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Dni = dni
        self.Direccion = direccion
        self.Telefono = telefono
        self.Salario = salario

    def imprimir(self):
        print("Empleado: ", self.Nombre, ", ", self.Apellidos ,
              "\nDNI: ", self.Dni,
              "\nDirección: ", self.Direccion,
              "\nTeléfono:", self.Telefono,
              "\nSalario: ", self.Salario,
              "\nAños en la empresa: ", self.Años,
              "\nSupervisor: ", self.Supervisor)

    def setSupervisor(self, supervisor):
        self.Supervisor = supervisor

    def setSalario(self):
        self.Salario = self.Salario + ((self.Salario * (self.INCREMENTO * self.Años))/100)

    def getSalario(self):
        return self.Salario

    def getSupervisor(self):
        return self.Supervisor

    def setAños(self, años):
        self.Años = años

    def getAños(self):
        return self.Años