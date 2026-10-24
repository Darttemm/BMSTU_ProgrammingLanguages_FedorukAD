import turtle
from random import Random
from math import pi
def inside(x,y,r):
    if abs(x)>r or abs(y)>r:return False
    if x<=0<=y and x*x+y*y<=r*r:return False
    if x>=0>=y and x*x+y*y<=r*r:return False
    if x>=0 and y>=0 and x+y<=r:return False
    if x<=0 and y<=0 and x+y>=-r:return False
    return True
def estimate(r,n=10000):
    q=Random(24); hits=sum(inside(q.uniform(-r,r),q.uniform(-r,r),r) for _ in range(n)); exact=(3-pi/2)*r*r
    area=4*r*r*hits/n; return area,exact,abs(area-exact)/exact*100
def main():
    r=float(input('R: '))
    if r<=0:raise ValueError('R должно быть положительным')
    area,exact,error=estimate(r); s=turtle.Screen();s.title('Монте-Карло — вариант 24');s.setworldcoordinates(-r-.2,-r-.2,r+.2,r+.2)
    p=turtle.Turtle();p.hideturtle();p.speed(0);q=Random(24)
    for _ in range(10000):
        x=q.uniform(-r,r);y=q.uniform(-r,r);p.penup();p.goto(x,y);p.dot(3,'green' if inside(x,y,r) else 'lightgray')
    p.penup();p.goto(-r,-r);p.write(f'N=10000; S≈{area:.4f}; Sточн={exact:.4f}; ошибка={error:.2f}%');s.mainloop()
if __name__=='__main__':main()
