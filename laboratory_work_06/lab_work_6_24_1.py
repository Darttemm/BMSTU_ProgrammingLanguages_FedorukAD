from pathlib import Path
from math import isclose
def main():
    try:
        a,b,c=map(float,Path('input_1.txt').read_text(encoding='utf-8').split())
        if a==0 or b+c==0 or b*c==0 or a-b-c==0 or 1/a+1/(b+c)==0: raise ValueError('Нулевой знаменатель')
        z1=((1/a-1/(b+c))/(1/a+1/(b+c)))*(1+(b*b+c*c-a*a)/(2*b*c))/((a-b-c)/(a*b*c)); z2=(a-b-c)*a/2
        Path('output_1.txt').write_text(f'z1={z1:.6f}; z2={z2:.6f}; совпадают={isclose(z1,z2,rel_tol=1e-9,abs_tol=1e-9)}\n',encoding='utf-8')
    except (ValueError,OSError) as e: print(f'Ошибка: {e}')
if __name__=='__main__': main()
