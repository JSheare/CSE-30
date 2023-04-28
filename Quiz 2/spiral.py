import turtle


# draw a spiral
def draw_spiral(t, segments, size, angle):
    t.pendown()
    for i in range(1, segments+1):
        t.fd(size*i)
        t.left(angle)


def draw_spiral2(t, segments, size, angle):
    t.pendown()
    if segments > 0:
        t.fd(size)
        t.left(angle)
        draw_spiral(t, segments-1, size+4, angle)


# driver code
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(500, 500)
    t = turtle.Turtle()
    t.pen(pencolor='dark violet', pensize=2, speed=0)
    t.penup()
    t.home()
    draw_spiral(t, 90, 4, 95)

    t.penup()
    t.home()
    t.color('green')
    draw_spiral2(t, 90, 4, 95)
    s.exitonclick()
