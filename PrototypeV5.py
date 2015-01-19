
__author__ = 'Radu'
# Importing libraries
from Tkinter import *
from datetime import datetime
import time
import random
import math

# --------------------------------------------------------------------------------------
# Window Defining
window = Tk()
w = Label(window, text = "Treasure Hunt!")
w.pack()
canvas = Canvas(window, width = 800, height = 600, bg = 'white')
canvas.pack(padx = 10, pady = 10)

# --------------------------------------------------------------------------------------
# Classes
class Robot(object):
    def __init__(self, x, y, size = 5, speed = 10, color = "black", score = 0, scored = 0):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.score = score
        self.scored = scored
    def drawRobot(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill = self.color)
    def scoreRobot(self, w, z):
        self.w = w
        self.z = z
        self.canvas.delete(self.scored)
        self.scored = canvas.create_text(self.w, self.z, text = "Robot 1 Score: %r" % self.score)
    def moveRobot(self, a, b):
        self.a = a
        self.b = b
        self.x += self.a
        self.y += self.b
        self.canvas.coords(self.shape, self.x, self.y, self.x + self.size, self.y + self.size)
        time.sleep(0.005)
        self.canvas.update()

class Landmark(object):
    def __init__(self, x, y, name = "", size = 50, color = 'black', lid = 0, tid = 0, v = 1, s = 0, txt = 0, txt2 = 0):
        self.x = x
        self.y = y
        self.name = name
        self.size = size
        self.color = color
        self.tid = tid                      # Treasure ID
        self.v = v                          # Valid
        self.s = s
        self.txt = txt
        self.txt2 = txt2
        self.lid = lid                      # Landmark ID
    def drawLandmark(self, canvas):
        self.canvas = canvas
        self.p = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill = self.color)
        self.txt = canvas.create_text(self.x + 15, self.y -8, text = self.name)
        self.canvas.update()
    def treasureFound(self,canvas):
        self.txt2 = canvas.create_text(self.x, self.y + self.size + 10, text = "Treasure %r found!!" %self.name )
        self.canvas.update()
    def deleteLandmark(self):
        self.canvas = canvas
        self.canvas.delete(self.p)
        self.canvas.delete(self.txt)
        self.canvas.delete(self.txt2)
        self.canvas.update()

# --------------------------------------------------------------------------------------
# Main body

listLmk = []                 # Landmark List
lnr = [9, 16, 25, 36, 49]    # Possible number of landmarks
nr = random.choice(lnr)
for i in range(1, nr + 1):
    x = "lmk" + str(i)
    listLmk.append(x)

rows = math.sqrt(nr)
spaceBetweenC = (800 - 50 * rows) / (rows + 1)
x = spaceBetweenC
spaceBetweenR = (600 - 50 * rows) / (rows + 1)
y = spaceBetweenR
count = 0               # Counter

for i in range(0, len(listLmk)):
    listLmk[i] = Landmark(x, y)
    listLmk[i].drawLandmark(canvas)
    if i >= 1:
        listLmk[i].lid = listLmk[i-1].lid + 1

    x += 50 + spaceBetweenC
    count += 1
    if count == rows:
        y += 50 + spaceBetweenR
        x = spaceBetweenC
        count = 0

r = Robot(10, 10, 10)
r.drawRobot(canvas)

# Collision detection
while r.x <= 800 and r.y <= 600:
    # r.moveRobot(random.randint(-1, 2), random.randint(-1, 2))
    r.moveRobot(0.3, 0.3)
    for i in range(0, len(listLmk)):
        if (r.y + r.size >= listLmk[i].y) and (r.y <= listLmk[i].y + listLmk[i].size) \
        and (r.x + r.size >= listLmk[i].x-5) and (r.x + r.size <= listLmk[i].x + listLmk[i].size):           # Left Side
            print "Left side detected", i
            r.moveRobot(0, 5)
        if (r.y <= listLmk[i].y + listLmk[i].size) and (r.y + r.size >= listLmk[i].y) \
        and (r.x >= listLmk[i].x) and (r.x <= listLmk[i].x + listLmk[i].size + 5):                           # Right Side
            print "Right side detected", i
            r.moveRobot(0, -5)
        if (r.y <= listLmk[i].y + listLmk[i].size) and (r.y + r.size >= listLmk[i].y - 10) \
        and (r.x + r.size >= listLmk[i].x) and (r.x <= listLmk[i].x + listLmk[i].size):                      # Up side
            print "Up side detected", i
            r.moveRobot(2, -1)
        if (r.y <= listLmk[i].y + listLmk[i].size + 11) and (r.y >= listLmk[i].y + listLmk[i].size) \
        and (r.x >= listLmk[i].x) and (r.x + r.size <= listLmk[i].x + listLmk[i].size):                      # Down side
            print "Down side detected", i
            r.moveRobot(-1, 1)

window.mainloop()
