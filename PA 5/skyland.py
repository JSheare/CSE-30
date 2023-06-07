# cse30
# pa5
# skyland.py - a one-level platform video game
# author: Jacob Shearer
# date: 6/6/2023

from tkinter import *
import tkinter.font as font

WIDTH, HEIGHT = 600, 400
CLOCK_RATE = 5
START_X, START_Y = 20, 350
END_X, END_Y = 400, 350


class Skyland:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        self.canvas.bind_all('<KeyPress-Alt_L>', self.restart)
        self.paused = False
        self.done = False

        self.score = 0
        self.time = 0
        self.land = Land(canvas)
        self.trophy = Trophy(canvas)
        self.avatar = Avatar(canvas)
        self.spider1 = AI(canvas, 75, 110)
        self.spider2 = AI(canvas, 500, 305)
        self.text = canvas.create_text(150, 370, text=f'Score {self.avatar.score}  Time {self.time} ',
                                       font=font.Font(family='Helveca', size=15, weight='bold'))

        self.update()

    def restart(self, event=None):
        self.paused = False
        self.pause()
        self.canvas.after(CLOCK_RATE, self.pause)
        self.avatar.replace()
        self.trophy.replace()
        self.avatar.score = 0
        self.time = 0
        if self.avatar.death_mask is not None:
            for item in self.avatar.death_mask:
                self.canvas.delete(item)

            self.avatar.dead = False
            self.avatar.death_mask = None

        self.canvas.delete(self.text)
        self.text = canvas.create_text(150, 370, text=f'Score {self.avatar.score}  Time {"% .2f" % self.time} ',
                                       font=font.Font(family='Helveca', size=15, weight='bold'))
        self.done = False
        self.update()

    def pause(self, event=None):
        if not self.paused:
            self.paused = True
        else:

            self.paused = False
            self.update()

    def update(self):
        if not self.paused and not self.done:
            self.avatar.update(self.land, self.trophy)
            self.land.update()
            self.avatar.find_trophy(self.trophy)
            self.spider1.update(self.avatar, self.land)
            self.spider2.update(self.avatar, self.land)
            # Finish the game once the avatar finds all the eggs
            if self.avatar.score == 6:
                self.pause()
                self.done = True
                self.canvas.delete(self.text)
                self.text = canvas.create_text(150, 370,
                                               text=11*' ' + f'Score {self.avatar.score}  Time {"% .2f" % self.time} ' +
                                                              '   You win!',
                                               font=font.Font(family='Helveca', size=15, weight='bold'))
            # Finish the game if the avatar is killed by a spider
            elif self.avatar.dead:
                self.avatar.kill()
                self.done = True
                self.canvas.delete(self.text)
                self.text = canvas.create_text(150, 370,
                                               text=15*' ' + f'Score {self.avatar.score}  Time {"% .2f" % self.time} ' +
                                                    "   You've died.",
                                               font=font.Font(family='Helveca', size=15, weight='bold'))
            # Update the game normally
            else:
                self.canvas.after(CLOCK_RATE, self.update)

                self.time += CLOCK_RATE * 1e-3
                self.canvas.delete(self.text)
                self.text = canvas.create_text(150, 370, text=f'Score {self.avatar.score}  Time {"% .2f" % self.time} ',
                                               font=font.Font(family='Helveca', size=15, weight='bold'))


