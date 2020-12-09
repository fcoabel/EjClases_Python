class Forma:
    color = ""
    coordenada = 0
    nombre = ""

    def __init__(self, color, x, y, nombre):
        self.color = color
        Punto().init(x, y)
        self.nombre = nombre

    def imprimir(self):
        print("Nombre: ", self.nombre,
              "\nColor: ", self.color,
              "\nCoordenada: ", self.coordenadaCentro)

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def mover(self, x, y):
        self.coordenadaCentro.set_x(x)
        self.coordenadaCentro.set_y(y)


class Punto:
    x = 0
    y = 0

    def init(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
