import tkinter as tk
from tkinter import messagebox

def series(x: float, eps: float) -> float:
    total=term=1.0; n=1
    while True:
        term *= (0.25-n+1)*x/n
        if abs(term)<eps: return total
        total+=term; n+=1

def draw() -> None:
    try:
        xmin=float(entries[0].get()); xmax=float(entries[1].get())
        dx=float(entries[2].get()); eps=float(entries[3].get()); b=float(entries[4].get())
        if not (-1 < xmin <= xmax <= 1 and dx>0 and eps>0): raise ValueError
    except ValueError:
        messagebox.showwarning("Параметры", "Введите -1 < xmin ≤ xmax ≤ 1, dx > 0 и eps > 0")
        return
    points=[]; x=xmin
    while x<=xmax+dx*1e-9:
        points.append((x,series(x,eps), (1+x)**0.25+b)); x+=dx
    canvas.delete("all"); w=canvas.winfo_width(); h=canvas.winfo_height(); pad=45
    ys=[v for _,a,c in points for v in (a,c)]
    ymin=min(ys); ymax=max(ys); span=max(ymax-ymin,1e-9)
    px=lambda x: pad+(x-xmin)/(xmax-xmin or 1)*(w-2*pad)
    py=lambda y: h-pad-(y-ymin)/span*(h-2*pad)
    canvas.create_line(pad,py(0),w-pad,py(0),fill="#555")
    canvas.create_line(px(0),pad,px(0),h-pad,fill="#555")
    for index,color in ((1,"#1464a5"),(2,"#d1495b")):
        coords=[coord for x,a,c in points for coord in (px(x),py(a if index==1 else c))]
        if len(coords)>=4: canvas.create_line(*coords,fill=color,width=2,smooth=True)
    canvas.create_text(w/2,18,text="Вариант 24: (1+x)^(1/4) и смещённая функция",font=("Liberation Serif",12))
    canvas.create_text(w-140,35,text="Синий — ряд; красный — точная функция + b",fill="#333")

def main() -> None:
    global entries, canvas
    root=tk.Tk(); root.title("Лабораторная работа 8 — вариант 24"); root.geometry("900x600")
    bar=tk.Frame(root); bar.pack(fill="x",padx=8,pady=8)
    labels=("X нач","X кон","dx","ε","b"); defaults=("-0.9","0.9","0.05","0.001","0")
    entries=[]
    for label,value in zip(labels,defaults):
        tk.Label(bar,text=label).pack(side="left",padx=(8,2)); field=tk.Entry(bar,width=8); field.insert(0,value); field.pack(side="left"); entries.append(field)
    tk.Button(bar,text="Построить",command=draw).pack(side="left",padx=10)
    canvas=tk.Canvas(root,bg="white",width=880,height=520); canvas.pack(fill="both",expand=True,padx=8,pady=8)
    root.after(100,draw); root.mainloop()

if __name__ == "__main__": main()
