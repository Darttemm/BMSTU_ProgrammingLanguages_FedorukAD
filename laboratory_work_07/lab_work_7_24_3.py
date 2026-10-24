from math import log, tan
from random import Random

def fourth_root_series(x: float, eps: float) -> tuple[float, int]:
    if not -1 < x <= 1 or eps <= 0:
        raise ValueError("Требуется -1 < x <= 1 и eps > 0")
    term = total = 1.0
    n = 1
    while True:
        term *= (0.25 - n + 1) * x / n
        if abs(term) < eps:
            break
        total += term
        n += 1
    return total, n

def main():
    import turtle
    s=turtle.Screen();s.title('Ряд (1+x)^(1/4), ε=10⁻³');s.setworldcoordinates(-1,-.1,1,1.3)
    axis=turtle.Turtle();axis.hideturtle();axis.speed(0);axis.penup()
    axis.goto(-1,0);axis.pendown();axis.goto(1,0);axis.penup();axis.goto(0,-.1);axis.pendown();axis.goto(0,1.3)
    for i in range(-10,11,2):
        x=i/10;axis.penup();axis.goto(x,-.025);axis.pendown();axis.goto(x,.025);axis.penup();axis.goto(x,-.08);axis.write(f'{x:.1f}',align='center')
    axis.penup();axis.goto(.88,.08);axis.write('X');axis.goto(.05,1.2);axis.write('Y')
    p=turtle.Turtle();p.hideturtle();p.speed(0);p.color('red');p.penup()
    for i in range(401):
        x=-.99+1.99*i/400;y=fourth_root_series(x,1e-3)[0];p.goto(x,y);p.pendown()
    s.mainloop()

if __name__=='__main__': main()
