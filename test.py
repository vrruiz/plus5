from plus5 import *

def setup():
    size(500,500)
    stroke(255)
    fill(127)

def keyPressed():
    print('keyPressed', keyCode)

def keyReleased():
    print('keyReleased')

def draw():
    background(127,0,0)
    line(0,0,width,height)
    rect(mouseX-25, mouseY-25,50,50)

run()
