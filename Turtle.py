import turtle as t
wn = t.Screen()
red = t.Turtle()
t.speed(10)
def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

def heart():
    red.fillcolor('purple')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

heart()
red.ht()
t.done()