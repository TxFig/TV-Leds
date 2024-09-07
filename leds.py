import neopixel
import board


ledsPin = board.D18
numOfLeds = 300
pixels = neopixel.NeoPixel(ledsPin, numOfLeds, auto_write=False)

def clear():
    pixels.fill((0, 0, 0))

def update(colors):
    for index in range(numOfLeds):
        pixels[index] = colors[index]
    pixels.show()
