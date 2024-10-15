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
        if self.pacman.position == self.fruit.position and not self.pacman.strong:
            music.play(music.JUMP_UP, wait=False)
            display.show(Image.HAPPY)
            self.pacman.strong = True
            self.fruit.hide()
            self.ghost.set_color(self.pacman.strong)

    def check_strong(self):
        if (
            time.ticks_diff(time.ticks_ms(), self.fruit.got_fruit) > self.strong_time
            and self.pacman.strong
        ):
            music.play(music.JUMP_DOWN, wait=False)
            display.clear()
            self.pacman.strong = False
            self.fruit.randomize_position()
            self.ghost.set_color(self.pacman.strong)

    def check_ghost_collision(self):
        if self.pacman.position == self.ghost.position:
            if self.pacman.strong:
                self.got_ghost()
                self.ghost.randomize_position()
                return False
            else:
                self.end()
                return True

    def got_ghost(self):
        display.show(Image.YES)
        music.play(music.BA_DING, wait=False)

    def end(self):
        display.show(Image.SAD)
        music.play(music.WAWAWAWAA)

    def run(self):
        while True:
            self.np.clear()
            self.pacman.move()
            self.ghost.move()

            self.check_fruit_collision()
            if self.check_ghost_collision():
                break
            self.check_strong()

            self.fruit.show(self.np)
            self.ghost.show(self.np)
            self.pacman.show(self.np)
            self.np.show()

            sleep(100)


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
        return (self.position + self.direction) % self.pixels

    def move(self):
        if button_a.was_pressed():
            self.direction = -1
        elif button_b.was_pressed():
            self.direction = 1

        if time.ticks_diff(time.ticks_ms(), self.last_moved) > self.speed:
            self.position = self.next_position()
            self.last_moved = time.ticks_ms()

    def show(self, np):
        np[self.position] = self.color


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
        return (self.position + self.direction) % self.pixels

    def move(self):
        if time.ticks_diff(time.ticks_ms(), self.last_moved) > self.speed:
            self.position = self.next_position()
            self.last_moved = time.ticks_ms()

    def randomize_position(self):
        self.position = random.randint(0, self.pixels - 1)

    def set_color(self, strong):
        if strong:
            self.current_color = self.strong_color
        else:
            self.current_color = self.regular_color

    def show(self, np):
        np[self.position] = self.current_color


class Fruit:
    def __init__(self, pixels):
        self.pixels = pixels
        self.position = random.randint(0, self.pixels - 1)
        self.color = (255, 0, 0)

        self.got_fruit = time.ticks_ms()

    def hide(self):
        self.color = (0, 0, 0)
        self.got_fruit = time.ticks_ms()

    def randomize_position(self):
        self.position = random.randint(0, self.pixels - 1)
        self.color = (255, 0, 0)

    def show(self, np):
        np[self.position] = self.color


game = Game(pin=pin0, pixels=12)
game.run()
