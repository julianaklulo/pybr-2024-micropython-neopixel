"""
Exercício 4: Trocando a cor de acordo com o som.

O anel de LED deve trocar de cor aleatoriamente conforme o som é detectado.
Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
from microbit import *
import neopixel
import random

pixels = 12
np = neopixel.NeoPixel(pin0, pixels)

sound_limit = 50

while True:
    if microphone.sound_level() > sound_limit:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        np.fill((r, g, b))
    np.show()
    sleep(100)
