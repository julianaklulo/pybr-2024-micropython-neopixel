"""
Exemplo 4: Apagar LEDs

Este exemplo apaga todos os LEDs de um anel de LEDs NeoPixel.
Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
import neopixel

np = neopixel.NeoPixel(pin0, 12)
for pixel_id in range(5):
    np[pixel_id] = (0, 63, 0)
    np.show()
    sleep(1000)

np.clear()
