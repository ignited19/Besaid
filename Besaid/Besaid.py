# Function: A simple graphics program 


import turtle
import random
from itertools import cycle

#cycles through colors 
colors=cycle(['red','green','blue','yellow','purple', 'orange'])

def Create_Circle(size, angle, shift):
    
    RandomSize=random.randrange(10,20)
    RandomAngle=random.randrange(10,20)
    RandomShift=random.randrange(1,10)

    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)

    Create_Circle(RandomSize+size, RandomAngle+angle, shift+RandomShift)



#Sets the background color, speed, and pen
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(2)
Create_Circle(30,0,1)

