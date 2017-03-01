import turtle

def draw_square(some_turtle, step):
    for i in range(1,5):
        some_turtle.forward(step)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("grey")

    turtle_sq = turtle.Turtle()
    turtle_sq.shape("turtle")
    turtle_sq.color("orange")
    turtle_sq.speed(50)

    for i in range(1, 361):
        draw_square(turtle_sq, 115)
        turtle_sq.right(1)

    window.exitonclick()



draw_art()
