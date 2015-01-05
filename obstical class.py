from tkinter import *
import random

class obstacle:
    def _init__(self,x, y, size=4,:
        self.x = x
        self.y = y
        self.xEnd = x + size
        self.yEnd = y + size
        self.size= x + size
        self.colour=colour
        
    def drawobstacle(self,canvas):
        self.shape = canvas.create_rectangle(self.x,self.xEnd,self.yEnd,Fill='Pink')
        
