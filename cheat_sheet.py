"""
Cheat sheet com os comandos utilizados no tutorial.

Este arquivo contém os comandos utilizados no tutorial para facilitar a
consulta.

Para mais informações detalhadas, consulte a documentação oficial no editor
Python (https://python.microbit.org/) ou a documentação oficial do MicroPython
(https://microbit-micropython.readthedocs.io/en/latest/).
"""
# ***** Botões *****
from microbit import *

# Botão A foi pressionado?
if button_a.was_pressed():
    pass

# Botão B foi pressionado?
if button_b.was_pressed():
    pass

# Botão A está sendo pressionado?
if button_a.is_pressed():
    pass

# Botão B está sendo pressionado?
if button_b.is_pressed():
    pass

# Quantas vezes o botão A foi pressionado?
quantity = button_a.get_presses()

# Quantas vezes o botão B foi pressionado?
quantity = button_b.get_presses()


# ***** Acelerômetro *****
from microbit import *

# Ler aceleração em cada eixo
x = accelerometer.get_x()
y = accelerometer.get_y()
z = accelerometer.get_z()

# Gesto está acontecendo?
if accelerometer.is_gesture("face up"):
    pass

# Gesto aconteceu desde a última leitura?
if accelerometer.was_gesture("shake"):
    pass


# ***** Rádio *****
import radio

# Ligar o rádio
radio.on()

# Configurar o grupo e a força do sinal
# Group: 0-255, Power: 0-7
radio.config(group=23, power=7)

# Receber uma mensagem do grupo
message = radio.receive()

# Enviar uma mensagem para o grupo
radio.send("Python Brasil 2024")


# ***** Microfone *****
from microbit import *

# Ler a intensidade do som (0-255)
level = microphone.sound_level()

# Ler evento de som atual (LOUD ou QUIET)
event = microphone.current_event()

# Ler os eventos que já aconteceram
history = microphone.get_events()


# ***** Alto-falante *****
from microbit import *
import music, speech, audio

# Tocar música predefinida
music.play(music.POWER_UP)

# Criar sua própria música - formato: '{nota}{oitava}:{duração}'
music.play(
    [
        "C4:2", "D4:2", "E4:2", "F4:2",
        "G4:2", "A4:2", "B4:2",
    ]
)

# Texto para fala
speech.say("Hello, Python Brasil!")

# Tocar sons expressivos
audio.play(Sound.YAWN)


# ***** Display *****
from microbit import *

# Mostrar uma imagem predefinida
display.show(Image.HEART)

# Mostrar uma imagem personalizada
display.show(
    Image(
        "00000:"
        "33333:"
        "55555:"
        "77777:"
        "99999"
    )
)

# Mostrar um texto
display.scroll("Python Brasil 2024")

# Mostrar um pixel
display.set_pixel(0, 0, 9)

# Limpar o display
display.clear()
