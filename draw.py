from turtle import Turtle
default_scale=10
def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t=Turtle()
    t.penup()
    drawman_scale(default_scale)
    x_current=0
    y_current=0
    t.goto(x_current,y_current)

def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale=scale
    grid(_drawman_scale)

def test_drawman():
    """
    Тестирование работы Чертёжника
    :return:None
    """
    pen_down()
    for i in range(5):
        on_vector(10,20)
        on_vector(0,-20)
    pen_up()
    to_point(0,0)
def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx,dy):
       to_point(x_current+dx,y_current+dy)

def to_point(x,y):
    global x_current, y_current
    x_current=x
    y_current=y
    t.goto(_drawman_scale*x,_drawman_scale*y)

def coordinates():
    t.goto(0,0)
    t.down()
    t.goto(0,300)
    t.goto(0,-300)
    t.goto(0,0)
    t.goto(350,0)
    t.goto(-350,0)
    t.penup()

def grid(scale):
    t.color("gray")
    t.goto(0,300)
    k=350//scale//2
    x=k
    for i in range(k):
        t.goto(x,300)
        t.pendown()
        t.goto(x,-300)
        x+=k
        t.penup()
    x=-k
    for i in range(k):
        t.goto(x,300)
        t.pendown()
        t.goto(x,-300)
        x-=k
        t.penup()
    k=300//scale//2
    x=k
    for i in range(k):
        t.goto(350,x)
        t.pendown()
        t.goto(-350,x)
        x+=k
        t.penup()
    x=-k
    for i in range(k):
        t.goto(350,x)
        t.pendown()
        t.goto(-350,x)
        x-=k
        t.penup()
    t.penup()
    t.color("black")
    coordinates()




init_drawman()
if __name__=='__main__':
    import time
    test_drawman()
    #time.sleep(10)

