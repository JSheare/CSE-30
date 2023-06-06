# cse30
# pa5
# skyland.py - a one-level platform video game
# author:
# date:

from tkinter import *
import tkinter.font as font
from random import random, randint # optional
from math import sin, cos, pi # optional


WIDTH, HEIGHT = 600, 400  # global variables (constants) go here
CLOCK_RATE = 15
START_X, START_Y = 20, 350
END_X, END_Y = 400, 350


class Skyland:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        self.canvas.bind_all('<KeyPress-Alt_L>', self.restart)
        self.paused = False
        self.pause_text = None

        self.score = 0
        self.time = 0
        self.land = Land(canvas)
        self.trophy = Trophy(canvas)
        self.avatar = Avatar(canvas)
        self.text = canvas.create_text(150, 370, text=f'Score {self.score}  Time {self.time} ',
                                       font=font.Font(family='Helveca', size=15, weight='bold'))

        self.update()

    def restart(self, event=None):
        self.avatar.replace()
        self.trophy.replace()
        self.update()
        
    def pause(self, event=None):
        if not self.paused:
            self.paused = True
        else:
            self.paused = False
            self.update()

    def update(self):
        if not self.paused:
            self.avatar.update(self.land, self.trophy)
            self.land.update()
            self.canvas.after(CLOCK_RATE, self.update)

            self.time += CLOCK_RATE * 1e-3
            self.canvas.delete(self.text)
            self.text = canvas.create_text(150, 370, text=f'Score {self.score}  Time {"% .2f" % self.time} ',
                                           font=font.Font(family='Helveca', size=15, weight='bold'))


class Land:
    def __init__(self, canvas):
        self.canvas = canvas

        # sky
        self.canvas.create_rectangle(0, 0, WIDTH, START_Y-100, fill='lightblue')
        # valley
        self.canvas.create_rectangle(0, START_Y-120, WIDTH, START_Y, fill='limegreen')
        
        self.make_hill(50, 230, 250, 230, height=100, delta=3)
        self.make_hill(150, 300, 350, 300, height=100, delta=3)
        self.make_hill(250, 250, 450, 250, height=100, delta=3)
        self.make_hill(350, 300, 550, 300, height=100, delta=3)

        cloud1 = self.make_cloud(100, 120)
        cloud2 = self.make_cloud(200, 140)
        cloud3 = self.make_cloud(300, 80)
        self.clouds = [cloud1, cloud2, cloud3]

        # Cave
        platform1 = self.canvas.create_rectangle(220, START_Y - 110, 320, START_Y, fill='coral')
        platform2 = self.canvas.create_rectangle(315, START_Y - 110, 420, START_Y - 60, fill='coral')
        platform3 = self.canvas.create_rectangle(315, START_Y - 30, 435, START_Y, fill='coral')

        # Big tree branches
        platform4 = self.canvas.create_rectangle(0, START_Y - 200, 150, START_Y - 193, fill='coral')
        platform5 = self.canvas.create_rectangle(WIDTH - 100, START_Y - 200, WIDTH, START_Y-193, fill='coral')
        platform6 = self.canvas.create_rectangle(0, START_Y - 100, 50, START_Y - 95, fill='coral')

        # Small Tree Trunks
        platform7 = self.canvas.create_rectangle(115, START_Y - 95, 120, START_Y, fill='coral')
        platform8 = self.canvas.create_rectangle(315, START_Y - 205, 320, START_Y - 110, fill='coral')

        self.platforms = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8]

        self.start = self.canvas.create_rectangle(0, 0, 10, START_Y, fill='coral')
        self.stop = self.canvas.create_rectangle(WIDTH-10, 0, WIDTH+3, START_Y, fill='coral')
        self.ground = self.canvas.create_rectangle(0, START_Y-5, WIDTH, START_Y, fill='coral')

    def make_hill(self, x1, y1, x2, y2, height=100, delta=3):
        x_diff = 0
        y_diff = 0
        for i in range(int(height/delta) + 1):
            self.canvas.create_rectangle(x1+x_diff, y1-y_diff, x2-x_diff, y2+delta-y_diff, fill='brown', outline='')
            x_diff += delta
            y_diff += delta

    def make_cloud(self, x, y):
        diameter = 15
        diff = -20
        diff_size = abs(diff)/2
        id_list = []
        for i in range(5):
            if abs(diff) == diff_size * 2:
                id = self.canvas.create_oval(x - diameter/2 + diff, y - diameter/2, x + diameter/2 + diff,
                                             y + diameter/2, fill="white")
                id_list.append(id)
                diff += diff_size
                continue
            else:
                id1 = self.canvas.create_oval(x - diameter/2 + diff, y - diameter/2 - diff_size, x + diameter/2 + diff,
                                              y + diameter/2 - diff_size, fill="white")
                id2 = self.canvas.create_oval(x - diameter/2 + diff, y - diameter/2, x + diameter/2 + diff,
                                              y + diameter/2, fill="white")
                id3 = self.canvas.create_oval(x - diameter/2 + diff, y - diameter/2 + diff_size, x + diameter/2 + diff,
                                              y + diameter/2 + diff_size, fill="white")

                id_list += [id1, id2, id3]
                diff += diff_size

        return id_list

    def get_obstacles(self):
        return [self.ground, self.start, self.stop] + self.platforms
    
    def update(self):
        # Moving the clouds
        cloud_speed = 0.1
        canvas_width = int(self.canvas.cget('width'))
        for cloud in self.clouds:
            for id in cloud:
                x1, y1, x2, y2 = self.canvas.coords(id)
                if x1 >= canvas_width:
                    self.canvas.moveto(id, 0 - abs(x2-x1), y1)

                self.canvas.move(id, cloud_speed, 0)


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


