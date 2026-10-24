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

def main():
    try: print(f'y = {graph_y(float(input("x: "))):.6f}')
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
