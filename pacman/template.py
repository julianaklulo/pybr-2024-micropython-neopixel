"""
Projeto: Jogo do Pacman

Implementação do jogo do Pacman com micro:bit e Neopixels.

O jogo consiste em um LED amarelo que representa o Pacman se movendo
para a esquerda ou para a direita conforme os botões A e B são pressionados.

O objetivo é capturar um LED que representa um fantasma.
Caso o Pacman coma a fruta vermelha, ele fica forte e pode capturar
o fastasma, que fica azul.

Se houver uma colisão com o fanstasma enquanto ele está verde, o jogo acaba.
"""
from microbit import *
import neopixel
import random
import time
import music


class Game:
    def __init__(self, pin, pixels):
        self.pixels = pixels
        self.np = neopixel.NeoPixel(pin, self.pixels)

        self.pacman = Pacman(self.pixels)
        self.ghost = Ghost(self.pixels)
        self.fruit = Fruit(self.pixels)

        self.strong_time = 5000

    def check_fruit_collision(self):
        pass

    def check_strong(self):
        pass

    def check_ghost_collision(self):
        pass

    def got_ghost(self):
        pass

    def end(self):
        pass

    def run(self):
        pass


class Pacman:
    def __init__(self, pixels):
        self.pixels = pixels
        self.position = random.randint(0, self.pixels - 1)
        self.color = (238, 173, 45)

        self.speed = 1000
        self.direction = 1
        self.last_moved = time.ticks_ms()

        self.strong = False

    def next_position(self):
        pass

    def move(self):
        pass

    def show(self, np):
        pass


class Ghost:
    def __init__(self, pixels):
        self.pixels = pixels
        self.position = random.randint(0, self.pixels - 1)

        self.regular_color = (0, 255, 0)
        self.strong_color = (0, 0, 255)
        self.current_color = self.regular_color

        self.speed = 1500
        self.direction = 1
        self.last_moved = time.ticks_ms()

    def next_position(self):
        pass

    def move(self):
        pass

    def randomize_position(self):
        pass

    def set_color(self, strong):
        pass

    def show(self, np):
        pass


class Fruit:
    def __init__(self, pixels):
        self.pixels = pixels
        self.position = random.randint(0, self.pixels - 1)
        self.color = (255, 0, 0)

        self.got_fruit = time.ticks_ms()

    def hide(self):
        pass

    def randomize_position(self):
        pass

    def show(self, np):
        pass


game = Game(pin=pin0, pixels=12)
game.run()
