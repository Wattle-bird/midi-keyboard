# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoKey 5x6 Ortho Snap-Apart simple key press NeoPixel demo.
"""
import board
import keypad
import neopixel

COLUMNS = 6
ROWS = 5

pixels = neopixel.NeoPixel(board.GP0, 30, brightness=0.05)

keys = keypad.KeyMatrix(
    row_pins=(board.GP1,board.GP2,board.GP3,board.GP4,board.GP5),
    column_pins=(board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11),
    columns_to_anodes=False,
)


def key_to_pixel_map(key_number):
    row = key_number // COLUMNS
    column = (key_number % COLUMNS)
    if row % 2 == 1:
        column = COLUMNS - column - 1
    return row * COLUMNS + column


pixels.fill((0, 0, 0))  # Begin with pixels off.
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            pixels[key_to_pixel_map(key_event.key_number)] = (255, 255, 255)
        else:
            pixels[key_to_pixel_map(key_event.key_number)] = (0, 0, 0)
