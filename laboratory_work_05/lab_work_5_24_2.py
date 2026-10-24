from collections import Counter
def frequencies(a):
    if not a or any(len(row)!=len(a) for row in a): raise ValueError('Матрица должна быть квадратной')
    return Counter(v for row in a for v in row)
def main():
    try:
        n=int(input('Порядок n: '))
        if n<1: raise ValueError('n должно быть положительным')
        a=[list(map(int,input().split())) for _ in range(n)]
        if any(len(r)!=n for r in a): raise ValueError('Матрица должна быть квадратной')
        c=frequencies(a); print('Частоты:')
        for v in sorted(c): print(f'{v}: {c[v]}')
    except ValueError as e: print(f'Ошибка: {e}')
if __name__=='__main__': main()
