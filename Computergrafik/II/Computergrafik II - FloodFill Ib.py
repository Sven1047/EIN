from turtle import *
import threading
import sys
speed(0)
hideturtle()
PIXEL_SIZE=10
sys.setrecursionlimit(2000)
import os
import time

setup(800,800)
    
def drawpixel(x, y, color):
    tracer(0, 0)
    up()
    goto(x,y)
    down()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(PIXEL_SIZE)
        right(90)
    end_fill()
    update()

def getpixelcolor(x, y):
    y = -y
    canvas = getcanvas()
    ids = canvas.find_overlapping(x+PIXEL_SIZE/2, y+PIXEL_SIZE/2, x+PIXEL_SIZE/2, y+PIXEL_SIZE/2)
    if ids: 
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color:
            return color
    return "white" # default color 

def floodfill(x, y, alteFarbe, neueFarbe):
    # print("floodfill(", x,",",y,",alteFarbe, neueFarbe))")
    if getpixelcolor(x, y) == alteFarbe:
        time.sleep(0.001)
        drawpixel(x, y, neueFarbe)
        floodfill(x, y + PIXEL_SIZE, alteFarbe, neueFarbe)  # oben
        floodfill(x, y - PIXEL_SIZE, alteFarbe, neueFarbe)  # unten
        floodfill(x + PIXEL_SIZE, y, alteFarbe, neueFarbe)  # rechts
        floodfill(x - PIXEL_SIZE, y, alteFarbe, neueFarbe)  # links

def drawsquare(size, color):
    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, color)
        
    for i in range(size+1):
        drawpixel((size/2)*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, color)

    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE, color)
        
    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, (size/2)*PIXEL_SIZE, color)


def drawing_prepare():
    clear()
    # zeichne das schwarze Quadrat
    drawsquare(20, "black")

    # zeichne das zweite schwarze Quadrat
    drawsquare(40, "black")

    # zeichne das dritte schwarze Quadrat
    drawsquare(200, "black")
    
    # loecher
    drawpixel(100,100,"white")
    drawpixel(90,100,"white")

def drawing_floodfill(x,y):
    floodfill(x,y,"white", "blue")


clickcounter = 0
def mouse_clicked(x, y):
    x=round(x/PIXEL_SIZE)*PIXEL_SIZE
    y=round(y/PIXEL_SIZE)*PIXEL_SIZE
    global clickcounter
    if(clickcounter % 2 == 0):
        drawing_prepare()
    elif(clickcounter % 2 == 1):
        drawing_floodfill(x,y)
    clickcounter = clickcounter + 1 % 2;
    
onscreenclick(mouse_clicked)
mainloop()
done()