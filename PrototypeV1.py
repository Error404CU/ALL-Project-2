    # Importing libraries
from Tkinter import *
from datetime import datetime
import time
import random

    # Window Defining
window = Tk()
w = Label(window, text = "Treasure Hunt!")
w.pack()
canvas = Canvas(window, width = 800, height = 600, bg = 'white')
canvas.pack(padx = 10, pady = 10)

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
    def scoreRobot(self):
        self.canvas.delete(self.scored)
        self.scored = canvas.create_text(50, 20, text = "Robot 1 Score: %r" % self.score)
    def moveRobot(self, a, b):
        self.a = a
        self.b = b
        self.x += self.a
        self.y += self.b
        self.canvas.coords(self.shape, self.x, self.y, self.x + self.size, self.y + self.size)
        time.sleep(0.005)
        self.canvas.update()

class Landmark(object):
    def __init__(self, x, y, name, size = 30, color = 'black', t = 0, v = 1, s = 0, txt = 0, txt2 = 0):
        self.x = x
        self.y = y
        self.name = name
        self.size = size
        self.color = color
        self.t = t                      # Treasure
        self.v = v                      # Valid
        self.s = s
        self.txt = txt
        self.txt2 = txt2
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

    # Landmarks
lm1 = Landmark(random.randint(50, 100), random.randint(50, 100), "A")
lm1.drawLandmark(canvas)
lm2 = Landmark(random.randint(100, 500), random.randint(100, 500), "B")
lm2.drawLandmark(canvas)
lm3 = Landmark(random.randint(200, 500), random.randint(200, 500), "C")
lm3.drawLandmark(canvas)
lm4 = Landmark(random.randint(300, 400), random.randint(300, 400), "D")
lm4.drawLandmark(canvas)
lm5 = Landmark(random.randint(400, 500), random.randint(400, 500), "E")
lm5.drawLandmark(canvas)

    # Treasure selection
myL = [lm1, lm2, lm3, lm4, lm5]
for i in range(1, len(myL)-1):
    tr1 = random.choice(myL)
    myL.remove(tr1)
for i in range(0, len(myL)):
    myL[i].t = 1

    # Robot
r1 = Robot(10, 10, 10)
r1.drawRobot(canvas)
r1.scoreRobot()
myL = [lm1, lm2, lm3, lm4, lm5]
run = 1
tries = len(myL)
while run != 0:
    print "tries =", tries
    while tries > 0:
        max = 0
        copy = 0
        for i in myL:
            if i.v != 0:
                if (abs((r1.x + r1.y) - (i.x + i.y))) > max:
                    max = i.x + i.y
                    copy = i
        print "max =", max
        copy.v = 0
        tries -= 1
        myL.remove(copy)
        while abs((r1.x + r1.y) - (copy.x + copy.y)) > 30:
            if r1.x > copy.x:
                r1.moveRobot(-1, 0)
            else:
                r1.moveRobot(1, 0)
            if r1.y > copy.y:
                r1.moveRobot(0, -1)
            else:
                r1.moveRobot(0, 1)
        if copy.t == 1:
            print copy.name
            r1.score += 100
            r1.scoreRobot()
            copy.treasureFound(canvas)
        print tries

    run = 0
canvas.create_text(50,40, text = "Finish!")

window.mainloop()
