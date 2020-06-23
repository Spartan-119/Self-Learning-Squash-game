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
VELOCITY_X = 1
VELOCITY_Y = 1

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
    def update(self):
        global bgColor, fgColor
        
        new_x = self.x + self.vx
        new_y = self.y + self.vy
        
        # conditions to manage the collision of the ball with the border
        if new_x < BORDER + self.RADIUS:
            self.vx = -self.vx
        
        elif new_y < BORDER + self.RADIUS or new_y > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy
        
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)

# Paddle class
class Paddle:
    WIDTH = 20
    HEIGHT = 100
    
    def __init__(self, y):
        self.y = y
    
    def show(self, color):
        global screen
        pg.draw.rect(screen, color, pg.Rect(WIDTH - self.WIDTH, self.y - self.HEIGHT//2))
    
    def update(self):
        self.show(pg.Color('Black'))
        self.y = pg.mouse.get_pos()[1]
        self.show(pg.Color('Yellow'))

# creating objects
ballPlay = Ball(WIDTH - Ball.RADIUS, HEIGHT//2, -VELOCITY_X, -VELOCITY_Y)
paddle = Paddle(HEIGHT//2)

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

bgColor = pg.Color('Black')
fgColor = pg.Color('Yellow')

# drawing the borders
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgColor, pg.Rect((0, 0), (BORDER, HEIGHT)))
pg.draw.rect(screen, fgColor, pg.Rect((0, HEIGHT - BORDER, WIDTH, BORDER)))

# to display the console screen
ballPlay.show(fgColor) # to show the ball
paddle.show(fgColor)

# to close the console
while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break
    
    pg.display.flip()
    ballPlay.update()
    paddle.update()

pg.quit()
