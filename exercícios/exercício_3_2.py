"""
Exercício 3.2: Mover LED através do rádio - Receiver.

Sender: lê os dados do acelerômetro e envia pelo rádio.
Receiver: recebe os dados do rádio e move o LED aceso.

Lembre-se de ajustar a quantidade de LEDs ao criar o objeto NeoPixel,
e de ajustar o canal de rádio (deve ser único por dupla).
"""
from microbit import *
import neopixel
import radio

channel = 0
radio.config(channel=channel)
radio.on()

pixels = 12
np = neopixel.NeoPixel(pin0, pixels)

index = 0

while True:
    message = radio.receive()
    if message:
        np[index] = (0, 0, 0)
        index = int(message)
        np[index] = (255, 0, 0)
        np.show()
    sleep(100)