class Land:
    def __init__(self, canvas):
        self.canvas = canvas

        # sky
        self.canvas.create_rectangle(0, 0, WIDTH, START_Y - 100, fill='lightblue')
        # valley
        self.canvas.create_rectangle(0, START_Y - 120, WIDTH, START_Y, fill='limegreen')

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
        platform5 = self.canvas.create_rectangle(WIDTH - 100, START_Y - 240, WIDTH, START_Y - 233, fill='coral')
        platform6 = self.canvas.create_rectangle(0, START_Y - 100, 50, START_Y - 95, fill='coral')

        # Small Tree Trunks
        platform7 = self.canvas.create_rectangle(115, START_Y - 95, 120, START_Y, fill='coral')
        platform8 = self.canvas.create_rectangle(315, START_Y - 205, 320, START_Y - 110, fill='coral')

        # Moving platform
        platform9 = self.canvas.create_rectangle(300, START_Y - 280, 335, START_Y - 275, fill='coral')
        self.platform_x = 0.9

        self.platforms = [platform1, platform2, platform3, platform4,
                          platform5, platform6, platform7, platform8,
                          platform9]

        self.start = self.canvas.create_rectangle(0, 0, 10, START_Y, fill='coral')
        self.stop = self.canvas.create_rectangle(WIDTH - 10, 0, WIDTH + 3, START_Y, fill='coral')
        self.ground = self.canvas.create_rectangle(0, START_Y - 5, WIDTH, START_Y, fill='coral')

        # Decoration
        # Nests
        self.canvas.create_line(110, START_Y - 85, 125, START_Y - 80, 140, START_Y - 85,
                                smooth=True, fill='brown', width=5)  # Pink egg
        self.canvas.create_line(288, START_Y - 195, 303, START_Y - 190, 318, START_Y - 195,
                                smooth=True, fill='brown', width=5)  # Red egg
        self.canvas.create_line(WIDTH-55, START_Y - 242, WIDTH-40, START_Y - 237, WIDTH-25, START_Y - 242,
                                smooth=True, fill='brown', width=5)  # Light blue egg

        # Left small tree leaves
        self.canvas.create_line(115, START_Y - 95, 85, START_Y - 65, fill='green', width=5)
        self.canvas.create_line(115, START_Y - 85, 85, START_Y - 55, fill='green', width=5)
        self.canvas.create_line(115, START_Y - 75, 85, START_Y - 45, fill='green', width=5)
        self.canvas.create_line(115, START_Y - 65, 85, START_Y - 35, fill='green', width=5)
        self.canvas.create_line(115, START_Y - 55, 85, START_Y - 25, fill='green', width=5)
        self.canvas.create_line(115, START_Y - 45, 85, START_Y - 15, fill='green', width=5)

        self.canvas.create_line(120, START_Y - 95, 150, START_Y - 65, fill='green', width=5)
        self.canvas.create_line(120, START_Y - 85, 150, START_Y - 55, fill='green', width=5)
        self.canvas.create_line(120, START_Y - 75, 150, START_Y - 45, fill='green', width=5)
        self.canvas.create_line(120, START_Y - 65, 150, START_Y - 35, fill='green', width=5)
        self.canvas.create_line(120, START_Y - 55, 150, START_Y - 25, fill='green', width=5)
        self.canvas.create_line(120, START_Y - 45, 150, START_Y - 15, fill='green', width=5)

        # Middle small tree leaves
        self.canvas.create_line(315, START_Y - 205, 285, START_Y - 175, fill='green', width=5)
        self.canvas.create_line(315, START_Y - 195, 285, START_Y - 165, fill='green', width=5)
        self.canvas.create_line(315, START_Y - 185, 285, START_Y - 155, fill='green', width=5)
        self.canvas.create_line(315, START_Y - 175, 285, START_Y - 145, fill='green', width=5)
        self.canvas.create_line(315, START_Y - 165, 285, START_Y - 135, fill='green', width=5)
        self.canvas.create_line(315, START_Y - 155, 285, START_Y - 125, fill='green', width=5)

        self.canvas.create_line(320, START_Y - 205, 350, START_Y - 175, fill='green', width=5)
        self.canvas.create_line(320, START_Y - 195, 350, START_Y - 165, fill='green', width=5)
        self.canvas.create_line(320, START_Y - 185, 350, START_Y - 155, fill='green', width=5)
        self.canvas.create_line(320, START_Y - 175, 350, START_Y - 145, fill='green', width=5)
        self.canvas.create_line(320, START_Y - 165, 350, START_Y - 135, fill='green', width=5)
        self.canvas.create_line(320, START_Y - 155, 350, START_Y - 125, fill='green', width=5)

        # Big left tree leaves
        self.canvas.create_line(10, 100, 60, 125, 150, 110, smooth=True, fill='green', width=10)
        self.canvas.create_line(10, 70, 50, 95, 120, 80, smooth=True, fill='green', width=10)
        self.canvas.create_line(10, 40, 40, 65, 90, 50, smooth=True, fill='green', width=10)
        self.canvas.create_line(10, 10, 30, 35, 70, 20, smooth=True, fill='green', width=10)

        # Big right tree leaves
        self.canvas.create_line(WIDTH-10, 70, WIDTH-50, 95, WIDTH-120, 80, smooth=True, fill='green', width=10)
        self.canvas.create_line(WIDTH-10, 40, WIDTH-40, 65, WIDTH-90, 50, smooth=True, fill='green', width=10)
        self.canvas.create_line(WIDTH-10, 10, WIDTH-30, 35, WIDTH-70, 20, smooth=True, fill='green', width=10)

    def make_hill(self, x1, y1, x2, y2, height=100, delta=3):
        x_diff = 0
        y_diff = 0
        for i in range(int(height / delta) + 1):
            self.canvas.create_rectangle(x1 + x_diff, y1 - y_diff, x2 - x_diff, y2 + delta - y_diff, fill='brown',
                                         outline='')
            x_diff += delta
            y_diff += delta

    def make_cloud(self, x, y):
        diameter = 15
        diff = -20
        diff_size = abs(diff) / 2
        id_list = []
        for i in range(5):
            # Tips of the cloud
            if abs(diff) == diff_size * 2:
                id = self.canvas.create_oval(x - diameter / 2 + diff, y - diameter / 2, x + diameter / 2 + diff,
                                             y + diameter / 2, fill="white")
                id_list.append(id)
                diff += diff_size
                continue
            # Body of the cloud
            else:
                id1 = self.canvas.create_oval(x - diameter / 2 + diff, y - diameter / 2 - diff_size,
                                              x + diameter / 2 + diff,
                                              y + diameter / 2 - diff_size, fill="white")
                id2 = self.canvas.create_oval(x - diameter / 2 + diff, y - diameter / 2, x + diameter / 2 + diff,
                                              y + diameter / 2, fill="white")
                id3 = self.canvas.create_oval(x - diameter / 2 + diff, y - diameter / 2 + diff_size,
                                              x + diameter / 2 + diff,
                                              y + diameter / 2 + diff_size, fill="white")

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
                    self.canvas.moveto(id, 0 - abs(x2 - x1), y1)

                self.canvas.move(id, cloud_speed, 0)

        # Moving the oscillating platform
        platform_leftbound = 200
        platform_rightbound = 430
        x1, y1, x2, y2 = self.canvas.coords(self.platforms[-1])
        if x1 <= platform_leftbound or x2 >= platform_rightbound:
            self.platform_x = -self.platform_x

        self.canvas.move(self.platforms[-1], self.platform_x, 0)


