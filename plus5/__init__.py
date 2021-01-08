import __main__
import builtins
import os
import pygame
import time

from math import ceil, exp, floor, log, sqrt
from math import acos, asin, atan, atan2, cos, degrees, radians, sin, tan

# Private variables
_clock = None               # pygame clock
_screen = None              # pygame screen
_font = None                # pygame font
_font_name = None           # Font name
_font_size = 20             # Font size
_font_cache = []            # pygame fonts
_no_loop = False            # Execute draw
_stroke = (255,255,255)     # Default stroke
_stroke_weight = 1          # Stroke weight
_fill = (255,255,255)       # Default fill
_no_fill = True             # No fill status
_no_stroke = True           # No stroke status
_setup_func = None          # setup function
_draw_func = None           # draw function
_keyPressed_func = None     # keyPressed function
_keyReleased_func = None    # keyReleased function
_mousePressed_func = None   # keyPressed function
_mouseReleased_func = None  # keyReleased function

# Variables
builtins.displayWidth = 0       # Display size
builtins.displayHeight = 0      # Display size
builtins.width = 100            # Window size
builtins.height = 100           # Window size
builtins.frameCount = 0         # Frame count
builtins.frameRate = 30         # Frame count
builtins.mouseX = 0             # Mouse position
builtins.mouseY = 0             # Mouse position
builtins.pmouseY = 0            # Previous mouse position
builtins.pmouseY = 0            # Previous mouse position
builtins.mouseIsPressed = False # Mouse status
builtins.keyIsPressed = False   # Key status
builtins.key = ''               # Key used
builtins.keyCode = 0            # Key code

# Constants
builtins.PI = 3.14159265358979323846
builtins.TWO_PI = 6.28318530717958647693
builtins.HALF_PI =1.57079632679489661923
builtins.TAU = 6.28318530717958647693
builtins.HALF_PI = 0.7853982


class PFont():
    """ Class PFont """

    def __init__(self, font):
        """ Store font """
        self.font = font


class PImage():
    """ Class PImage """

    def __init__(self):
        """ Initalization """
        self.image = None
        self.width = 0
        self.height = 0

    def load_image(self, filename):
        """ Load image """
        self.image = pygame.image.load(filename)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

def size(w,h):
    """ Set window size """
    global _screen
    _screen = pygame.display.set_mode([w,h])
    builtins.width = w
    builtins.height = h

def setup():
    """ Setup """
    size(100,100)

def draw():
    """ Draw """
    pass

def redraw():
    """ Redraw """
    global _draw_func
    if _draw_func:
        builtins.frameCount = builtins.frameCount + 1
        _draw_func()

def noLoop():
    """ noLoop """
    global _no_loop
    _no_loop = True

def keyPressed():
    """ keyPressed """
    pass

def keyReleased():
    """ keyReleased """
    pass

def mousePressed():
    """ mousePressed """
    pass

def mouseReleased():
    """ mouseReleased """
    pass

def color(*args):
    """ color """
    if len(args) == 1:
        return args[0], args[0], args[0]
    elif len(args) == 3:
        return args[:3]
    elif len(args) == 4:
        return args[:4]
    else:
        raise "Incorrect number of parameters"

def background(*args):
    """ Background """
    global _screen
    c = color(*args)
    _screen.fill(c)

def stroke(*args):
    """ Set color for stroke """
    global _stroke, _no_stroke
    _stroke = color(*args)
    _no_stroke = False

def strokeWeight(weight):
    """ strokeWeight() """
    global _stroke_weight
    _stroke_weight = weight

def noStroke():
    """ noStroke """
    global _no_stroke
    _no_stroke = True

def fill(*args):
    """ Fill """
    global _fill, _no_fill
    _fill = color(*args)
    _no_fill = False

def noFill():
    """ noFill """
    global _no_fill
    _no_fill = True

def point(x, y):
    """ Point """
    global _screen, _stroke, _no_stroke
    if _no_stroke == False:
        pygame.draw.line(_screen, _stroke, [x, y], [x, y])

def line(x1, y1, x2, y2):
    """ Draw line """
    global _screen, _stroke, _no_stroke
    if _no_stroke == False:
        pygame.draw.line(_screen, _stroke, [x1, y1], [x2, y2], _stroke_weight)

def rect(*args):
    """ Rectangle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if len(args) == 4:
        pygame.draw.rect(_screen, _fill, list(args[:4]), _stroke_weight)

def square(a, b, extent):
    """ Square """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    square = [a, b, a + extent, b + extent]
    if _no_fill == False:
        pygame.draw.rect(_screen, _fill, square, 0)
    if _no_stroke == False:
        pygame.draw.rect(_screen, _stroke, square, _stroke_weight)

def arc(*args):
    """ Arch """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if len(args) == 6:
        a,b,c,d,start,stop = args[:6]
        if _no_fill == False:
            pygame.draw.arc(_screen, _fill, [a,b,c,d], start, stop, 0)
        if _no_stroke == False:
            pygame.draw.arc(_screen, _stroke, [a,b,c,d], start, stop, _stroke_weight)

def circle(a,b,extent):
    """ Circle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if _no_fill == False:
        pygame.draw.circle(_screen, _fill, [a,b], int(extent / 2), 0)
    if _no_stroke == False:
        pygame.draw.circle(_screen, _stroke, [a,b], int(extent / 2), _stroke_weight)

