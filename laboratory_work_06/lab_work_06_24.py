from collections import Counter
from pathlib import Path

def process_file(input_path: Path, output_path: Path) -> None:
    tokens = input_path.read_text(encoding="utf-8").split()
    if not tokens: raise ValueError("Входной файл пуст")
    mode, *data = tokens
    if mode == "formula":
        a, b, c = map(float, data)
        if a == 0 or b+c == 0 or b*c == 0 or 1/a+1/(b+c) == 0 or a-b-c == 0:
            raise ValueError("Недопустимые значения для формулы")
        z1 = ((1/a-1/(b+c))/(1/a+1/(b+c))) * (1+(b*b+c*c-a*a)/(2*b*c)) / ((a-b-c)/(a*b*c))
        z2 = (a-b-c)*a/2
        result = f"z1={z1:.6f}\nz2={z2:.6f}\n"
    elif mode == "array":
        n = int(data[0]); values = list(map(float, data[1:n+1])); new_value = float(data[n+1])
        if len(values) != n or n < 2: raise ValueError("Неверная длина массива")
        lo, hi = min(values), max(values)
        if not lo <= new_value <= hi: raise ValueError("Новое значение вне [Min, Max]")
        imin, imax = values.index(lo), values.index(hi)
        pos = (min(imin, imax)+max(imin, imax))//2
        values[pos+1:] = values[pos:-1]; values[pos] = new_value
        values.sort(key=lambda value: abs(value-new_value))
        result = " ".join(f"{v:.3f}" for v in values)+"\n"
    elif mode == "matrix":
        n = int(data[0]); flat = list(map(int, data[1:]))
        if n < 1 or len(flat) != n*n: raise ValueError("Нужно n² целых элементов матрицы")
        matrix = [flat[i*n:(i+1)*n] for i in range(n)]
        transposed = list(zip(*matrix)); counts = Counter(flat)
        result = "Транспонированная матрица:\n" + "\n".join(" ".join(map(str,row)) for row in transposed)
        result += "\nЧастоты:\n" + "\n".join(f"{k}: {v}" for k,v in sorted(counts.items()))+"\n"
    else:
        raise ValueError("Режим должен быть formula, array или matrix")
    output_path.write_text(result, encoding="utf-8")

def main() -> None:
    try: process_file(Path("input.txt"), Path("output.txt"))
    except (ValueError, OSError, IndexError) as error: print(f"Ошибка обработки: {error}")

if __name__ == "__main__": main()
