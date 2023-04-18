import turtle as turtle


# Generates star using iteration
def star(size, n, d=2):
    pass


# Generates star using recursion
def star_recursive(size, n, level, d=2):
    pass


# main program
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(800, 400)
    s.bgcolor("white")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("turtle")
    t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=3, speed=1)

    t.penup()
    t.goto(-150, 0)
    star(100, 5, 2)  # should draw a purple pentagram (5-pointed star)

    t.penup()
    t.goto(150, 0)
    t.color('red')
    t.pendown()
    star_recursive(100, 8, 8, 3)  # should draw a red octagram (8-pointed star)
