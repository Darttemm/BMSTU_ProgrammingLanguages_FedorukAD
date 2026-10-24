from collections import Counter

def process(matrix: list[list[int]]) -> tuple[list[list[int]], Counter[int]]:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("Матрица должна быть квадратной и непустой")
    transposed = [list(column) for column in zip(*matrix)]
    frequencies = Counter(value for row in matrix for value in row)
    return transposed, frequencies

def main():
    try:
        n=int(input('Порядок n: '))
        if n<1: raise ValueError('n должно быть положительным')
        a=[list(map(int,input().split())) for _ in range(n)]
        if any(len(r)!=n for r in a): raise ValueError('Матрица должна быть квадратной')
        b,_=process(a)
        print('Исходная матрица:'); [print(*r) for r in a]
        print('Транспонированная:'); [print(*r) for r in b]
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
