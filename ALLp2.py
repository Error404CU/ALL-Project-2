from Tkinter import *
window = Tk()
canvas = Canvas(window, width = 1200, height = 800, bg = 'yellow')
canvas.pack()
canvas.pack(padx = 10, pady = 10)

a1 = 120
a2 = 120
a3 = 60
a4 = 60
Lm1 = canvas.create_rectangle(a1, a2, a3, a4, fill = 'green')

b1 = 530
b2 = 530
b3 = 600
b4 = 600
Lm2 = canvas.create_rectangle(b1, b2, b3, b4, fill = 'green')

c1 = 1000
c2 = 300
c3 = 1070
c4 = 230

Lm3 = canvas.create_rectangle(c1, c2, c3, c4, fill = 'green')

d1 = 120
d2 = 680
d3 = 50
d4 = 750

Lm4 = canvas.create_rectangle(d1, d2, d3, d4, fill = 'green')

e1 = 370
e2 = 320
e3 = 300
e4 = 250

Lm5 = canvas.create_rectangle(e1, e2, e3, e4, fill = 'green')

f1 = 1010
f2 = 750
f3 = 930
f4 = 670

Lm6 = canvas.create_rectangle(f1, f2, f3, f4, fill = 'green')

window.mainloop()