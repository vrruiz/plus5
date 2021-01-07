# plus5

Native Python port of a subset of the Processing API.

This is a proof of concept. Based on ideas of [p5](https://pypi.org/project/p5/), it uses [PyGame](https://www.pygame.org/news) backend to implement a subset of the [Processing API](https://py.processing.org/).

## Requirements

- PyGame 2
- libsdl2-ttf

## Installation

```bash
$ git clone https://github.com/vrruiz/plus5/
$ cd plus5/
$ python3 setup.py install
```

## Usage

Working example.

```python
from plus5 import *

def setup():
    size(500,500)
    background(127,0,0)
    stroke(255)
    fill(127)
    rect(100,100,100,100)
    line(0,0,width,height)

def draw():
    pass

run()

```

## Author

Víctor R. Ruiz <rvr@linotipo.es>

## License

MIT
