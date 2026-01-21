from turtle import *
import math

speed(0)
WINDOW_SIZE = 800

def main():
    paintCoordinateSystem()
    hideturtle()
    setup(WINDOW_SIZE,WINDOW_SIZE)
    width(5)

    positions = [ [100,100], [200,100], [200,200], [100,200] ]
    color("black")
    paintFigure(positions)

    color("blue")
    t = [50, 50]
    positions_translated = []
    
    # 1. TRANSLATION (Translation)
    # Hier wird die Translation angewendet - Siehe Slides zu Translation analytisch
    # Für jeden Punkt in der Liste "positions" wird zu x und y jeweils t[0] und t[1] hinzugerechnet
    for i in range(len(positions)):
        x = positions[i][0] + t[0]
        y = positions[i][1] + t[1]
        positions_translated.append([x,y])
    paintFigure(positions_translated)
      
    # 2. ROTATION (Drehung um den Ursprung (0,0))
    color("red")
    rho = 45 # Grad
    positions_rotated = []
    for i in range(len(positions)):
        # Analytische Rotationsformel
        x = positions[i][0]*cosinus(rho) - positions[i][1]*sinus(rho)
        y = positions[i][0]*sinus(rho) + positions[i][1]*cosinus(rho)
        positions_rotated.append([x,y])
    paintFigure(positions_rotated)

    # 3. SCALING (Skalierung um den Ursprung (0,0))
    color("green")
    s = [0.5, 0.5] # Skalierungsfaktoren für X und Y
    positions_scaled = []
    for i in range(len(positions)):
        # Analytische Skalierungsformel
        x = positions[i][0] * s[0]
        y = positions[i][1] * s[1]
        positions_scaled.append([x,y])
    paintFigure(positions_scaled)

    # 4. SHEARING (Scherung)
    color("orange")
    sh = [0.5, 0.5] # sh[0] für X-Abhängigkeit (Y-Scherung), sh[1] für Y-Abhängigkeit (X-Scherung)
    positions_sheared = []
    for i in range(len(positions)):
        # Analytische Scherungsformel (X-Scherung abhängig von Y, Y-Scherung abhängig von X)
        x = positions[i][0] + sh[1] * positions[i][1]
        y = positions[i][1] + sh[0] * positions[i][0]
        positions_sheared.append([x,y])
        
    # Die gescherten Punkte werden nun gezeichnet!
    paintFigure(positions_sheared)
    done()


def sinus(degrees):
    # Konvertiert Grad zu Bogenmass und berechnet den Sinus
    return math.sin(math.radians(degrees))
    
def cosinus(degrees):
    # Konvertiert Grad zu Bogenmass und berechnet den Cosinus
    return math.cos(math.radians(degrees))

def paintFigure(positions):
    for i in range(0, len(positions)):
        start = positions[i % len(positions)]
        end = positions[(i+1) % len(positions)]
        print("painting start:", start, " end:", end)
        penup()
        goto(start[0],start[1])
        pendown()
        goto(end[0],end[1])

def paintCoordinateSystem():
    width(2)
    penup()
    goto(-WINDOW_SIZE,0)
    pendown()
    goto(WINDOW_SIZE,0)
    penup()
    goto(0,-WINDOW_SIZE)
    pendown()
    goto(0,WINDOW_SIZE)
    
# Programm starten
main()
