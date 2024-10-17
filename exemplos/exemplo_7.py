"""
Exemplo 7: Teleportando o pato

- Escolha um parceiro e defina um grupo de rádio
- Envie “duck” quando o dispositivo for sacudido
- Exiba um pato quando “duck” for recebido
"""
from microbit import *
import radio

GROUP = 0  # Defina o grupo de rádio com a sua dupla

radio.on()
radio.config(group=GROUP)

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        radio.send("duck")
    if radio.receive() == "duck":
        display.show(Image.DUCK)
    sleep(100)
