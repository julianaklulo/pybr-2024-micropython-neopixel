"""
Exemplo 8: Lendo os valores do microfone

Este exemplo lê os valores do microfone e imprime o valor lido.
"""
from microbit import *

while True:
    level = microphone.sound_level()
    print(level)

    sleep(100)
