from pathlib import Path
from collections import Counter
def main():
    try:
        d=list(map(int,Path('input_3.txt').read_text(encoding='utf-8').split())); n=d[0]
        if n<1 or len(d)!=1+n*n: raise ValueError('Нужны n и n² элементов')
        a=[d[1+i*n:1+(i+1)*n] for i in range(n)]; t=[list(c) for c in zip(*a)]; c=Counter(d[1:])
        lines=['Транспонированная матрица:']+[' '.join(map(str,r)) for r in t]+['Частоты:']+[f'{v}: {c[v]}' for v in sorted(c)]
        Path('output_3.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    except (ValueError,OSError,IndexError) as e: print(f'Ошибка: {e}')
if __name__=='__main__': main()
