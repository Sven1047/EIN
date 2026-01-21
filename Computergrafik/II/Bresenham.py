from turtle import *

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
    
    print("Mouse clicked at ", x, ",", y)
    
    # First click sets (x1, y1)
    if x1 is None:
        x1 = grid_x
        y1 = grid_y
        # Draw the first point
        drawpixel(x1, y1, "red") 
    
    # Second click sets (x2, y2) and triggers line drawing
    elif x2 is None:
        x2 = grid_x
        y2 = grid_y
        
        # Draw the second point
        drawpixel(x2, y2, "blue") 
        
        # Draw the line
        bres(x1, y1, x2, y2)
        
        # Reset points for the next line
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        
        print("Line drawn. Points reset. Click again for a new line.")
        

def drawpixel(grid_x, grid_y, color):
    screen_x = grid_x * PIXEL_SIZE
    screen_y = grid_y * PIXEL_SIZE

    tracer(0, 0) # Turn off screen updates
    up()
    goto(screen_x, screen_y) 
    down()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for z in range(4):
        forward(PIXEL_SIZE)
        right(90)
    end_fill()
    up()
    update() # Force screen update


def drawsquare(size, color):
    half_size_p = (size / 2) * PIXEL_SIZE

    for i in range(size + 1):
        # Left edge
        drawpixel(round((-half_size_p) / PIXEL_SIZE), round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), color)
        # Right edge
        drawpixel(round(half_size_p / PIXEL_SIZE), round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), color)
        # Bottom edge
        drawpixel(round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), round((-half_size_p) / PIXEL_SIZE), color)
        # Top edge
        drawpixel(round((-half_size_p + i * PIXEL_SIZE) / PIXEL_SIZE), round(half_size_p / PIXEL_SIZE), color)


def drawing_prepare():
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

def bres(x1,y1,x2,y2):
    # Bresenham's Line Algorithm adapted for turtle drawing
    x,y = x1,y1
    
    # Determine the step direction
    if x2 > x1:
        sx = 1
    else:
        sx = -1

    if y2 > y1:
        sy = 1
    else:
        sy = -1
    
    # get the absolute value
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    
    if dx > dy:
        # Shallow slope (dx > dy)
        p = 2 * dy - dx
        
        # Loop 
        while x != x2 or y != y2:
            drawpixel(x, y, "black")
            
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            x += sx
        
    else:
        # Steep slope (dy >= dx)
        p = 2 * dx - dy
        
        # Loop for steep slope
        while x != x2 or y != y2:
            drawpixel(x, y, "black")
            
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            y += sy

    # Draw the end point (since the loop condition might exit before it's drawn)
    drawpixel(x2, y2, "black") 
    print("Bresenham line drawn.")

# Run the main function
if __name__ == "__main__":
    main()