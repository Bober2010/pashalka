
import time
import turtle as t


t.screensize(500,500)
player = t.Turtle('circle')
player.shapesize(8)
x = -380
ball = t.Turtle('circle')
ball.up()
ball.goto(x,-320)
ball.shapesize(3)
ball.color('blue')
color = 'red'
while True:
    start = time.time()
    player.color(color)
    while start + 5 > time.time():
        if color == 'green':
            ball.speed(1)
            ball.forward(1)
        
    
        
        
    if color == 'red':
        color = 'green'
    elif color == 'green':
        color = 'red'
    
    

