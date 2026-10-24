from pathlib import Path
def main():
    try:
        d=list(map(float,Path('input_2.txt').read_text(encoding='utf-8').split())); n=int(d[0]); a=d[1:n+1]; v=d[n+1]
        if len(d)!=n+2 or n<2: raise ValueError('Ожидаются n>=2, n элементов и новое значение')
        lo,hi=min(a),max(a)
        if not lo<=v<=hi: raise ValueError('Новое значение вне [Min,Max]')
        i,j=a.index(lo),a.index(hi); k=(min(i,j)+max(i,j))//2; a[k+1:]=a[k:-1]; a[k]=v; a.sort(key=lambda x:abs(x-v))
        Path('output_2.txt').write_text(f'Min={lo}; Max={hi}\n'+' '.join(map(str,a))+'\n',encoding='utf-8')
    except (ValueError,OSError,IndexError) as e: print(f'Ошибка: {e}')
if __name__=='__main__': main()
