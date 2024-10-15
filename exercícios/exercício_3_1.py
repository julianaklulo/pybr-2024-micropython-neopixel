"""
Exercício 3.1: Mover LED através do rádio - Sender.

Sender: lê os dados do acelerômetro e envia pelo rádio.
Receiver: recebe os dados do rádio e move o LED aceso.

Lembre-se de ajustar a quantidade de LEDs para gerar o index,
e de ajustar o canal de rádio (deve ser único por dupla).
"""
from microbit import *
import radio

channel = 0
radio.config(channel=channel)
radio.on()

pixels = 12
limit = 250
index = 0

while True:
    if accelerometer.get_x() > limit:
        index = (index  - 1) % pixels
    elif accelerometer.get_x() < -limit:
        index = (index + 1) % pixels

    radio.send(str(index))
    sleep(100)
