from plus5 import *

def setup():
    size(500,500)

def keyPressed():
    print('keyPressed', keyCode)

def keyReleased():
    print('keyReleased')

def mousePressed():
    print('mousePressed')
    redraw()

def draw():
    background(127,0,0)
    stroke(0)
    circle(250,250,150)
    fill(0,255,0)
    fill(0,0,255)
    rect(mouseX-25,mouseY-25,50,50)
    stroke(255)
    text('Hola mundo', 100, 100)

run()
