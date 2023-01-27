from turtle import Turtle, Screen
import random

# list of rgb colours extracted from previous image
extract = [(202, 156, 95), (119, 162, 193), (225, 239, 232), (157, 82, 53), (149, 65, 96), (241, 223, 232),
           (218, 229, 238), (65, 99, 144), (164, 154, 54)]

# GUI set up
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=500)
turtle = Turtle()
current = -225

# Loop creating "painting" using random colours from extracted list
for b in range(10):
    turtle.penup()
    turtle.goto(-225, current)
    for a in range(10):
        turtle.dot(30, random.choice(extract))
        turtle.penup()
        turtle.forward(50)
    current += 50

screen.exitonclick()
