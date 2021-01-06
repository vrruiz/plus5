import __main__
import builtins
import pygame
import time

_clock = None           # pygame clock
_screen = None          # pygame screen
_stroke = (255,255,255) # Default stroke
_fill = (255,255,255)   # Default fill

builtins.width = 100
builtins.height = 100

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
    global _stroke
    rgb = _get_color(args)
    _stroke = rgb

def fill(*args):
    global _fill
    rgb = _get_color(args)
    _fill = rgb

def line(x1, y1, x2, y2):
    """ Draw line """
    global _screen, _stroke
    pygame.draw.line(_screen, _stroke, [x1, y1], [x2, y2])

def rect(*args):
    """ Rectangle """
    global _screen, _stroke, _fill
    if len(args) == 4:
        pygame.draw.rect(_screen, _fill, list(args[:4]))

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

    # Call setup
    setup_func()

    # Main loop (draw)
    running = True
    while running:
        _clock.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_func()
        pygame.display.flip()

    # Exit
    pygame.quit()
