from rectangulo import *

class Cuadrado(Rectangulo):
    lado = 0

    def __init__(self, color, x, y, nombre, lado):
        self.lado = ladoMayor = ladoMenor = lado
        super(Cuadrado, self).__init__(color, x, y, nombre, ladoMayor, ladoMenor)

