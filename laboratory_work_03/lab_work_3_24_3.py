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
    try:
        a,b,dx,eps=map(float,input('xнач, xкон, dx, ε: ').split())
        if not -1<a<=b<=1 or dx<=0 or eps<=0: raise ValueError('Недопустимые параметры ряда')
        print('x\\tS(x)\\tN'); x=a
        while x<=b+dx*1e-10:
            v,n=fourth_root_series(x,eps); print(f'{x:.3f}\\t{v:.8f}\\t{n}'); x+=dx
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
