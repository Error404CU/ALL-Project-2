from Tkinter import *
import random
import time

class robot:
    robotId = 0
    _vy = 0
    _vx = 0

    def __init__(self, x, y, speed=1.0, size=10, colour='blue'):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.colour = colour

    def drawRobot(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, fill=self.colour)

    def movement(self):
        v = self.speed

        self._vx += random.randint(-v, v)
        self._vy += random.randint(-v, v)
        self._vx = max(-v, min(self._vx, v))
        self._vy = max(-v, min(self._vy, v))

        self.x += self._vx
        self.y += self._vy

        self.canvas. coords(self.shape, self.x, self.y, self.x+self.size, self.y+self.size)
        self.canvas.update()
    

window = Tk()
canvas = Canvas(window, width = 600, height = 600, bg = 'white')
canvas.pack(padx=5, pady=5)

Robot1 = robot(200, 200, speed=2, size=10, colour='yellow')

Robot1.drawRobot(canvas)

for t in range(500):
    Robot1.movement()
    time.sleep(0.1)

window.mainloop()
