"""
Exercício 1: Mover o LED aceso com os botões.

O LED aceso deve se mover para a esquerda ou para a direita
conforme os botões A e B são pressionados.

Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
from microbit import *
import neopixel

pixels = 12
np = neopixel.NeoPixel(pin0, pixels)

index = 0

while True:
    np[index] = (0, 0, 0)

    if button_a.was_pressed():
        index = (index - 1) % pixels
    elif button_b.was_pressed():
        index = (index + 1) % pixels

    np[index] = (255, 0, 0)
    np.show()

    sleep(100)
