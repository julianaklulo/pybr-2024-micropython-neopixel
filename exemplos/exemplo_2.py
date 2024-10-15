"""
Exemplo 2: Acender todos os LEDs.

Este exemplo acende todos os LEDs de um anel de LEDs NeoPixel.
Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
import neopixel

np = neopixel.NeoPixel(pin0, 12)
np.fill((0, 0, 63))
np.show()
