import turtle

def pos(t):
    t.penup()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.bk(600)
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
    t.fd(190)
    t.bk(190)
    t.rt(30)
    t.fd(190)
    t.penup()
    t.rt(80)
    t.fd(50)
    t.pendown()

def b(t):
    t.rt(85)
    t.fd(150)
    t.circle(50,350)
    t.penup()
    t.circle(50,100)
    t.fd(140)
    t.pendown()

def d(t):
    t.circle(50,450)
    t.fd(150)
    t.penup()
    t.bk(190)
    t.rt(90)
    t.fd(150)
    t.pendown()
   
 
def p(t):
    t.lt(90)
    t.fd(150)
    t.circle(50)
    t.penup()
    t.bk(420)
    t.rt(90)
    t.bk(1080)
    t.pendown()

def _t(t):
    t.lt(90)
    t.fd(150)
    t.circle(50)
    t.penup()
    t.bk(150)
    t.rt(90)
    t.fd(30)
    t.pendown()

def k(t):
    t.lt(55)
    t.fd(150)
    t.circle(50,250)
    t.fd(150)
    t.penup()
    t.lt(52)
    t.fd(100)
    t.pendown()

def g(t):
    t.penup()
    t.lt(90)
    t.fd(180)
    t.rt(210)
    t.pendown()
    t.fd(150)
    t.circle(50,250)
    t.fd(150)
    t.penup()
    t.bk(180)
    t.rt(125)
    t.fd(50)
    t.pendown()

def w(t):
    t.rt(95)
    t.circle(50,185)
    t.circle(50,-95)
    t.lt(93)
    t.fd(180)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.fd(180)
    t.pendown()

def f(t):
    t.lt(90)
    t.circle(50,180)
    t.circle(50,-90)
    t.lt(90)
    t.fd(180)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.pendown()

def full_stop(t):
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.fd(100)
    
    
t = turtle.Turtle()
t.pensize(3)
t.speed(50)
t.color('black')
pos(t)
a(t)
o(t)
i(t)
y(t)
e(t)
u(t)
b(t)
d(t)
p(t)
_t(t)
k(t)
g(t)
w(t)
f(t)
full_stop(t)
turtle.mainloop();
