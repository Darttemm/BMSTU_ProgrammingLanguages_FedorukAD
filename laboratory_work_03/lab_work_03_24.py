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

def in_gray_region(x: float, y: float, radius: float) -> bool:
    if radius <= 0 or abs(x) > radius or abs(y) > radius:
        return False
    if x <= 0 <= y and x*x + y*y <= radius*radius:
        return False
    if x >= 0 >= y and x*x + y*y <= radius*radius:
        return False
    if x >= 0 and y >= 0 and x + y <= radius:
        return False
    if x <= 0 and y <= 0 and x + y >= -radius:
        return False
    return True

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

def random_shots(radius: float, seed: int = 24) -> list[tuple[float, float, bool]]:
    if radius <= 0:
        raise ValueError("Радиус должен быть положительным")
    rng = Random(seed)
    results = []
    for _ in range(10):
        x = rng.uniform(-radius, radius)
        y = rng.uniform(-radius, radius)
        results.append((x, y, in_gray_region(x, y, radius)))
    return results

def main() -> None:
    try:
        x0, x1, dx = map(float, input("Интервал графика xнач, xкон, dx: ").split())
        if not -5 <= x0 <= x1 <= 5 or dx <= 0:
            raise ValueError("Нужны -5<=xнач<=xкон<=5 и dx>0")
        print("Таблица графика: x\ty")
        x = x0
        while x <= x1 + dx * 1e-10:
            try:
                value = f"{graph_y(x):.6f}"
            except ValueError:
                value = "нет"
            print(f"{x:.3f}\t{value}")
            x += dx
        radius = float(input("Радиус области R: "))
        print("Выстрелы: X\tY\tРезультат")
        for x, y, hit in random_shots(radius):
            print(f"{x:.3f}\t{y:.3f}\t{'Попадание' if hit else 'Промах'}")
        a, b, step, eps = map(float, input("Интервал ряда xнач, xкон, dx, eps: ").split())
        if not -1 < a <= b <= 1 or step <= 0 or eps <= 0:
            raise ValueError("Для ряда нужны -1<xнач<=xкон<=1, dx>0, eps>0")
        print("Ряд: x\tS(x)\tN")
        x = a
        while x <= b + step * 1e-10:
            value, terms = fourth_root_series(x, eps)
            print(f"{x:.3f}\t{value:.6f}\t{terms}")
            x += step
    except ValueError as error:
        print(f"Ошибка: {error}")

if __name__ == "__main__": main()
