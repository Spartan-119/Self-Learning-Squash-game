# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg

# declaring the variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

fgColor = pg.Color('Yellow')

# drawing the borders
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (BORDER, HEIGHT)))
pg.draw.rect(screen, fgColor, pg.Rect((0, HEIGHT - BORDER, WIDTH, BORDER)))

# to display the console screen
pg.display.flip()

# to close the console
while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break

pg.quit()