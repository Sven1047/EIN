from turtle import *
import math

# Grösse des Fensters
WINDOW_SIZE = 800

setup(WINDOW_SIZE, WINDOW_SIZE)
speed(0)
hideturtle()

# Projektion
SKALIERUNG = 0.5
NEIGUNG_IN_GRAD = 45

def main():
    paintCoordinateSystem()
    color("black")
    width(5)
    
    # Startpunkt (Offset) des Würfels
    offset_x = 50
    offset_y = 50
    offset_z = 0

    # Vordere Ecken des Würfels
    pos0 = [100, 100, 0]
    pos1 = [100, 200, 0]
    pos2 = [200, 200, 0]
    pos3 = [200, 100, 0]
    
    paintPoint(pos0)
    paintPoint(pos1)
    paintPoint(pos2)
    paintPoint(pos3)

    # Hintere Ecken des Würfels
    pos4 = [100, 100, 100]
    pos5 = [100, 200, 100]
    pos6 = [200, 200, 100]
    pos7 = [200, 100, 100]
    
    paintPoint(pos4)
    paintPoint(pos5)
    paintPoint(pos6)
    paintPoint(pos7)

    drawLine([pos0, pos1, pos2, pos3, pos0])
    drawLine([pos0, pos4])
    drawLine([pos1, pos5])
    drawLine([pos2, pos6])
    drawLine([pos3, pos7])
    drawLine([pos4, pos5, pos6, pos7, pos4])


    
    done()

# Projiziert einen 3D-Punkt (x, y, z) auf 2D mittels Kavalierprojektion
def paintPoint(pos):
    global SKALIERUNG
    global NEIGUNG_IN_GRAD
    
    # Kavalierprojektion Formel (NEIGUNG)
    xproj = pos[0] + pos[2] * SKALIERUNG * cosinus(NEIGUNG_IN_GRAD)
    yproj = pos[1] + pos[2] * SKALIERUNG * sinus(NEIGUNG_IN_GRAD)
    
    penup()
    goto(xproj, yproj)
    pendown()
    dot(5, "blue") # Zeichne blauen Punkt
    
# Zeichnet eine Linie im 3D Raum
def drawLine(pos):
    global SKALIERUNG
    global NEIGUNG_IN_GRAD

    color("black")
    width(1)
    for i in range(len(pos)-1):
        posa = pos[i]
        posb = pos[i+1]
    # Kavalierprojektion Formel (NEIGUNG)
        xproja = posa[0] + posa[2] * SKALIERUNG * cosinus(NEIGUNG_IN_GRAD)
        yproja = posa[1] + posa[2] * SKALIERUNG * sinus(NEIGUNG_IN_GRAD)

    # Kavalierprojektion Formel (NEIGUNG)
        xprojb = posb[0] + posb[2] * SKALIERUNG * cosinus(NEIGUNG_IN_GRAD)
        yprojb = posb[1] + posb[2] * SKALIERUNG * sinus(NEIGUNG_IN_GRAD)

        penup()
        goto(xproja,yproja)
        pendown()
        goto(xprojb,yprojb)


# Zeichnet die x-, y- und projizierte z-Achse.
def paintCoordinateSystem():
    color("gray")
    width(1)
    # x-Achse (Horizontal)
    penup()
    goto(-WINDOW_SIZE/2, 0)
    pendown()
    goto(WINDOW_SIZE/2, 0)
    # y-Achse (Vertikal)
    penup()
    goto(0, -WINDOW_SIZE/2)
    pendown()
    goto(0, WINDOW_SIZE/2)
    penup()
    goto(0, 0)
    pendown()

# Konvertiert Grad zu Bogenmass und berechnet den Sinus
def sinus(degrees):
    return math.sin(math.radians(degrees))
    
# Konvertiert Grad zu Bogenmass und berechnet den Cosinus
def cosinus(degrees):
    return math.cos(math.radians(degrees))

# Programm starten
main()