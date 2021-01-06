import __main__
import builtins
import pygame
import time

# Private variables
_clock = None           # pygame clock
_screen = None          # pygame screen
_stroke = (255,255,255) # Default stroke
_fill = (255,255,255)   # Default fill
_no_fill = True         # No fill status
_no_stroke = True       # No stroke status

# Variables
builtins.width = 100    # Window size
builtins.height = 100   # Window size
builtins.mouseX = 0     # Mouse position
builtins.mouseY = 0     # Mouse position
builtins.pmouseY = 0    # Previous mouse position
builtins.pmouseY = 0    # Previous mouse position
builtins.mouseIsPressed = False # Mouse status
builtins.keyIsPressed = False   # Key status
builtins.key = ''             # Key used
builtins.keyCode = 0          # Key code

# Constants
builtins.PI = 3.14159265358979323846
builtins.TWO_PI = 6.28318530717958647693
builtins.HALF_PI =1.57079632679489661923
builtins.TAU = 6.28318530717958647693
builtins.HALF_PI = 0.7853982

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

def keyPressed():
    """ keyPressed """
    pass

def keyReleased():
    """ keyReleased """
    pass

def _get_color(args):
    r,g,b = (0,0,0)
    if len(args) == 1:
        r = args[0]
        g = args[0]
        b = args[0]
    elif len(args) == 3:
        r = args[0]
        g = args[1]
        b = args[2]
    else:
        raise "Incorrect number of parameters"
    return (r,g,b)

def background(*args):
    """ Background """
    global _screen
    r, g, b = _get_color(args)
    _screen.fill((r,g,b))

def stroke(*args):
    """ Set color for stroke """
    global _stroke, _no_stroke
    rgb = _get_color(args)
    _stroke = rgb
    _no_stroke = False

def noStroke():
    global _no_stroke
    _no_stroke = True

def fill(*args):
    global _fill, _no_fill
    rgb = _get_color(args)
    _fill = rgb
    _no_fill = False

def noFill():
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
        pygame.draw.line(_screen, _stroke, [x1, y1], [x2, y2])

def rect(*args):
    """ Rectangle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if len(args) == 4:
        pygame.draw.rect(_screen, _fill, list(args[:4]))

def square(a, b, extent):
    """ Square """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    square = [a, b, a + extent, b + extent]
    if _no_fill == False:
        pygame.draw.rect(_screen, _fill, square, width=0)
    if _no_stroke == False:
        pygame.draw.rect(_screen, _stroke, square, width=1)

def arc(*args):
    """ Arch """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if len(args) == 6:
        a,b,c,d,start,stop = args[:6]
        if _no_fill == False:
            pygame.draw.arc(_screen, _fill, [a,b,c,d], start, stop, 0)
        if _no_stroke == False:
            pygame.draw.arc(_screen, _stroke, [a,b,c,d], start, stop, width=1)

def circle(a,b,extent):
    """ Circle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if _no_fill == False:
        pygame.draw.circle(_screen, _fill, [a,b], extent, width=0)
    if _no_stroke == False:
        pygame.draw.circle(_screen, _stroke, [a,b], extent, width=1)

def ellipse(a, b, c, d):
    """ Ellipse """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    if _no_fill == False:
        pygame.draw.ellipse(_screen, _fill, [a,b,c,d], width=0)
    if _no_stroke == False:
        pygame.draw.ellipse(_screen, _stroke, [a,b,c,d], width=1)

def triangle(x1, y1, x2, y2, x3, y3):
    """ Triangle """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    points = [[x1,y1],[x2,y2],[x3,y3]]
    if _no_fill == False:
        pygame.draw.polygon(_screen, _fill, points, width=0)
    if _no_stroke == False:
        pygame.draw.polygon(_screen, _stroke, points, width=1)

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    """ Quad """
    global _screen, _stroke, _no_stroke, _fill, _no_fill
    points = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    if _no_fill == False:
        pygame.draw.polygon(_screen, _fill, points, width=0)
    if _no_stroke == False:
        pygame.draw.polygon(_screen, _stroke, points, width=1)

def run():
    """ Main loop """
    global _clock, _screen

    # Initialization
    pygame.init()
    pygame.display.set_caption('plus5')
    _screen = pygame.display.set_mode([100,100])
    _clock = pygame.time.Clock()
    frames_per_second = 25

    # Get handlers
    setup_func = setup
    if hasattr(__main__, 'setup'):
        setup_func = __main__.setup
    draw_func = draw
    if hasattr(__main__, 'draw'):
        draw_func = __main__.draw
    keyPressed_func = keyPressed
    if hasattr(__main__, 'keyPressed'):
        keyPressed_func = __main__.keyPressed
    keyReleased_func = keyReleased
    if hasattr(__main__, 'keyReleased'):
        keyReleased_func = __main__.keyReleased

    # Call setup
    setup_func()

    # Main loop (draw)
    running = True
    while running:
        # Wait
        _clock.tick(frames_per_second)
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
                keyPressed_func()
            if event.type == pygame.KEYUP:
                # Key released
                builtins.keyIsPressed = False
                # Call keyRelease() function
                keyReleased_func()
        # Update mouse positions and status
        builtins.mouseIsPressed = pygame.mouse.get_pressed()
        builtins.mouseX, builtins.mouseY = pygame.mouse.get_pos()
        builtins.pmouseX, builtins.pmouseY = pygame.mouse.get_pos()
        # Call draw() function
        draw_func()
        # Update screen
        pygame.display.update()

    # Exit
    pygame.quit()
