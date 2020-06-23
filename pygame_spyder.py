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
VELOCITY = -1

# defining the classes

# Ball class
class Ball:
    RADIUS = 20
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
    def show(self, color):
        global screen
        pg.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
        
    # function to move the ball
    def update(self, color):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(fgColor)

# Paddle class
class Paddle:
    pass

# creating objects
ballPlay = Ball(WIDTH - Ball.RADIUS, HEIGHT//2, VELOCITY, 0)

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

fgColor = pg.Color('Yellow')

# drawing the borders
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (BORDER, HEIGHT)))
pg.draw.rect(screen, fgColor, pg.Rect((0, HEIGHT - BORDER, WIDTH, BORDER)))

# to display the console screen
ballPlay.show(fgColor) # to show the ball

# to close the console
while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break
    
    pg.display.flip()
    ballPlay.update(fgColor)

pg.quit()
