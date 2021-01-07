# plus5

Python3 port of a subset of the Processing API.

Inspired by [p5](https://pypi.org/project/p5/), plus5 uses [PyGame](https://www.pygame.org/news) library to implement a subset of the [Processing API](https://py.processing.org/). It's in an early stage but works very fast, thanks to PyGame.

## Requirements

The current requirements are Python3 and PyGame. PyGame uses [Simple Directmedia Layer (SDL)](https://www.libsdl.org/). In order to use fonts, sdl2-ttf must be also installed in the systems.

- Python3
- PyGame
- libsdl2-ttf

plus5, Python3, PyGame and SDL are supported in *multiple operating systems* (Linux, Windows, Mac).

## Installation

### Using pip

```bash
$ pip install plus5
```

### Using git

```bash
$ git clone https://github.com/vrruiz/plus5/
$ cd plus5/
$ python3 setup.py install
```

### libsdl2-ttf

In some operating systems, this library must be installed manually.

## Usage

Example. A rectangle follows the mouse pointer.

```python
from plus5 import *

def setup():
    size(500,500)

def draw():
    background(127,0,0)
    stroke(255)
    fill(0,127,0)
    rect(mouseX - 25, mouseY - 25, 50, 50)

run()
```

## Reference

Usually, the calls are the same as in [Processing.py Reference](https://py.processing.org/reference/).

### Structure

```python
draw()
noLoop()
setup()
size(width, height)
redraw()
run()
```

### Environment
```python
delay(milliseconds)
displayHeight
displayWidth
frameCount
frameRate
height
size()
width
```

### Color

```python
background(color)
fill(color)
noFill()
noStroke()
stroke(width)
strokeWeight(weight)
```

### Input

```python
key
keyCode
keyIsPressed
keyPressed()
keyReleased()
mouseIsPressed
mousePressed()
mouseReleased()
mouseX
mouseY
pmouseX
pmouseY
```

### Shape

```python
arc(x, y, width, height, start, stop)
circle(a, b, extent)
ellipse(x, y, width, height)
line(x1, y1, x2, y2)
point(x, y)
quad(x1, y1, x2, y2, x3, y3, x4, y4)
rect(x, y, width, height)
square(a, b, extent)
triangle(x1, y1, x2, y2, x3, y3)
```

### Text

```python
text(string, x, y)
textSize(size)
textFont(font, size)
loadFont(name)
createFont(name, size)
```

### Constants
```python
PI = 3.14159265358979323846
TWO_PI = 6.28318530717958647693
HALF_PI =1.57079632679489661923
TAU = 6.28318530717958647693
HALF_PI = 0.7853982
```

## Author

Víctor R. Ruiz <rvr@linotipo.es>

## License

MIT
