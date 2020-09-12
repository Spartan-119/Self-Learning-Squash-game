# import statements
import pygame as pg

pg.init()

# declaring global variables
HEIGHT = 600
WIDTH = 1200
BORDER = 20
bgcolor = "Black"
fgcolor = pg.Color("White")
ball_color = pg.Color("Yellow")
paddle_color = pg.Color("Green")
VELOCITY = 5
FRAMERATE = 60

pg.init()

# displaying the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))

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
    def update(self, ):
        pass

# ------- PADDLE --------
class Paddle:
    
    WIDTH = 20
    HEIGHT = 100
    
    def __init__(self, y):
        self.y = y # because we will only move the paddle along Y axis
    
    # method to show the paddle
    def show(self, color, x):
        pg.draw.rect(screen, color, pg.Rect(x, self.y - self.HEIGHT//2,self.WIDTH,self.HEIGHT))
    
    # method to update the paddle
    def update(self, ):
        pass

# ------ MAKING OBJECTS -------
ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)
ball.show(ball_color)

paddle = Paddle(HEIGHT//2)
paddle.show(paddle_color, WIDTH - Paddle.WIDTH)


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