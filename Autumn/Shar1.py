from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
numb=1
e = Entry(width=20)
e1 = Entry(width=20)
b = Button(text="Начать игру")
beg = Label(text="Введите имя")
beg1 =Label(text= "Введите число шаров")
quit1=Button(text="Выход")
quit12=Button(text="Выход")
quit13=Button(text="Выход")
beg.pack()
e.pack()
beg1.pack()
e1.pack()
b.pack()
score1=0 
colors = ['red','orange','yellow','green','blue']
canv = Canvas(root,bg='white')
canv2 = Canvas(root,bg='white')
canv1=Canvas(root,width=90,height=20,bg="white")
def start(event):
    global numb, name
    name=e.get()
    numb=e1.get()
    numb=int(numb)
    e.destroy()
    b.destroy()
    e1.destroy()
    beg.destroy()
    beg1.destroy()
    canv1.pack()
    canv1.create_text(0,10,text="Score:",anchor=W,fill="grey",font="Verdana 14")
    canv.pack(fill=BOTH,expand=1)
    quit1.pack()
b.bind('<Button-1>', start)
class Ball(object):
    def __init__(self,x,y,r,vx,vy,c):
        self.x=x
        self.y=y
        self.r=r
        self.vx=vx
        self.vy=vy
        self.c=c
Balls=[]
def moving_ball():
    canv.delete(ALL)
    global job2
    for i in range(numb):
        Balls[i].x=Balls[i].x+Balls[i].vx*(0.01)
        Balls[i].y=Balls[i].y+Balls[i].vy*(0.01)
        if Balls[i].x+Balls[i].r>=800 or Balls[i].x-Balls[i].r <=0:
            Balls[i].vx=-Balls[i].vx
        if Balls[i].y+Balls[i].r >= 600 or Balls[i].y-Balls[i].r <=0:
            Balls[i].vy=-Balls[i].vy
        canv.create_oval(Balls[i].x-Balls[i].r,Balls[i].y-Balls[i].r,Balls[i].x+Balls[i].r,Balls[i].y+Balls[i].r,fill = Balls[i].c, width=0)
    job2=root.after(10,moving_ball)
    
def new_ball():
    canv.delete(ALL)
    global job1
    for i in range(numb):
        Balls.append(Ball(rnd(100, 700),rnd(100, 500),rnd(30, 50),rnd(-10,10),rnd(-10,10),choice(colors)))
    for i in range(numb):
        canv.create_oval(Balls[i].x-Balls[i].r,Balls[i].y-Balls[i].r,Balls[i].x+Balls[i].r,Balls[i].y+Balls[i].r,fill = Balls[i].c, width=0)
    moving_ball()
    job1=root.after(1000,new_ball)
boss1=[]
boss1.append(Ball(400,300,100,0,0,choice(colors)))
def boss():
    global job3
    canv2.delete(ALL)
    boss1[0].x=rnd(100,700)
    boss1[0].y=rnd(100,500)
    boss1[0].c=choice(colors)
    canv2.create_oval(boss1[0].x-boss1[0].r,boss1[0].y-boss1[0].r,boss1[0].x+boss1[0].r,boss1[0].y+boss1[0].r,fill=boss1[0].c,width=0)
    job3=root.after(100,boss)
    
def click(event):
    global score1
    for i in range(numb):
        x1=int(Balls[i].x)
        y1=int(Balls[i].y)
        if abs((event.x-x1))**2+abs((event.y-y1))**2<=Balls[i].r**2 :
            score1=score1+1
            Balls[i].r=0
            if score1==numb:
                root.after_cancel(job1)
                root.after_cancel(job2)
                canv.destroy()
                quit1.destroy()
                quit12.pack()
                canv2.pack(fill=BOTH,expand=1)
                boss()
                root.after(100000,quit_afterboss)
            canv1.delete(ALL)
            canv1.create_text(0,10,text="Score:",anchor=W,fill="grey",font="Verdana 14")
            canv1.create_text(70,10,text=score1,anchor=W,fill="grey",font="Verdana 14")
def quit():
    F=open("Highscore.txt","a")
    F.write("\n")
    F.write(name)
    F.write(" - ")
    r=str(score1)
    F.write(r)
    H=list()
    with open("Highscore.txt","r") as F:
        H.append(F.read())
    root.after_cancel(job2)
    root.after_cancel(job1)
    canv.destroy()
    canv1.destroy()
    quit1.destroy()
    quit13.pack()
    G=Label(text=H[0])
    G.pack()
def quit_afterboss():
    F=open("Highscore.txt","a")
    F.write("\n")
    F.write(name)
    F.write(" - ")
    r=str(score1)
    F.write(r)
    H=list()
    with open("Highscore.txt","r") as F:
        H.append(F.read())
    root.after_cancel(job3)
    canv2.destroy()
    quit12.destroy()
    quit13.pack()
    G=Label(text=H[0])
    G.pack()
def quit_afterbosse(event):
    quit_afterboss()
def boss_hit(event):
    global score1    
    x2=int(boss1[0].x)
    y2=int(boss1[0].y)
    if abs((event.x-x2))**2+abs((event.y-y2))**2<=boss1[0].r**2 :
        boss1[0].r=boss1[0].r-10
    if boss1[0].r==0:
        score1=score1+100
        quit_afterboss()
def quit_full(event):
    root.destroy()

def quit2(event):
    quit()
quit1.bind('<Button-1>',quit2)
quit12.bind('<Button-1>', quit_afterbosse)
quit13.bind('<Button-1>',quit_full)
new_ball()
canv.bind('<Button-1>', click)
canv2.bind('<Button-1>',boss_hit)
root.mainloop()
mainloop()