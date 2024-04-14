import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0.2)  # speed

# List of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a colorful spiral
for i in range(360):
    t.pencolor(random.choice(colors))  # Random color from the list
    t.forward(i * 2)  # Move the turtle forward
    t.left(121)  # Turn the turtle left

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