def ellipse(a, b, c, d):
    """ Ellipse """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if _no_fill == False:
        pygame.draw.ellipse(_screen, _fill, [a,b,c,d], 0)
    if _no_stroke == False:
        pygame.draw.ellipse(_screen, _stroke, [a,b,c,d], _stroke_weight)

def triangle(x1, y1, x2, y2, x3, y3):
    """ Triangle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    points = [[x1,y1],[x2,y2],[x3,y3]]
    if _no_fill == False:
        pygame.draw.polygon(_screen, _fill, points, 0)
    if _no_stroke == False:
        pygame.draw.polygon(_screen, _stroke, points, _stroke_weight)

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    """ Quad """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    points = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    if _no_fill == False:
        pygame.draw.polygon(_screen, _fill, points, 0)
    if _no_stroke == False:
        pygame.draw.polygon(_screen, _stroke, points, _stroke_weight)

def text(string, x, y):
    """ Text """
    global _screen, _font, _stroke
    alpha = 255
    if len(_stroke) == 4:
        alpha = _stroke[3]
    text_render = _font.render(string, True, _stroke)
    text_render.set_alpha(alpha)
    _screen.blit(text_render, [x,y])
 
def textSize(size):
    """ textSize """
    global _font, _font_name, _font_size
    _font_size = size
    _font = pygame.font.SysFont(_font_name, _font_size)

def textFont(font, size=None):
    """ textFont """
    global _font, _font_name, _font_size
    if type(font) == str and size is not None:
        font = createFont(font, size)
        _font_name = font
        _font_size = size
    if type(font) == PFont:
        _font = font.font

def loadFont(font_name):
    """ loadFont """
    fonts = pygame.font.get_fonts()
    if font_name.lower() in fonts:
        return font_name
    else:
        return None

def createFont(name, size):
    """ createFont """
    font = pygame.font.SysFont(name, size)
    pfont = PFont(font)
    return pfont

def delay(ms):
    """ Delay """
    time.sleep(ms/1000.0)

def save(filename):
    """ Save """
    global _screen
    if filename.lower().endswith('.png'):
        pygame.image.save(_screen, filename)
    else:
        raise "Only PNG image format supported"

def loadImage(filename):
    """ loadImage """
    img = PImage()
    img.load_image(filename)
    return img

def image(img, x, y):
    """ image """
    global _screen
    _screen.blit(img.image, [x, y])

def _init():
    """ Initialization """
    global _clock, _screen, _no_loop, _font_size
    global _setup_func, _draw_func, _keyPressed_func, _keyReleased_func
    global _mousePressed, _mousedReleased

    # PyGame unitialization
    pygame.init()
    pygame.display.set_caption('Plus5')
    _screen = pygame.display.set_mode([100,100])
    _clock = pygame.time.Clock()

    display_info = pygame.display.Info()
    builtins.displayWidth = display_info.current_w
    builtins.displayHeight = display_info.current_h

    # Set defaults
    background(200)
    textSize(_font_size)

    # Get handlers
    _setup_func = setup
    if hasattr(__main__, 'setup'):
        _setup_func = __main__.setup
    _draw_func = draw
    if hasattr(__main__, 'draw'):
        _draw_func = __main__.draw
    _keyPressed_func = keyPressed
    if hasattr(__main__, 'keyPressed'):
        _keyPressed_func = __main__.keyPressed
    _keyReleased_func = keyReleased
    if hasattr(__main__, 'keyReleased'):
        _keyReleased_func = __main__.keyReleased
    if hasattr(__main__, 'mousePressed'):
        _mousePressed_func = __main__.mousePressed
    _mouseReleased_func = mouseReleased
    if hasattr(__main__, 'mouseReleased'):
        _mouseReleased_func = __main__.mouseReleased

    # Call setup
    _setup_func()

    # Update screen
    pygame.display.update()


def _loop():
    """ Loop (draw) """
    # Main loop (draw)
    running = True
    while running:
        # Update mouse positions and status
        builtins.mouseX, builtins.mouseY = pygame.mouse.get_pos()
        builtins.pmouseX, builtins.pmouseY = pygame.mouse.get_pos()
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit
                running = False
            if event.type == pygame.KEYDOWN:
                # Key pressed
                builtins.keyIsPressed = True
                builtins.key = event.key  # Numeric code
                builtins.keyCode = pygame.key.name(event.key)  # String code
                if len(builtins.keyCode) > 1:
                    builtins.keyCode = builtins.keyCode.upper()
                # Call keyPressed() function
                _keyPressed_func()
            if event.type == pygame.KEYUP:
                # Key released
                builtins.keyIsPressed = False
                # Call keyRelease() function
                _keyReleased_func()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse pressed
                builtins.mouseIsPressed = True
                # Call keyRelease() function
                _mousePressed_func()
            if event.type == pygame.MOUSEBUTTONUP:
                # Mouse pressed
                builtins.mouseIsPressed = False
                # Call mouseReleased() function
                _mouseReleased_func()
        # Call draw() function
        if _no_loop == False:
            builtins.frameCount = builtins.frameCount + 1
            _draw_func()
        # Update screen
        pygame.display.update()
        # Wait
        _clock.tick(builtins.frameRate)

def _end():
    """ Finish """
    # Exit PyGame
    pygame.quit()

def run():
    """ Main loop """
    # Initialization
    _init()

    # Main loop
    _loop()

    # Exit
    _end()