class AI:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.spider = self.make_spider(x, y)
        self.thread = self.canvas.create_line(x+10, 0, x+10, y+5, fill='ivory2', width=3)
        self.x, self.y = 0, 0.5

    def make_spider(self, x, y):

        color1 = 'black'
        head = canvas.create_oval(5, 5, 15, 13, fill=color1)
        torso = canvas.create_oval(0, 10, 20, 40, fill=color1)
        legs = [canvas.create_line(-5-i*5, 10*i+5, 5, 10*i+15,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(15, 10*i+15, 25+i*5, 10*i+5,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(-10+i*5, 10*i+35, 5, 10*i+25,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(15, 10*i+25, 30-i*5, 10*i+35,
                                   fill=color1, width=4) for i in range(2)]
                 
        spider = [head, torso] + legs
        for part in spider:
            self.canvas.move(part, x, y)
        return spider

    def update(self, eatable):
        pass


class Avatar:
    def __init__(self, canvas):
        color1 = 'lime'
        color2 = 'sandybrown'
        self.canvas = canvas
        self.head = self.canvas.create_oval(0, 0, 10, 10, fill=color2)
        self.torso = self.canvas.create_rectangle(0, 10, 10, 20,
                                                  fill=color1)
        self.canvas.move(self.head, START_X, START_Y-26)
        self.canvas.move(self.torso, START_X, START_Y-26)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.canvas.bind_all('<KeyPress-Down>', self.move)

        self.x = 1
        self.y = 0
        self.acceleration = 0.05  # gravitational acceleration in units of distance units/clock tick squared
        self.fallspeed = 0
        self.jumping = False
    
    def update(self, land, trophy):  # call find_trophy and hit_object, check if jumping up or falling, etc.

        for object in land.get_obstacles():
            self.hit_object(object)

        if self.jumping:
            self.y = self.fallspeed
            self.fallspeed += self.acceleration

        self.canvas.move(self.head, self.x, self.y)
        self.canvas.move(self.torso, self.x, self.y)

    def move(self, event=None):
        if event.keysym == 'Left':
            self.x = -1
        elif event.keysym == 'Right':
            self.x = 1
        elif event.keysym == 'Up':  # jumping
            if not self.jumping:
                self.fallspeed = -2
                self.jumping = True
        elif event.keysym == 'Down':
            self.y = 1
   
    def hit_object(self, obj):
        x1, y1, dummyx2, dummyy2 = self.canvas.coords(self.head)
        dummyx1, dummyy1, x2, y2 = self.canvas.coords(self.torso)
        ox1, oy1, ox2, oy2 = self.canvas.coords(obj)
        if (ox1 <= x1 <= ox2 and oy1 <= y1 <= oy2) or (ox1 <= x2 <= ox2 and oy1 <= y2 <= oy2):
            # Top collision
            if y1 < oy1 <= y2 <= oy2:
                self.y = -1
                self.jumping = False
                self.fallspeed = 0
            # Bottom collision
            elif oy1 <= y1 <= oy2 < y2:
                self.y = 1
            # Left collision
            elif ox1 <= x2 <= ox2:
                self.x = -1
            # Right collision
            elif ox1 <= x1 <= ox2:
                self.x = 1
    
    def find_trophy(self, trophy):
        pass


if __name__ == '__main__':
    
    tk = Tk()
    tk.title('Skyland')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    game = Skyland(canvas)
    mainloop()
