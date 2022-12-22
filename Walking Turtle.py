from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle(shape = "turtle")
colors = ["blue", "red", "green", "purple", "violet", "yellow", "gold", "brown", "black", "orange"]
directions = [0, 90, 180, 270, 360]
while True:
    tim.forward(10)
    A = random.choice(directions)
    B = random.choice(colors)
    tim.right(A)
    tim.color(B)
    
screen.exitonclick()
