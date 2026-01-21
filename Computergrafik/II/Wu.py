from turtle import *
import math 

PIXEL_SIZE = 10
WINDOW_X = 800
WINDOW_Y = 800

x1 = None
y1 = None
x2 = None
y2 = None

clickedx = None
clickedy = None

def main():
    # Set up the screen and turtle
    speed(0)
    setup(WINDOW_X, WINDOW_Y)
    colormode(255) # Stellen Sie den Farbmodus auf 255 ein, damit Hex-Farben korrekt funktionieren
    drawing_prepare()
    
    # Register the click handler
    onscreenclick(mouse_clicked)
    
    print("waiting for two clicks to define a line segment...")
    # The done() call is essential to keep the window open and responsive
    done()

def mouse_clicked(x, y):
    # Round to the nearest grid cell coordinate
    grid_x = round(x / PIXEL_SIZE)
    grid_y = round(y / PIXEL_SIZE)
    
    global x1, x2, y1, y2
    
    print(f"Mouse clicked at raw ({x:.2f}, {y:.2f}) -> grid ({grid_x}, {grid_y})")
    
    # First click sets (x1, y1)
    if x1 is None:
        x1 = grid_x
        y1 = grid_y
        # drawpixel(x1, y1, 1.0, "red") # <-- DIESER AUFRUF WURDE ENTFERNT
        print(f"x1, y1 set to ({x1}, {y1})")
    
    # Second click sets (x2, y2) and triggers line drawing
    elif x2 is None:
        x2 = grid_x
        y2 = grid_y
        
        # drawpixel(x2, y2, 1.0, "blue") # <-- DIESER AUFRUF WURDE ENTFERNT
        print(f"x2, y2 set to ({x2}, {y2})")
        
        # Draw the line
        wu(x1, y1, x2, y2)
        
        # Reset points for the next line
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        
        print("Wu-Line drawn. Points reset. Click again for a new line.")

def drawpixel(grid_x, grid_y, intensity, base_color="black"):
    """
    Zeichnet ein Pixel mit einer bestimmten Intensität (0.0 bis 1.0).
    """
    if base_color == "black":
        # Konvertiere Intensität (0.0-1.0) in Graustufen (0-255)
        gray_value = int(255 * (1.0 - intensity))
        gray_value = max(0, min(255, gray_value))
        
        hex_color = f'#{gray_value:02x}{gray_value:02x}{gray_value:02x}'
        p_color = hex_color
    else:
        # Für Start- und Endpunkte einfach die feste Farbe verwenden
        p_color = base_color
        
    screen_x = grid_x * PIXEL_SIZE
    screen_y = grid_y * PIXEL_SIZE

    tracer(0, 0)
    up()
    goto(screen_x, screen_y)  
    down()
    pencolor(p_color)
    fillcolor(p_color)
    begin_fill()
    for _ in range(4):
        forward(PIXEL_SIZE)
        right(90)
    end_fill()
    up()
    update()

def drawing_prepare():
    """Zeichnet die X- und Y-Achse auf den Bildschirm."""
    up()
    # Draw X-axis
    goto(-WINDOW_X/2,0)
    down()
    goto(WINDOW_X/2,0)
    up()
    # Draw Y-axis
    goto(0, -WINDOW_Y/2)
    down()
    goto(0, WINDOW_Y/2)
    up()

def drawsquare(size, color):
    """Zeichnet ein leeres Quadrat (wie in Ihrem Originalcode)."""
    half_size_p = (size / 2) * PIXEL_SIZE

    for i in range(size + 1):
        # Left edge
        drawpixel(round((-half_size_p) / PIXEL_SIZE), round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), 1.0, color)
        # Right edge
        drawpixel(round(half_size_p / PIXEL_SIZE), round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), 1.0, color)
        # Bottom edge
        drawpixel(round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), round((-half_size_p) / PIXEL_SIZE), 1.0, color)
        # Top edge
        drawpixel(round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), round(half_size_p / PIXEL_SIZE), 1.0, color)

# Hilfsfunktionen für Wu-Algorithmus
def ipart(x):
    return int(x)

def round_int(x):
    return ipart(x + 0.5)

def fpart(x):
    return x - math.floor(x)

def rfpart(x):
    return 1 - fpart(x)


def wu(x1, y1, x2, y2):
    """
    Implementiert den Wu-Antialiasing-Algorithmus.
    """
    
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    
    steep = abs(y2 - y1) > abs(x2 - x1)
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0.0:
        gradient = 1.0
    else:
        gradient = dy / dx

    # Erster Endpunkt
    xend = round_int(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = rfpart(x1 + 0.5)
    
    xpxl1 = xend    
    ypxl1 = ipart(yend) 
    
    if steep:
        drawpixel(ypxl1, xpxl1, rfpart(yend) * xgap, "black")
        drawpixel(ypxl1 + 1, xpxl1, fpart(yend) * xgap, "black")
    else:
        drawpixel(xpxl1, ypxl1, rfpart(yend) * xgap, "black")
        drawpixel(xpxl1, ypxl1 + 1, fpart(yend) * xgap, "black")
        
    intery = yend + gradient

    # Hauptschleife
    xend = round_int(x2)
    
    for x in range(xpxl1 + 1, xend):
        y = intery
        y_int = ipart(y)
        
        if steep:
            drawpixel(y_int, x, rfpart(y), "black")
            drawpixel(y_int + 1, x, fpart(y), "black")
        else:
            drawpixel(x, y_int, rfpart(y), "black")
            drawpixel(x, y_int + 1, fpart(y), "black")
            
        intery += gradient
    
    # Letzter Endpunkt
    yend = y2
    xgap = fpart(x2 + 0.5)
    
    xpxl2 = xend
    ypxl2 = ipart(yend)
    
    if steep:
        drawpixel(ypxl2, xpxl2, rfpart(yend) * xgap, "black")
        drawpixel(ypxl2 + 1, xpxl2, fpart(yend) * xgap, "black")
    else:
        drawpixel(xpxl2, ypxl2, rfpart(yend) * xgap, "black")
        drawpixel(xpxl2, ypxl2 + 1, fpart(yend) * xgap, "black")

    print("Wu-Line drawn.")

# Run the main function
if __name__ == "__main__":
    main()