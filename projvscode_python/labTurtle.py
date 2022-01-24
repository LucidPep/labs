import turtle

def drawAnything(angle, step, spd):
    anything = turtle.Turtle()
    anything.speed(spd)
    for i in range(50):
        anything.left(angle)
        for j in range(10):
            anything.forward(step)
            anything.left(angle//2)
            anything.right(angle % 13)
            anything.forward(step*2 + i//3)
    
    turtle.exitonclick()

def drawAnything2(angle, step, spd):
    anything_2 = turtle.Turtle()
    anything_2.speed(spd)
    anything_2.color("red")
    anything_2.pensize(3)
    for i in range(61):
        anything_2.left(angle)
        for j in range(10):
            anything_2.forward(step+j)
            anything_2.left(angle//5)
            anything_2.right(angle % 13)
            anything_2.forward(step*2 + i//3)
    
    turtle.exitonclick()

#drawAnything(90, 2, 11999999)
drawAnything2(90, 5, 11999999)