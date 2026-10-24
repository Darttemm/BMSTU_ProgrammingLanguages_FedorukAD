from collections import Counter

def process(matrix: list[list[int]]) -> tuple[list[list[int]], Counter[int]]:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("Матрица должна быть квадратной и непустой")
    transposed = [list(column) for column in zip(*matrix)]
    frequencies = Counter(value for row in matrix for value in row)
    return transposed, frequencies

def main() -> None:
    try:
        n = int(input("Порядок матрицы n: "))
        if n <= 0: raise ValueError("n должен быть положительным")
        print("Введите строки матрицы:")
        matrix = [list(map(int, input().split())) for _ in range(n)]
        if any(len(row) != n for row in matrix): raise ValueError("В каждой строке должно быть n целых чисел")
        transposed, frequencies = process(matrix)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    print("Транспонированная матрица:")
    for row in transposed: print(*row)
    print("Частоты:")
    for value, count in sorted(frequencies.items()): print(f"{value}: {count}")

if __name__ == "__main__": main()
