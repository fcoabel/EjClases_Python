from claseForma import *
import math


class Elipse(Forma):
    radioMayor = 0
    radioMenor = 0

    def __init__(self, color, x, y, nombre, radioMayor, radioMenor):
        super(Elipse, self).__init__(color, x, y, nombre)
        self.radioMayor = radioMayor
        self.radioMenor = radioMenor

    def area(self):
        area = math.pi * (self.radioMayor * self.radioMenor)
        return area
