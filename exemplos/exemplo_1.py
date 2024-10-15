"""
Exemplo 1: Acender um LED.

Este exemplo acende o primeiro LED de um anel de LEDs NeoPixel.
Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
import neopixel

np = neopixel.NeoPixel(pin0, 12)
np[0] = (63, 63, 0)
np.show()
