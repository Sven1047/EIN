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

FRAMES_PER_SECOND = 10


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

    # wir definieren das Fenster
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Hintergrundfarbe Weiss
    glClearColor(1.0, 1.0, 1.0, 1.0)
 
    # Projektions-Perspektive
    gluPerspective(45, (display[0] / display[1]), 0.1, 10000.0)
    
    # Kameraposition
    glTranslatef(-1*camera_x, -1*camera_y, -1*camera_z)
    
    # Bewegungsparameter
    move_speed = 10


    # Endlosschlaufe
    while True:
        
        # Beginn jedes Render-Durchgangs - alles löschen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Achsen zeichnen
        zeichne_achsen()
        
        # Farbe des Würfels (linien) auf Schwarz (R=0, G=0, B=0) 
        glColor3f(0.0, 0.0, 0.0)

        # hier generieren wir den Würfel - am Nullpunkt
        for i in range(10):

            wuerfellinien = generiereWuerfel(i*100, 0, 0, 50)
        
        # Zeichne den Würfel
            glBegin(GL_LINES)
            for linie in wuerfellinien:
                for koordinaten in linie:
                    glVertex3fv(koordinaten)
            glEnd()

        for i in range(10):

            wuerfellinien = generiereWuerfel(0, 0, -i*100, 50)

            # Zeichne den Würfel
            glBegin(GL_LINES)
            for linie in wuerfellinien:
                for koordinaten in linie:
                    glVertex3fv(koordinaten)
            glEnd()


        # alle Events durchgehen
        for event in pygame.event.get():
            
            # Falls ich oben rechts das Fenster schliesse -> beende das Programm sofort
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Eingaben mit der Tastatur
            if event.type == pygame.KEYDOWN:
                
                # --- Y-Achsen-Bewegung (Hoch/Runter) ---
                if event.key == pygame.K_UP:
                    glTranslatef(0, -move_speed, 0)
                    camera_y += move_speed # Kamera Y-Koordinate steigt
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, move_speed, 0) 
                    camera_y -= move_speed # Kamera Y-Koordinate sinkt
                
                # --- X-Achsen-Bewegung (Links/Rechts) ---
                if event.key == pygame.K_LEFT:
                    glTranslatef(move_speed, 0, 0) 
                    camera_x -= move_speed
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-move_speed, 0, 0) 
                    camera_x += move_speed
                    
                # --- Z-Achsen-Steuerung (für die Tiefe/Zoom) ---
                # Tasten A/D für Z 
                if event.key == pygame.K_w: # Z-Achse vorwärts
                    glTranslatef(0, 0, move_speed) 
                    camera_z += move_speed
                if event.key == pygame.K_s: # Z-Achse rückwärts
                    glTranslatef(0, 0, -move_speed) 
                    camera_z += move_speed
                
                pos_text = "Camera:  " + str(camera_x)+ "," + str(camera_y) + str(",") + str(camera_z)
                pygame.display.set_caption(pos_text)
        
        
        
            
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
    glColor4f(1.0, 1.0, 1.0, 1.0) # Farbe zurücksetzen (oft gute Praxis)
    glLineWidth(1.0) # Etwas dicker für bessere Sichtbarkeit
    
    
if __name__ == '__main__':
    main()