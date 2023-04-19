# draws a tree
import turtle as turtle
import time


# set the canvas window
def set_canvas():
    s = turtle.Screen()
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s


# set a turtle (a pen)
def set_pen(color):
    t = turtle.Turtle()
    t.shape('turtle')
    t.pen(pencolor=color, fillcolor=color, pensize=1, speed=10)
    return t


# draw a tree fractal using recursion
def draw_tree(t, branch, angle, n):
    if n > 0:  # recursive step
        t.pensize(3)
        t.forward(branch)
        t.left(angle)
        draw_tree(t, branch, angle, n-1)
        t.right(2*angle)
        t.pensize(1)
        draw_tree(t, branch, angle, n-1)
        t.left(angle)
        t.backward(branch)

    else:  # base case
        t.right(90)
        t.forward(1)
        t.left(90)

        t.pencolor('green')
        t.fillcolor('green')
        t.dot(15)

        t.pencolor('brown')
        t.fillcolor('brown')
        t.right(90)
        t.forward(1)
        t.left(90)


# main program
if __name__ == '__main__':
    s = set_canvas()
    t = set_pen('brown')
    t.penup()
    t.goto(-45, -150)
    t.left(90)
    t.pendown()
    draw_tree(t, 60, 20, 6)
    time.sleep(10)
