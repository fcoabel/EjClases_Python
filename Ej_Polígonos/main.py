import circulo
import cuadrado
import elipse
import rectangulo

if __name__ == '__main__':
    r = rectangulo.Rectangulo("Morado", 1, 1, "Rectangulo", 4, 6)
    cu = cuadrado.Cuadrado("Violeta", 7 ,7 ,"Cuadrado", 5)
    ci = circulo.Circulo("Amarillo", 18, 18, "Círculo", 3)
    el = elipse.Elipse("Verde", 21, 21, "Elipse", 3, 2)

    lista = [r, cu, ci, el]

    for i in lista:
        i.setcolor("Azul")
        i.mover(25, 30)

    for i in lista:
        i.imprimir()