class Trophy:
    def __init__(self, canvas):
        self.canvas = canvas
        purple_egg = self.canvas.create_oval(0, 0, 20, 10, fill='orchid')
        pink_egg = self.canvas.create_oval(0, 0, 20, 10, fill='pink')
        blue_egg = self.canvas.create_oval(0, 0, 20, 10, fill='blue')
        red_egg = self.canvas.create_oval(0, 0, 20, 10, fill='red')
        yellow_egg = self.canvas.create_oval(0, 0, 20, 10, fill='yellow')
        light_blue_egg = self.canvas.create_oval(0, 0, 20, 10, fill='light sky blue')

        # Moves eggs to initial positions
        self.canvas.moveto(purple_egg, 10, START_Y - 212)
        self.canvas.moveto(pink_egg, 115, START_Y - 95)
        self.canvas.moveto(blue_egg, 25, START_Y - 112)
        self.canvas.moveto(blue_egg, 25, START_Y - 112)
        self.canvas.moveto(red_egg, 293, START_Y - 205)
        self.canvas.moveto(yellow_egg, 320, START_Y - 42)
        self.canvas.moveto(light_blue_egg, WIDTH - 50, START_Y - 252)

        self.trophies = [purple_egg, pink_egg, blue_egg, red_egg, yellow_egg, light_blue_egg]

    def get_trophy(self):
        return self.trophies

    def replace(self):
        # Places each egg back in its original position (in order)
        self.canvas.moveto(self.trophies[0], 10, START_Y - 212)
        self.canvas.moveto(self.trophies[1], 115, START_Y - 95)
        self.canvas.moveto(self.trophies[2], 25, START_Y - 112)
        self.canvas.moveto(self.trophies[3], 293, START_Y - 205)
        self.canvas.moveto(self.trophies[4], 320, START_Y - 42)
        self.canvas.moveto(self.trophies[5], WIDTH - 50, START_Y - 252)


