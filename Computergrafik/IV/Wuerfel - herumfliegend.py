import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from random import *


# die initiale Kameraposition
camera_x = 100
camera_y = 150
camera_z = 500

FRAMES_PER_SECOND = 24


def main():

    global punkte 
    global linien
    global camera_x
    global camera_y
    global camera_z

    pygame.init()
    
    # Breite und Höhe des Displays
    display = [800, 600]
    
    # Wir kreieren eine Uhr
    clock=pygame.time.Clock()

    
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Hintergrundfarbe Weiss
    glClearColor(1.0, 1.0, 1.0, 1.0)
 
    # Projektions-Perspektive
    gluPerspective(45, (display[0] / display[1]), 0.1, 10000.0)
    
    # Kameraposition
    glTranslatef(-1*camera_x, -1*camera_y, -1*camera_z)
    
    # Bewegungsparameter
    move_speed = 20
    
    # hier generieren wir die Würfel
    wuerfel = []
    directions = []
    anzahl_wuerfel = 4
    
    # Generiere Würfel alle an Punkt 0,0,0 - mit jeweils einer zufälligen Richtung
    for i in range(anzahl_wuerfel):
        seitenlaenge=50
        wuerfel_startpunkt_x = 0
        wuerfel_startpunkt_y = 0
        wuerfel_startpunkt_z = 0
        # generiere Wuerfellinien-Liste
        wuerfellinien = generiereWuerfel(wuerfel_startpunkt_x, wuerfel_startpunkt_y, wuerfel_startpunkt_z, seitenlaenge)
        # speichere jeweils in der Liste "wuerfel"
        wuerfel.append(wuerfellinien)
        # wähle eine zufällige Richtung
        directions.append([1,1,1])
        print(directions)
    
    # Endlosschlaufe
    while True:
        for event in pygame.event.get():
            
            # Falls ich oben rechts das Fenster schliesse -> beende das Programm sofort
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Eingaben mit der Tastatur
            if event.type == pygame.KEYDOWN:
                
                # --- Y-Achsen-Bewegung (Hoch/Runter) ---
                if event.key == pygame.K_UP:
                    # GL: Welt bewegt sich nach unten (-Y) -> Kamera bewegt sich nach oben
                    glTranslatef(0, -move_speed, 0)
                    camera_y += move_speed # Kamera Y-Koordinate steigt
                if event.key == pygame.K_DOWN:
                    # GL: Welt bewegt sich nach oben (+Y) -> Kamera bewegt sich nach unten
                    glTranslatef(0, move_speed, 0) 
                    camera_y -= move_speed # Kamera Y-Koordinate sinkt
                
                # --- X-Achsen-Bewegung (Links/Rechts) ---
                if event.key == pygame.K_LEFT:
                    # GL: Welt bewegt sich nach rechts (+X) -> Kamera bewegt sich nach links
                    glTranslatef(move_speed, 0, 0) 
                    camera_x -= move_speed
                if event.key == pygame.K_RIGHT:
                    # GL: Welt bewegt sich nach links (-X) -> Kamera bewegt sich nach rechts
                    glTranslatef(-move_speed, 0, 0) 
                    camera_x += move_speed
                    
                # --- Z-Achsen-Steuerung (für die Tiefe/Zoom) ---
                # Tasten A/D für Z 
                if event.key == pygame.K_w: # Z-Achse vorwärts (optional)
                    # GL: Welt bewegt sich weg (+Z) -> Kamera bewegt sich vorwärts
                    glTranslatef(0, 0, move_speed) 
                    camera_z += move_speed
                if event.key == pygame.K_s: # Z-Achse rückwärts (optional)
                    # GL: Welt bewegt sich näher (-Z) -> Kamera bewegt sich rückwärts
                    glTranslatef(0, 0, -move_speed) 
                    camera_z -= move_speed
                
                pos_text = "Camera:  " + str(camera_x)+ "," + str(camera_y) + str(",") + str(camera_z)
                pygame.display.set_caption(pos_text)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # [NEU]: Achsen zeichnen
        zeichne_achsen()

        # LINIENFARBE AUF SCHWARZ (R=0, G=0, B=0) SETZEN
        # Wichtig: Diese Farbanweisung kommt nach zeichne_achsen(),
        # damit die Achsen ihre Rot/Grün/Blau-Farben behalten.
        glColor3f(0.0, 0.0, 0.0)
        
        # Zeichne die Würfel
        glBegin(GL_LINES)
        for wuerfellinien in wuerfel:
            for linie in wuerfellinien:
                for koordinaten in linie:
                    glVertex3fv(koordinaten)
        glEnd()
        
        
        # Wir verschieben die Würfel immer um deren "direction"
        for i in range(len(wuerfel)):
            wuerfellinien = wuerfel[i]
            direction = directions[i]
            for linie in wuerfellinien:
                for koordinaten in linie:
                    koordinaten[1] = koordinaten[1]+direction[0]
                    koordinaten[2] = koordinaten[2]+direction[1]
                    koordinaten[0] = koordinaten[0]+direction[2]
        
            
        clock.tick(FRAMES_PER_SECOND)
        
        pygame.display.flip()
        pygame.time.wait(10)


