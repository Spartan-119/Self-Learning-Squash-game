# import statements
import pygame as pg

pg.init()

# declaring global variables
HEIGHT = 600
WIDTH = 1200
BORDER = 20
bgcolor = pg.Color("black")
fgcolor = pg.Color("White")
ball_color = pg.Color("Yellow")
paddle_color = pg.Color("Green")
VELOCITY = 5
FRAMERATE = 120
clock = pg.time.Clock()


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
    
    ''' To move the ball around, we must UPDATE the position of the ball
        asper the command given by an input device 
        (in this case it is Mouse cursor)'''
    # method to update the position of the Ball
    def update(self, paddle_y, paddle_WIDTH, paddle_HEIGHT):
        newx = self.x + self.vx
        newy = self.y + self.vy
        
        ''' logic to bounce back the ball off the walls '''
        
        ''' for along the X axis '''
        if newx < BORDER + self.RADIUS:
            self.vx = - self.vx
        
        ''' for along the Y axis '''
        if newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = - self.vy
        
        ''' logic to bounce off the ball when it hits the paddle '''
        if newx == WIDTH - paddle_WIDTH and (newy + self.RADIUS >= paddle_y - paddle_HEIGHT//2 and 
                                             newy - self.RADIUS <= paddle_y + paddle_HEIGHT//2):
            self.vx = -self.vx
             
        # to show the moving ball
        self.show(bgcolor)
        self.x += self.vx
        self.y += self.vy
        self.show(ball_color)

# ------- PADDLE --------
class Paddle:
    
    WIDTH = 20
    HEIGHT = 100
    
    def __init__(self, y):
        self.y = y # because we will only move the paddle along Y axis
    
    # method to show the paddle
    def show(self, color, x):
        pg.draw.rect(screen, color, pg.Rect(x, self.y - self.HEIGHT//2,self.WIDTH,self.HEIGHT))
    
    ''' To move the paddle, we must UPDATE the position of the paddle 
        it asper the command given by an input device 
        (in this case it is Mouse cursor)'''
    # method to Move the paddle
    def update(self,mouse,x):
        if not(mouse - self.HEIGHT//2 <= BORDER or mouse + self.HEIGHT//2 >= HEIGHT - BORDER):
            self.show(bgcolor,x)
            self.y = mouse
            self.show(paddle_color,x)
        elif mouse + self.HEIGHT//2 <= BORDER:
            self.y = self.HEIGHT//2 + BORDER
        else:
            self.y = HEIGHT -self.HEIGHT//2 - BORDER

# ------ MAKING OBJECTS -------
ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)
ball.show(ball_color)

paddle = Paddle(HEIGHT//2)
paddle.show(paddle_color, WIDTH - Paddle.WIDTH)


# now we will draw the screen
pg.draw.rect(screen, fgcolor, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fgcolor, pg.Rect(0, 0, BORDER, HEIGHT))
pg.draw.rect(screen, fgcolor, pg.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))

while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break
    
    ball.update(paddle.y, paddle.WIDTH, paddle.HEIGHT)
    paddle.update(pg.mouse.get_pos()[1], WIDTH-BORDER)
    
    ''' This method should be called once per frame. It will compute how many 
        milliseconds have passed since the previous call.
        If you pass the optional framerate argument the function 
        will delay to keep the game running slower 
        than the given ticks per second. 
        This can be used to help limit the runtime speed of a game. 
        By calling Clock.tick(40) once per frame, the program will 
        never run at more than 40 frames per second. '''
        
    '''
    FPS, Frames Per Second, is the number of frames shown per unit of time.
    1 / FPS is the amount of time should pass between each frame.
    Tick is just a measure of time in PyGame.

    clock.tick(60) means that for every second at most 60 frames should pass.
    '''    
    clock.tick(FRAMERATE)
    
    # to update the contents of the ENTIRE screen
    pg.display.flip()

pg.quit()