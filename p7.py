import turtle

# Set up the screen

screen = turtle.Screen()

screen.title("Turtle Drawing")

screen.bgcolor("lightblue")

 

# Set the background image

screen.bgpic("D:\AI\ESRGAN\LR\1 (2).png")  # Replace with the actual path to your image

 

# Create a Turtle instance

t = turtle.Turtle()

 

# Draw a circle

t.penup()

t.goto(0, -100)  # Move the turtle to the center of the circle

t.pendown()

t.color("red")

t.begin_fill()

t.circle(100)

t.end_fill()

 

# Hide the turtle

t.hideturtle()

 

# Keep the window open until it's closed by the user

turtle.done()