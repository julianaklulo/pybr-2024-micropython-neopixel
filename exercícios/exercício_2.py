"""
Exercício 2 Acender LED aleatório conforme balança a placa.

O LED aceso deve ser escolhido aleatoriamente conforme a placa é balançada.
A verificação de balanço é feita através do acelerômetro.

Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel.
"""
from microbit import *
import neopixel
import random

pixels = 12
np = neopixel.NeoPixel(pin0, pixels)

index = 0

while True:
    np[index] = (0, 0, 0)

    if accelerometer.is_gesture("shake"):
        index = random.randint(0, pixels - 1)
        
    np[index] = (255, 0, 0)
    np.show()

    sleep(100)
