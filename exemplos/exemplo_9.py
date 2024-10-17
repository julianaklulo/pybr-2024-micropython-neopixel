"""
Exemplo 9: Tocando uma melodia

Esse exemplo toca uma melodia no alto-falante da micro:bit.
"""
import music

music.play(
    [
        "G4:2", "A4:2", "B4:4", "D5:4", "D5:4", "B4:4", "C5:4", "C5:4",
        "r:2", "G4:2", "A4:2", "B4:4", "D5:4", "D5:4", "C5:4", "B4:8",
    ]
)
