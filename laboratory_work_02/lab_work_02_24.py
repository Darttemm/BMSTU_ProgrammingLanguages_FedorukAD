from math import log, tan

def graph_y(x: float) -> float:
    if x < -5 or x > 5:
        raise ValueError("Для графика задан интервал [-5, 5]")
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
    # Белые четверти круга: II и IV квадранты.
    if x <= 0 <= y and x*x + y*y <= radius*radius:
        return False
    if x >= 0 >= y and x*x + y*y <= radius*radius:
        return False
    # Белые треугольники: I и III квадранты.
    if x >= 0 and y >= 0 and x + y <= radius:
        return False
    if x <= 0 and y <= 0 and x + y >= -radius:
        return False
    return True

def main() -> None:
    try:
        x = float(input("x графика (-5..5): "))
        print(f"y = {graph_y(x):.4f}")
        x, y, r = map(float, input("Введите x, y, R области: ").split())
        print("Точка принадлежит серой области" if in_gray_region(x, y, r) else "Точка не принадлежит серой области")
    except ValueError as error:
        print(f"Ошибка: {error}")

if __name__ == "__main__":
    main()
