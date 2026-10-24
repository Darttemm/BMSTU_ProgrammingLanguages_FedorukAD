from math import isclose

def calculate(a: float, b: float, c: float) -> tuple[float, float]:
    if a == 0 or b + c == 0 or b * c == 0 or a - b - c == 0:
        raise ValueError("В формуле появился нулевой знаменатель")
    if 1 / a + 1 / (b + c) == 0:
        raise ValueError("В формуле появился нулевой знаменатель")
    ratio = (1 / a - 1 / (b + c)) / (1 / a + 1 / (b + c))
    z1 = ratio * (1 + (b**2 + c**2 - a**2) / (2 * b * c)) / ((a - b - c) / (a * b * c))
    z2 = (a - b - c) * a / 2
    return z1, z2

def main() -> None:
    try:
        a, b, c = map(float, input("Введите a, b, c через пробел: ").split())
        z1, z2 = calculate(a, b, c)
    except ValueError as error:
        print(f"Ошибка ввода: {error}")
        return
    print(f"z1 = {z1:.6f}; z2 = {z2:.6f}")
    print("Результаты совпадают" if isclose(z1, z2, rel_tol=1e-9, abs_tol=1e-9) else "Результаты различаются")

if __name__ == "__main__":
    main()
