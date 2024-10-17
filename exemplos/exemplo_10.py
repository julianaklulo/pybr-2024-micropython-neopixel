"""
Exemplo 10: Usando o contador de tempo

Este exemplo exibe um coração após 3 segundos.
"""
from microbit import *
import time

start_time = time.ticks_ms()

while True:
    now = time.ticks_ms()
    if time.ticks_diff(now, start_time) > 3000:
        display.show(Image.HEART)
        break
