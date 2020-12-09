from elipse import *
from math import sqrt

class Circulo(Elipse):
    radio = 0

    def __init__(self, color, x, y, nombre, radio):
        self.radio = radio
        super(Circulo, self).__init__(color, x, y, nombre, radio, radio)

    def area(self):
        area = math.pi * sqrt(self.radio)
        return area