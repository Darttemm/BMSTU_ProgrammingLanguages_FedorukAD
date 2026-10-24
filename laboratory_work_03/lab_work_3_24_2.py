from math import log, tan
from random import Random

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

def main():
    try:
        r=float(input('R: '))
        for i,(x,y,hit) in enumerate(random_shots(r),1):
            print(f'{i}: x={x:.3f}, y={y:.3f} — {"Попадание" if hit else "Промах"}')
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
