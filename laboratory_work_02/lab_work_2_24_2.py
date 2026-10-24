from math import log, tan

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

def main():
    try:
        r,x,y=map(float,input('R, x, y: ').split())
        print('Попадает' if in_gray_region(x,y,r) else 'Не попадает')
    except ValueError as e: print(f'Ошибка: {e}')

if __name__=='__main__': main()
