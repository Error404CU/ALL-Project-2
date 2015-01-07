from Tkinter import *
import time
import random
root = Tk()
w = Label(root, text="Treasure Hunt")
w.pack()
canvas = Canvas(root, width = 1200, height = 800, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
canvas.pack()
canvas.pack(padx = 10, pady = 10)
gif1 = PhotoImage(file = 'EuropeMap.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)

Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
Score2 = canvas.create_text(150,20, text='Robot2 Score: 0')
    
widget = Label(canvas, text='AAA', fg='white', bg='black')

Lm1 = canvas.create_rectangle(270, 405, 270+30, 405+30, fill = 'green')

Lm2 = canvas.create_rectangle(460, 625, 460+30, 625+30, fill = 'green')

Lm3 = canvas.create_rectangle(820, 330, 820+30, 330+30, fill = 'green')

Lm4 = canvas.create_rectangle(135, 630, 135+30, 630+30, fill = 'green')

Lm5 = canvas.create_rectangle(470, 405, 470+30, 405+30, fill = 'green')

Lm6 = canvas.create_rectangle(760, 620, 760+30, 620+30, fill = 'green')

Lm7 = canvas.create_rectangle(405,730,405+30,730+30, fill = 'green')

Lm8 = canvas.create_rectangle(300,470,300+30,470+30, fill = 'green')

def Tr1():
    Tr1 = canvas.create_rectangle(270,405,270+10,405+10, fill = 'blue')
    return Tr1
def Tr2():
    Tr2 = canvas.create_rectangle(460,625,460+10,625+10, fill = 'blue')
    return Tr2
def Tr3():
    Tr3 = canvas.create_rectangle(820,330,820+10,330+10, fill = 'blue')
    return Tr3
def Tr4():
    Tr4 = canvas.create_rectangle(135,630,135+10,630+10, fill = 'blue')
    return Tr4
def Tr5():
    Tr5 = canvas.create_rectangle(470,405,470+10,405+10, fill = 'blue')
    return Tr5
def Tr6():
    Tr6 = canvas.create_rectangle(760,620,760+10,620+10, fill = 'blue')
    return Tr6
def Tr7():
    Tr7 = canvas.create_rectangle(405,730,405+10,730+10, fill = 'blue')
    return Tr7
def Tr8():
    Tr8 = canvas.create_rectangle(300,470,300+10,470+10, fill = 'blue')
    return Tr8

count = 0
    
my_list = [Tr1, Tr2, Tr3, Tr4, Tr5, Tr6, Tr7, Tr8]

Location = random.choice(my_list)
Location2 = random.choice(my_list)
Location3 = random.choice(my_list)

if Location == Tr1:
    print Tr1()
elif Location == Tr2:
    print Tr2()
elif Location == Tr3:
    print Tr3()
elif Location == Tr4:
    print Tr4()
elif Location ==Tr5:
    print Tr5()
elif Location == Tr6:
    print Tr6()
elif Location == Tr7:
    print Tr7()
elif Location == Tr8:
    print Tr8()
if Location2 == Tr1:
    print Tr1()
elif Location2 == Tr2:
    print Tr2()
elif Location2 == Tr3:
    print Tr3()
elif Location2 == Tr4:
    print Tr4()
elif Location2 == Tr5:
    print Tr5()
elif Location2 == Tr6:
    print Tr6()
elif Location2 == Tr7:
    print Tr7()
elif Location2 == Tr8:
    print Tr8()
if Location3 == Tr1:
    print Tr1()
elif Location3 == Tr2:
    print Tr2()
elif Location3 == Tr3:
    print Tr3()
elif Location3 == Tr4:
    print Tr4()
elif Location3 == Tr5:
    print Tr5()
elif Location3 == Tr6:
    print Tr6()
elif Location3 == Tr7:
    print Tr7()
elif Location3 == Tr8:
    print Tr8()

vx = 10.0
vy = 10.0

Ro1 = canvas.create_rectangle(20, 20, 20+10, 20+10)

def right():
    #instructs the robot to move the x coordinates one step to the right
    canvas.coords(Ro1,x1+vx,y1,x2+vx,y2)
    canvas.update()
    #wait 0.1 seconds before moving to the next step
    time.sleep(0.1)
    
def left():
    canvas.coords(Ro1, x1-vx,y1,x2-vx,y2)
    canvas.update()
    time.sleep(0.1)

def down():
    canvas.coords(Ro1, x1,y1+vy,x2,y2+vy)
    canvas.update()
    time.sleep(0.1)

def up():
    canvas.coords(Ro1, x1,y1-vy,x2,y2-vy)
    canvas.update()
    time.sleep(0.1)
def Dright():
    canvas.coords(Ro1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    time.sleep(0.1)
    
#the 'right' function is perfomed 10 times i.e it moves 10 steps (0.1 seconds between each loop)
for r in range(1, 43):
    #save the new coordinates the robot is now at
    x1,y1,x2,y2 = canvas.coords(Ro1)
    #perform the 'right' funtion at the new coordinates
    down()
for r in range(1,27):
    x1,y1,x2,y2 = canvas.coords(Ro1)
    right()
time.sleep(1.0)
if (Location == Tr1 or Location2 == Tr1 or Location3 == Tr1):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count
    for r in range(1,8):
        x1,y1,x2,y2 = canvas.coords(Ro1)
        down()
else:
    for r in range(1,8):
        x1,y1,x2,y2 = canvas.coords(Ro1)
        down()
for r in range(1,4):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    right()
time.sleep(1.0)
if (Location == Tr8 or Location2 == Tr8 or Location3 == Tr8):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count
for r in range(1,17):
    x1,y1,x2,y2=canvas.coords(Ro1)
    down()
for r in range(1,17):
    x1,y1,x2,y2=canvas.coords(Ro1)
    left()
time.sleep(1.0)
if (Location == Tr4 or Location2 == Tr4 or Location3 == Tr4):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count
    for r in range(1,10):
        x1,y1,x2,y2 = canvas.coords(Ro1)
        down()
else:
    for r in range(1,11):
        x1,y1,x2,y2 = canvas.coords(Ro1)
        down()
for r in range(1,27):
    x1,y1,x2,y2 = canvas.coords(Ro1)
    right()
time.sleep(1.0)
if (Location == Tr7 or Location2 == Tr7 or Location3 == Tr7):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')    
    print count
for r in range(1,4):
    x1,y1,x2,y2 = canvas.coords(Ro1)
    right()
for r in range(1,11):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    up()
for r in range(1,4):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    right()
time.sleep(1.0)
if (Location == Tr2 or Location2 == Tr2 or Location3 == Tr2):
    count +=100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count
    
for r in range(1,4):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    right()
for r in range(1,20):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    up()
for r in range(1,3):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    left()
for r in range(1,4):
    x1,y1,x2,y2 =canvas.coords(Ro1)
    up( )                  
time.sleep(1.0)
if (Location == Tr5 or Location2 == Tr5 or Location3 == Tr5):
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    count +=100
    print count
for r in range(1,22):
    x1,y1,x2,y2=canvas.coords(Ro1)
    Dright()
for r in range(1,9):
    x1,y1,x2,y2=canvas.coords(Ro1)
    right()
time.sleep(1.0)
if (Location == Tr6 or Location2 == Tr6 or Location3 == Tr6):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count
for r in range(1,5):
    x1,y1,x2,y2=canvas.coords(Ro1)
    left()
for r in range(1,20):
    x1,y1,x2,y2=canvas.coords(Ro1)
    up()
for r in range(1,11):
    x1,y1,x2,y2=canvas.coords(Ro1)
    right()
for r in range(1,11):
    x1,y1,x2,y2=canvas.coords(Ro1)
    up()
time.sleep(1.0)
if (Location == Tr3 or Location2 == Tr3 or Location3 == Tr3):
    count += 100
    if (count <= 0):
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 0')
    elif (count == 100):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 100')
    elif (count == 200):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 200')
    elif (count == 300):
        canvas.delete(Score1)
        Score1 = canvas.create_text(50,20, text='Robot1 Score: 300')
    print count

root.mainloop()

