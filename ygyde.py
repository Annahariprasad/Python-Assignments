import turtle

def pos(t):
    t.penup()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.bk(650)
    t.pendown()


def a(t):
    t.rt(90)
    for i in range(4):
        a = t.circle(50,180) if i%2==0 else t.fd(100)
    t.circle(50,180)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(120)
    t.pendown()
    
def o(t):
    t.rt(90)
    for i in range(4):
        a = t.circle(50,180) if i%2==0 else t.fd(100)
    t.penup()
    t.lt(90)
    t.fd(120)
    t.pendown()

def i(t):
    t.rt(90)
    for i in range(4):
        a = t.circle(50,180) if i%2==0 else t.fd(100)
    t.circle(50,90)
    t.lt(90)
    t.penup()
    t.fd(20)
    t.pendown()
    t.fd(155)
    t.penup()
    t.fd(20)
    t.pendown()
    t.penup()
    t.bk(190)
    t.rt(90)
    t.fd(80)
    t.pendown()

def y(t):
    t.fd(50)
    for i in range(3):
        a = t.circle(50,90) if i%2==0 else t.fd(80)
    t.fd(40)
    t.penup()
    t.lt(90)
    t.fd(180)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(180)
    t.rt(90)
    t.fd(60)
    t.lt(180)
    t.pendown()

def e(t):
    t.fd(50)
    for i in range(3):
        a = t.circle(50,90) if i%2==0 else t.fd(80)
    t.fd(60)
    t.penup()
    t.fd(90)
    t.pendown()

def u(t):
    t.lt(105)
    t.fd(180)
    t.bk(180)
    t.rt(30)
    t.fd(180)
    t.penup()
    t.bk(180)
    t.rt(80)
    t.fd(50)
    t.pendown()
    
t = turtle.Turtle()
t.pensize(3)
t.speed(50)
pos(t)
a(t)
o(t)
i(t)
y(t)
e(t)
u(t)
turtle.mainloop();
