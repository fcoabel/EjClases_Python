from claseForma import *

class Rectangulo(Forma):
    ladoMayor = 0
    ladoMenor = 0

    def __init__(self, color, x, y, nombre, ladoMayor, ladoMenor):
        super(Rectangulo, self).__init__(color, x, y, nombre)
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def imprimir(self):
        print("rectangulo: ", self.nombre,
              "\nColor: ", self.color,
              "\nCentro: ", self.coordenadaCentro.get_x, self.coordenadaCentro.get_y,
              "\nLado Mayor: ", self.ladoMayor,
              "\nLado Menor: ", self.ladoMenor)

    def area(self):
        area = self.ladoMayor * self.ladoMenor
        return area

    def perimetro(self):
        perimetro = (2 * self.ladoMayor) + (2 * self.ladoMayor)
        return perimetro

    def modificar(self, factor):
        self.ladoMayor = self.ladoMayor * factor
        self.ladoMenor = self.ladoMenor * factor