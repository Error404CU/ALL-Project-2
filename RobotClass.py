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
        

    def up:

    def down:

    def left:

    def right:

    
