def transform(values: list[float], new_value: float) -> tuple[float, float, list[float]]:
    if len(values) < 2:
        raise ValueError("Нужно не менее двух элементов")
    minimum, maximum = min(values), max(values)
    if not minimum <= new_value <= maximum:
        raise ValueError("Новое значение должно находиться между Min и Max")
    min_index = values.index(minimum)
    max_index = values.index(maximum)
    insert_at = (min(min_index, max_index) + max(min_index, max_index)) // 2
    result = values.copy()
    result[insert_at + 1:] = result[insert_at:-1]
    result[insert_at] = new_value
    result.sort(key=lambda item: abs(item - new_value))
    return minimum, maximum, result

def main() -> None:
    try:
        values = list(map(float, input("Введите элементы массива: ").split()))
        new_value = float(input("Новое значение: "))
        minimum, maximum, result = transform(values, new_value)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    print(f"Min={minimum:g}; Max={maximum:g}")
    print("Результат:", " ".join(f"{item:.3f}" for item in result))

if __name__ == "__main__": main()
