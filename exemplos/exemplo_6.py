"""
Exemplo 6: Lendo os gestos do acelerômetro

Mostre uma seta na direção do gesto atual do acelerômetro.
"""
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "up":
        display.show(Image.ARROW_N)
    elif gesture == "down":
        display.show(Image.ARROW_S)
    elif gesture == "left":
        display.show(Image.ARROW_W)
    elif gesture == "right":
        display.show(Image.ARROW_E)

    sleep(100)
    display.clear()
