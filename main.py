import turtle

dog = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    dog.forward(10)


def move_backward():
    dog.backward(10)


def turn_clockwise():
    dog.setheading(dog.heading() - 10)


def turn_counterclockwise():
    dog.setheading(dog.heading() + 10)


def reset():
    dog.clear()
    dog.hideturtle()
    dog.penup()
    dog.home()
    dog.pendown()
    dog.showturtle()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counterclockwise, "a")
screen.onkey(reset, "c")
screen.exitonclick()
