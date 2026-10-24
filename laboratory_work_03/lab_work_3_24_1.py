from math import log, tan
from random import Random

def graph_y(x: float) -> float:
    if not -5 <= x <= 5:
        raise ValueError("Требуется -5 <= x <= 5")
    if x <= -2:
        return (-x - 2) / 3
    if x >= 2:
        return (x - 2) / 3
    tangent = tan(x / 2)
    if abs(tangent) < 1e-12:
        raise ValueError("Функция не определена при tan(x/2)=0")
    return log(abs(1 / tangent))

def main():
    try:
        a,b,dx=map(float,input('xнач, xкон, dx: ').split())
        if not -5<=a<=b<=5 or dx<=0: raise ValueError('Интервал или шаг недопустимы')
        print('x\\ty'); x=a
        while x<=b+dx*1e-10:
            try: y=f'{graph_y(x):.6f}'
            except ValueError: y='нет'
            print(f'{x:.3f}\\t{y}'); x+=dx
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
