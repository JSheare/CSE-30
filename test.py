import turtle


def draw_dragon(t, length, level, right=1):
    t.pendown()
    if level > 0:
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        for i in range(right):
            t.forward(length)
            t.right(90)

        draw_dragon(t, length, level-1, right+1)


if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(450, 450)
    t = turtle.Turtle()
    t.pen(pencolor='black', pensize=2, speed=0)
    for i in range(4):
        t.forward(100)
        t.left(90)


