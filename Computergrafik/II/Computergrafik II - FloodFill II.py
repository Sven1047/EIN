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

def floodfill4(x, y, alteFarbe, neueFarbe):
    # print("floodfill4(", x,",",y,",alteFarbe, neueFarbe))")
    if getpixelcolor(x, y) == alteFarbe:
        time.sleep(0.005)
        drawpixel(x, y, neueFarbe)
        floodfill4(x, y + PIXEL_SIZE, alteFarbe, neueFarbe)  # oben
        floodfill4(x, y - PIXEL_SIZE, alteFarbe, neueFarbe)  # unten
        floodfill4(x + PIXEL_SIZE, y, alteFarbe, neueFarbe)  # rechts
        floodfill4(x - PIXEL_SIZE, y, alteFarbe, neueFarbe)  # links
    
    # DIESEN CODE MUSST DU SCHREIBEN
    
def floodfill8(x, y, alteFarbe, neueFarbe):
    if getpixelcolor(x, y) == alteFarbe:
        time.sleep(0.005)
        drawpixel(x, y, neueFarbe)
        floodfill8(x, y + PIXEL_SIZE, alteFarbe, neueFarbe)  # oben
        floodfill8(x, y - PIXEL_SIZE, alteFarbe, neueFarbe)  # unten
        floodfill8(x + PIXEL_SIZE, y, alteFarbe, neueFarbe)  # rechts
        floodfill8(x - PIXEL_SIZE, y, alteFarbe, neueFarbe)  # links
        floodfill8(x + PIXEL_SIZE, y + PIXEL_SIZE, alteFarbe, neueFarbe)  #
        floodfill8(x - PIXEL_SIZE, y - PIXEL_SIZE, alteFarbe, neueFarbe)  #
        floodfill8(x + PIXEL_SIZE, y - PIXEL_SIZE, alteFarbe, neueFarbe)  #
        floodfill8(x - PIXEL_SIZE, y + PIXEL_SIZE, alteFarbe, neueFarbe)  #
    
def drawsquare(size, color):
    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, color)
        
    for i in range(size+1):
        drawpixel((size/2)*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, color)

    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, -1*(size/2)*PIXEL_SIZE, color)
        
    for i in range(size+1):
        drawpixel(-1*(size/2)*PIXEL_SIZE+i*PIXEL_SIZE, (size/2)*PIXEL_SIZE, color)


def drawing_prepare(mode):
    clear()
    
    # zeichne das schwarze Quadrat
    drawsquare(8, "black")

    # den rest
    drawpixel(-30,0,"black")
    drawpixel(-20,0,"black")

    drawpixel(0,-30,"black")
    drawpixel(0,-20,"black")

    drawpixel(30,0,"black")
    drawpixel(20,0,"black")

    drawpixel(0,30,"black")
    drawpixel(0,20,"black")

    drawpixel(-10,10,"black")
    drawpixel(10,-10,"black")
    
    up()
    goto(0,200)
    write(mode, font=("Verdana",15, "normal"))


def drawing_floodfill4(x,y):
    floodfill4(x,y,"white", "blue")

def drawing_floodfill8(x,y):
    floodfill8(x,y,"white", "blue")



clickcounter = 0
def mouse_clicked(x, y):
    x=round(x/PIXEL_SIZE)*PIXEL_SIZE
    y=round(y/PIXEL_SIZE)*PIXEL_SIZE
    global clickcounter
    if(clickcounter % 4 == 0):
        drawing_prepare("Floodfill 4")
    elif(clickcounter % 4 == 1):
        drawing_floodfill4(x,y)
    elif(clickcounter % 4 == 2):
        drawing_prepare("Floodfill 8 - zu implementieren!")
    elif(clickcounter % 4 == 3):
        drawing_floodfill8(x,y)
    clickcounter = clickcounter + 1 % 4;
    
onscreenclick(mouse_clicked)
mainloop()
done()