def generiereWuerfel(wuerfel_startpunkt_x, wuerfel_startpunkt_y, wuerfel_startpunkt_z, seitenlaenge):
    
    SEITE = seitenlaenge

    linien = [
        # Vorderes Quadrat
        [[0, 0, 0], [SEITE, 0, 0]],
        [[SEITE, 0, 0], [SEITE, SEITE, 0]],
        [[SEITE, SEITE, 0], [0, SEITE, 0]],
        [[0, SEITE, 0], [0, 0, 0]],
        
        # Hinteres Quadrat
        [[0, 0, SEITE], [SEITE, 0, SEITE]],
        [[SEITE, 0, SEITE], [SEITE, SEITE, SEITE]],
        [[SEITE, SEITE, SEITE], [0, SEITE, SEITE]],
        [[0, SEITE, SEITE], [0, 0, SEITE]],
        
        # Verknüpfung der Quadrate
        [[0, 0, 0], [0, 0, SEITE]],
        [[SEITE, 0, 0], [SEITE, 0, SEITE]],
        [[SEITE, SEITE, 0], [SEITE, SEITE, SEITE]],
        [[0, SEITE, 0], [0, SEITE, SEITE]],    
    ]

    for i in range(len(linien)):
        linie = linien[i]
        
        anfang = linie[0]
        ende = linie[1]
        
        anfang[0] = anfang[0] + wuerfel_startpunkt_x
        ende[0] = ende[0] + wuerfel_startpunkt_x
        
        anfang[1] = anfang[1] + wuerfel_startpunkt_y
        ende[1] = ende[1] + wuerfel_startpunkt_y
        
        anfang[2] = anfang[2] + wuerfel_startpunkt_z
        ende[2] = ende[2] + wuerfel_startpunkt_z
    
    return linien

# [NEU]: Funktion zum Zeichnen der Achsen
def zeichne_achsen():
    glLineWidth(2.0) # Etwas dicker für bessere Sichtbarkeit
    glBegin(GL_LINES)
    
    # X-Achse (Rot)
    glColor4f(1.0, 0.0, 0.0, 1.0) # Rot
    glVertex3f(-10000.0, 0.0, 0.0)
    glVertex3f(10000.0, 0.0, 0.0)
    
    # Y-Achse (Grün)
    glColor4f(0.0, 1.0, 0.0, 1.0) # Grün
    glVertex3f(0.0, -10000.0, 0.0)
    glVertex3f(0.0, 10000.0, 0.0)
    
    # Z-Achse (Blau)
    glColor4f(0.0, 0.0, 1.0, 1.0) # Blau
    glVertex3f(0.0, 0.0, -10000.0)
    glVertex3f(0.0, 0.0, 10000.0)
    
    glEnd()
    # Wichtig: Die Linienfarbe wird hier nicht auf Weiß zurückgesetzt,
    # da wir danach explizit glColor3f(0.0, 0.0, 0.0) für die Würfel setzen.
    glLineWidth(1.0) # Linienstärke zurücksetzen (für zukünftige Objekte)

if __name__ == '__main__':
    main()