import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
#TO draw shapes
# n=int(input("Enter number of sides"))
# for _ in range(n):
#     timmy.forward(100)
#     timmy.left(360/n)
# use penup penddown fro dashed line
# color=["red", "blue", "green", "turquoise", "lavender"]
dir=[0, 90, 180, 270]
turtle.colormode(255)
tim.speed("fastest")
def colorchoice ():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color=(r, g, b)
    return color
origin=0
for _ in range(200):
    tim.circle(100)
    tim.position(origin)
    origin+=1
    #for random walk
    tim.color(colorchoice())
    # tim.forward(30)
    # tim.setheading(random.choice(dir))
screen.exitonclick()

