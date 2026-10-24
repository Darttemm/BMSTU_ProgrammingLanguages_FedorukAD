import turtle
from math import log,tan
def f(x):
    if x<=-2:return (-x-2)/3
    if x>=2:return (x-2)/3
    t=tan(x/2)
    if abs(t)<1e-10:raise ValueError
    return log(abs(1/t))
def main():
    s=turtle.Screen(); s.title('График функции — вариант 24'); s.setworldcoordinates(-5,-2,5,4)
    axis=turtle.Turtle(); axis.hideturtle(); axis.speed(0); axis.penup()
    axis.goto(-5,0); axis.pendown(); axis.goto(5,0); axis.penup(); axis.goto(0,-2); axis.pendown(); axis.goto(0,4)
    for x in range(-5,6):
        axis.penup(); axis.goto(x,-.08); axis.pendown(); axis.goto(x,.08); axis.penup(); axis.goto(x,-.28); axis.write(str(x),align='center')
    axis.penup(); axis.goto(4.7,.18); axis.write('X'); axis.goto(.12,3.7); axis.write('Y')
    p=turtle.Turtle(); p.hideturtle(); p.speed(0); p.color('blue'); p.penup()
    for i in range(2001):
        x=-5+10*i/2000
        try:y=f(x)
        except ValueError:p.penup();continue
        if -2<=y<=4:p.goto(x,y);p.pendown()
        else:p.penup()
    s.mainloop()
if __name__=='__main__':main()
