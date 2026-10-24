from math import log, tan, pi
from random import Random
import turtle

def y_graph(x: float) -> float:
    if x <= -2: return (-x-2)/3
    if x >= 2: return (x-2)/3
    value = tan(x/2)
    if abs(value) < 1e-10: raise ValueError("Разрыв графика")
    return log(abs(1/value))

def in_gray(x: float, y: float, r: float) -> bool:
    if abs(x)>r or abs(y)>r: return False
    if x<=0<=y and x*x+y*y<=r*r: return False
    if x>=0>=y and x*x+y*y<=r*r: return False
    if x>=0 and y>=0 and x+y<=r: return False
    if x<=0 and y<=0 and x+y>=-r: return False
    return True

def root_series(x: float, eps: float=1e-3) -> float:
    if not -1 < x <= 1: raise ValueError("Для ряда требуется -1<x<=1")
    total = term = 1.0; n = 1
    while True:
        term *= (0.25-n+1)*x/n
        if abs(term)<eps: return total
        total += term; n += 1

def draw() -> None:
    screen=turtle.Screen(); screen.title("Вариант 24 — графики и Монте-Карло")
    screen.setworldcoordinates(-5,-4,5,4); pen=turtle.Turtle(); pen.hideturtle(); pen.speed(0)
    pen.penup(); pen.goto(-5,0); pen.pendown(); pen.goto(5,0)
    pen.penup(); pen.goto(0,-4); pen.pendown(); pen.goto(0,4)
    pen.color("blue")
    for i in range(1001):
        x=-5+10*i/1000
        try: y=y_graph(x)
        except ValueError: pen.penup(); continue
        if abs(y)>4: pen.penup(); continue
        pen.goto(x,y); pen.pendown()
    rng=Random(24); r=1.0; pen.color("darkgreen"); hits=0
    for trial in range(10_000):
        x=rng.uniform(-r,r); y=rng.uniform(-r,r)
        if in_gray(x,y,r):
            hits += 1
            if trial < 1500:
                pen.penup(); pen.goto(3+x,2+y); pen.dot(3)
    estimate=4*r*r*hits/10_000; exact=(3-pi/2)*r*r
    print(f"Площадь ≈ {estimate:.4f}; точная площадь = {exact:.4f}; ошибка = {abs(estimate-exact)/exact*100:.2f}%")
    pen.color("red"); pen.penup()
    for i in range(201):
        x=-0.99+1.99*i/200
        y=root_series(x)
        pen.goto(x, y); pen.pendown()
    screen.mainloop()

if __name__ == "__main__": draw()
