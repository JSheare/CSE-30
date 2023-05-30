from tkinter import *


class Racket:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 100
        self.height = 10
        self.speed = 6
        self.score = 0
        self.id = self.canvas.create_rectangle(0, 0, self.width, self.height, fill='blue')
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def move_left(self, *args):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x1 > 0:
            self.canvas.move(self.id, -1*self.speed, 0)

    def move_right(self, *args):
        width = int(self.canvas.cget('width'))
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x2 < width:
            self.canvas.move(self.id, self.speed, 0)

    def reset(self):
        self.canvas.moveto(self.id, 0, 0)


class AiRacket:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ball = None
        self.width = 100
        self.height = 10
        self.speed = 6
        self.score = 0
        self.id = self.canvas.create_rectangle(0, 0, self.width, self.height, fill='black')
        self.canvas.move(self.id, 0, 7 * int(self.canvas.cget('height')) / 8 - self.height)

    def assign_ball(self, ball):
        self.ball = ball

    def move(self, *args):
        x1b, y1b, x2b, y2b = self.canvas.coords(self.ball.id)
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x1b < x1:
            self.move_left()
        elif x2b > x2:
            self.move_right()

        self.canvas.after(10, self.move)

    def move_left(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x1 > 0:
            self.canvas.move(self.id, -1*self.speed, 0)

    def move_right(self):
        width = int(self.canvas.cget('width'))
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x2 < width:
            self.canvas.move(self.id, self.speed, 0)

    def reset(self):
        self.canvas.moveto(self.id, 0, 7 * int(self.canvas.cget('height')) / 8 - self.height)


class Ball:
    def __init__(self, canvas, top_racket, bottom_racket):
        self.canvas = canvas
        self.top_racket = top_racket
        self.bottom_racket = bottom_racket
        self.size = 115
        self.speed = 3
        self.dx = self.speed
        self.dy = self.speed
        self.lock = False
        self.id = self.canvas.create_oval(100, 100, self.size, self.size, fill="red")
        self.text_id = self.canvas.create_text(189, 260, text=f'Score {self.top_racket.score}:'
                                                              f'{self.bottom_racket.score}', font=('Times', 15))

    def move(self):
        canvas_width = int(self.canvas.cget('width'))
        canvas_height = int(self.canvas.cget('height'))
        x1tr, y1tr, x2tr, y2tr = self.canvas.coords(self.top_racket.id)
        x1br, y1br, x2br, y2br = self.canvas.coords(self.bottom_racket.id)
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        # Ball bounces off the left or right wall
        if x2 > canvas_width or x1 < 0:
            self.dx = -self.dx

        # Ball bounces off one of the rackets
        # Self.lock prevents the ball from 'surfing' on the top racket
        if y2tr >= y1 and (x1tr <= x1 <= x2tr or x1tr <= x2 <= x2tr) and not self.lock:
            self.dy = -self.dy
            self.lock = True
        elif y1br <= y2 and (x1br <= x1 < x2br or x1br <= x2 < x2br):
            self.dy = -self.dy
            self.lock = False

        # Ball goes past one of the rackets
        if y2 > canvas_height or y1 < 0:
            if y2 > canvas_height:
                self.top_racket.score += 1
            else:
                self.bottom_racket.score += 1

            self.reset()

        self.canvas.move(self.id, self.dx, self.dy)
        self.canvas.after(10, self.move)

    def reset(self):
        self.canvas.delete(self.text_id)
        self.text_id = self.canvas.create_text(189, 260, text=f'Score {self.top_racket.score}:'
                                                              f'{self.bottom_racket.score}', font=('Times', 15))
        self.top_racket.reset()
        self.bottom_racket.reset()
        self.canvas.moveto(self.id, 100, 100)
        self.dx = self.speed
        self.dy = self.speed


# main program
gui = Tk()
gui.title('Pong')
canvas = Canvas(gui)
racket1 = Racket(canvas)
racket2 = AiRacket(canvas)
ball = Ball(canvas, racket1, racket2)
racket2.assign_ball(ball)
canvas.pack()
ball.move()
racket2.move()
mainloop()
