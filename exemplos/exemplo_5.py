"""
Exemplo 5: Lendo o estado dos botões

Este exemplo lê o estado dos botões A e B do micro:bit e imprime mensagens
de acordo com o botão que foi ou está sendo pressionado.
"""
from microbit import *

while True:
    if button_a.is_pressed():
        print("Botão A está sendo pressionado")
    if button_b.is_pressed():
        print("Botão B está sendo pressionado")

    if button_a.was_pressed():
        print("Botão A foi pressionado")
    if button_b.was_pressed():
        print("Botão B foi pressionado")

    sleep(100)
