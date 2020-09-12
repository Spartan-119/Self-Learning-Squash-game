# import statements
import pygame as pg

pg.init()

# declaring global variables
HEIGHT = 600
WIDTH = 1200
BORDER = 20
bgcolor = "Black"
ball_color = "Yellow"



class Ball:
    
    RADIUS = 15
    
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    # method to show the Ball
    def show(self, color):
        pg.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
    
    # method to update the position of the Ball
    # def update(self, )
    
pg.init()

# displaying the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
fgcolor = pg.Color("White")

# now we will draw the screen
pg.draw.rect(screen, fgcolor, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgcolor, pg.Rect(0, 0, BORDER, HEIGHT))
pg.draw.rect(screen, fgcolor, pg.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))

pg.display.flip()

while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break

pg.quit()