from tkinter import *
import tkinter.font as font
from random import random, randint
from math import sin, cos, pi
from pygame import mixer


class Avatar:

    def __init__(self, canvas):

        color1 = 'lime'
        color2 = 'sandybrown'
        self.canvas = canvas
        self.head = self.canvas.create_oval(0, 0, 10, 10, fill=color2)
        self.torso = self.canvas.create_rectangle(0, 10, 10, 20,
                                                  fill=color1)
        self.canvas.move(self.head, START_X, START_Y - 20)
        self.canvas.move(self.torso, START_X, START_Y - 20)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.canvas.bind_all('<KeyPress-Down>', self.move)

    def update(self, land, trophy):  # call find_trophy and hit_object, check if jumping up or falling, etc.
        self.canvas.move(self.head, self.x, self.y)
        self.canvas.move(self.torso, self.x, self.y)

    def move(self, event=None):
        if event.keysym == 'Left':
            self.x = -1
        elif event.keysym == 'Right':
            self.x = 1
        elif event.keysym == 'Up':  # jumping
            self.y = -2
        elif event.keysym == 'Down':
            self.y = 1

    def hit_object(self, obj):  # recommended
        pass

    def find_trophy(self, trophy):  # recommended
        pass


class AI:

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.spider = self.make_spider(x, y)
        self.thread = self.canvas.create_line(x + 10, 0, x + 10, y + 5,
                                              fill='ivory2', width=3)
        self.x, self.y = 0, 0.5

    def make_spider(self, x, y):
        color1 = 'black'
        head = self.canvas.create_oval(5, 5, 15, 13, fill=color1)
        torso = self.canvas.create_oval(0, 10, 20, 40, fill=color1)
        legs = [self.canvas.create_line(-5 - i * 5, 10 * i + 5, 5, 10 * i + 15,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(15, 10 * i + 15, 25 + i * 5, 10 * i + 5,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(-10 + i * 5, 10 * i + 35, 5, 10 * i + 25,
                                        fill=color1, width=4) for i in range(2)] + \
               [self.canvas.create_line(15, 10 * i + 25, 30 - i * 5, 10 * i + 35,
                                        fill=color1, width=4) for i in range(2)]

        spider = [head, torso] + legs
        for part in spider:
            self.canvas.move(part, x, y)
        return spider

    def update(self, eatable):
        pass


class Trophy:

    def __init__(self, canvas):
        self.canvas = canvas
        purple_egg = self.canvas.create_oval(0, 0, 20, 10, fill='orchid')
        pink_egg = self.canvas.create_oval(0, 0, 20, 10, fill='pink')

        self.trophies = [purple_egg, pink_egg]

    def get_trophy(self):
        return self.trophies

    def replace(self):
        pass


class Land:

    def __init__(self, canvas):
        self.canvas = canvas

        # sky
        self.canvas.create_rectangle(0, 0, WIDTH, START_Y - 100,
                                     fill='lightblue')
        # valley
        self.canvas.create_rectangle(0, START_Y - 120, WIDTH, START_Y,
                                     fill='limegreen')

        self.make_hill(50, 230, 250, 230, height=100, delta=3)
        self.make_hill(150, 300, 350, 300, height=100, delta=3)
        self.make_hill(250, 250, 450, 250, height=100, delta=3)
        self.make_hill(350, 300, 550, 300, height=100, delta=3)

        cloud1 = self.make_cloud(100, 120)
        cloud2 = self.make_cloud(200, 140)
        cloud3 = self.make_cloud(300, 80)
        self.clouds = [cloud1, cloud2, cloud3]

    def get_obstacles(self):
        return [self.ground, self.start, self.stop] + self.platforms

    def update(self):
        pass


class Skyland:

    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        self.canvas.bind_all('<KeyPress-Alt_L>', self.restart)

        self.avatar = Avatar(canvas)
        ...
        self.text = canvas.create_text(x, y, text='Score ?  Time ? ',
                                       font=font.Font(family='Helveca', size=15, weight='bold'))
        self.play_music()
        self.update()

    def restart(self, event=None):
        self.avatar.replace()
        self.trophy.replace()
        ...
        self.sound.stop()
        self.sound.play()
        self.update()

    def pause(self, event=None):
        pass


    def update(self):
        pass
        self.canvas.after(CLOCK_RATE, self.update)


    def play_music(self):
        if not mixer.get_init():
            mixer.init()
        self.sound = mixer.Sound('./sound1.mp3')
        self.sound.play()


WIDTH, HEIGHT = 600, 400
CLOCK_RATE = 15

if __name__ == '__main__':
    tk = Tk()
    tk.title('Skyland')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    game = Skyland(canvas)
    mainloop()