class AI:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.spider = self.make_spider(x, y)
        self.thread = self.canvas.create_line(x + 10, 0, x + 10, y + 5, fill='ivory2', width=3)
        self.y = 0.5
        self.prev_y = 0
        self.movement_counter = 0

    def make_spider(self, x, y):
        color1 = 'black'
        head = canvas.create_oval(5, 5, 15, 13, fill=color1)
        torso = canvas.create_oval(0, 10, 20, 40, fill=color1)
        legs = [canvas.create_line(-5 - i * 5, 10 * i + 5, 5, 10 * i + 15,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(15, 10 * i + 15, 25 + i * 5, 10 * i + 5,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(-10 + i * 5, 10 * i + 35, 5, 10 * i + 25,
                                   fill=color1, width=4) for i in range(2)] + \
               [canvas.create_line(15, 10 * i + 25, 30 - i * 5, 10 * i + 35,
                                   fill=color1, width=4) for i in range(2)]

        spider = [head, torso] + legs
        for part in spider:
            self.canvas.move(part, x, y)
        return spider

    def update(self, avatar, land):
        # Makes the spider lunge at the avatar
        X1, Y1, X2, Y2 = self.canvas.coords(avatar.torso)
        x1, y1, x2, y2 = self.canvas.coords(self.spider[1])
        if X1 <= x1 <= X2 or X1 <= x2 <= X2:
            if y2 >= Y2:
                self.y = -2
            else:
                self.y = 2

        # Checks to see if the avatar has been killed
        if (X1 <= x1 <= X2 and Y1 <= y1 <= Y2) or (X1 <= x2 <= X2 and Y1 <= y2 <= Y2) or \
                (X1 <= x1 <= X2 and Y1 <= y2 <= Y2) or (X1 <= x2 <= X2 and Y1 <= y2 <= Y2):
            avatar.dead = True

        closeness = 3
        for obstacle in land.get_obstacles():
            ox1, oy1, ox2, oy2 = self.canvas.coords(obstacle)
            # Potential collision from the top
            if oy1 <= (y2 + closeness) <= oy2 and (ox1 <= x1 <= ox2 or ox1 <= x2 <= ox2):
                self.y = -0.5
                self.prev_y = -0.5
                self.movement_counter += 1

            # Potential collision from the bottom
            elif oy1 <= (y1 - closeness) <= oy2 and (ox1 <= x1 <= ox2 or ox1 <= x2 <= ox2):
                self.y = 0.5
                self.prev_y = 0.5
                self.movement_counter += 1

        # The movement_counter is basically an attack cooldown
        if 0 < self.movement_counter < 140:
            self.y = self.prev_y
            self.movement_counter += 1

        if self.movement_counter >= 140:
            self.y = 0
            self.prev_y = 0
            self.movement_counter = 0

        for part in self.spider:
            self.canvas.move(part, 0, self.y)


class Avatar:
    def __init__(self, canvas):
        color1 = 'lime'
        color2 = 'sandybrown'
        self.canvas = canvas
        self.score = 0
        self.dead = False
        self.death_mask = None
        self.head = self.canvas.create_oval(0, 0, 10, 10, fill=color2)
        self.torso = self.canvas.create_rectangle(0, 10, 10, 20,
                                                  fill=color1)
        self.canvas.move(self.head, START_X, START_Y - 26)
        self.canvas.move(self.torso, START_X, START_Y - 26)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.canvas.bind_all('<KeyPress-Down>', self.move)

        self.x = 1
        self.y = 0
        self.acceleration = 0.020  # gravitational acceleration
        self.can_jump = False

    def update(self, land, trophy):  # call find_trophy and hit_object, check if jumping up or falling, etc.
        for object in land.get_obstacles():
            self.hit_object(object)

        self.canvas.move(self.head, self.x, self.y)
        self.canvas.move(self.torso, self.x, self.y)

        self.y += self.acceleration

    def move(self, event=None):
        if event.keysym == 'Left':
            self.x = -1
        elif event.keysym == 'Right':
            self.x = 1
        elif event.keysym == 'Up':  # jumping
            if self.can_jump:
                self.y = -2
                self.can_jump = False
        elif event.keysym == 'Down':
            self.y = 1

    def hit_object(self, obj):
        for appendage in [self.head, self.torso]:
            x1, y1, x2, y2 = self.canvas.coords(appendage)
            ox1, oy1, ox2, oy2 = self.canvas.coords(obj)
            if (ox1 <= x1 <= ox2 and oy1 <= y1 <= oy2) or (ox1 <= x2 <= ox2 and oy1 <= y2 <= oy2) or \
                    (ox1 <= x1 <= ox2 and oy1 <= y2 <= oy2) or (ox1 <= x2 <= ox2 and oy1 <= y2 <= oy2):
                # Top collision
                if y1 < oy1 <= y2 <= oy2:
                    self.y = -0.12
                    self.can_jump = True
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
        trophies = trophy.get_trophy()
        for trophy in trophies:
            X1, Y1, X2, Y2 = self.canvas.coords(trophy)
            x1, y1, x2, y2 = self.canvas.coords(self.torso)
            if (X1 <= x1 <= X2 and Y1 <= y1 <= Y2) or (X1 <= x1 <= X2 and Y1 <= y1 <= Y2) or \
                    (X1 <= x2 <= X2 and Y1 <= y1 <= Y2) or (X1 <= x2 <= X2 and Y1 <= y2 <= Y2):
                self.score += 1
                self.canvas.moveto(trophy, -30, -30)

    def replace(self):
        self.x = 1
        self.y = 0
        self.canvas.moveto(self.head, START_X, START_Y - 26)
        self.canvas.moveto(self.torso, START_X, START_Y - 16)

    def kill(self):
        hx1, hy1, hx2, hy2 = self.canvas.coords(self.head)
        tx1, ty1, tx2, ty2 = self.canvas.coords(self.torso)
        head = self.canvas.create_oval(hx1, hy1, hx2, hy2, fill='red')
        torso = self.canvas.create_rectangle(tx1, ty1, tx2, ty2, fill='red')
        self.death_mask = [head, torso]


if __name__ == '__main__':
    tk = Tk()
    tk.title('Skyland')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    game = Skyland(canvas)
    mainloop()
