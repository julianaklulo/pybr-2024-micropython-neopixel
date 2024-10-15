"""
Exemplo 3: Acender vários LEDs.

Este exemplo acende um LED de cada vez em um anel de LEDs NeoPixel.
Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
import neopixel

np = neopixel.NeoPixel(pin0, 12)
for pixel_id in range(len(np)):
    np[pixel_id] = (127, 0, 127)
    np.show()
    sleep(1000)
