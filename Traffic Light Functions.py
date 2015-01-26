    # Traffic lights position
tx1 = 1000
ty1 = 10
tx2 = 1050
ty2 = 60

    # Traffic Lights functions
def red (a) :
    for i in range (a) :
        red = canvas.create_oval(tx1, ty1, tx2, ty2, fill = "red")
        canvas.update()
        time.sleep(0.05)

def redb (a) :
    for i in range (a) :
        red = canvas.create_oval(tx1, ty1, tx2, ty2, fill = "black")
        canvas.update()
        time.sleep(0.05)

def green (a) :
    for i in range (a) :
        green = canvas.create_oval(tx1, ty1 + 50, tx2, ty2 + 50, fill = "green")
        canvas.update()
        time.sleep(0.001)

def greenb (a) :
    for i in range (a) :
        green = canvas.create_oval(tx1, ty1 + 50, tx2, ty2 + 50, fill = "black")
        canvas.update()
        time.sleep(0.05)

def lights() :
    red = canvas.create_oval(tx1, ty1, tx2, ty2, fill = "black")
    green = canvas.create_oval(tx1, ty1 + 50, tx2, ty2 + 50, fill = "black")
    
