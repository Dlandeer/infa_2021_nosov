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
beg.pack()
e.pack()
beg1.pack()
e1.pack()
b.pack()
score1=0 
colors = ['red','orange','yellow','green','blue']
canv = Canvas(root,bg='white')
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
    for i in range(0,numb):
        Balls[i].x=Balls[i].x+Balls[i].vx*(0.01)
        Balls[i].y=Balls[i].y+Balls[i].vy*(0.01)
        if Balls[i].x+Balls[i].r>=800 or Balls[i].x-Balls[i].r <=0:
            Balls[i].vx=-Balls[i].vx
        if Balls[i].y+Balls[i].r >= 600 or Balls[i].y-Balls[i].r <=0:
            Balls[i].vy=-Balls[i].vy
        canv.create_oval(Balls[i].x-Balls[i].r,Balls[i].y-Balls[i].r,Balls[i].x+Balls[i].r,Balls[i].y+Balls[i].r,fill = Balls[i].c, width=0)
    root.after(10,moving_ball)
    
def new_ball():
    canv.delete(ALL)
    for i in range(numb):
        Balls.append(Ball(rnd(100, 700),rnd(100, 500),rnd(30, 50),rnd(-10,10),rnd(-10,10),choice(colors)))
    for i in range(0,numb):
        canv.create_oval(Balls[i].x-Balls[i].r,Balls[i].y-Balls[i].r,Balls[i].x+Balls[i].r,Balls[i].y+Balls[i].r,fill = Balls[i].c, width=0)
    moving_ball()
    root.after(1000,new_ball)
  
  
def click(event):
    global score1
    for i in range(0,numb):
        x1=int(Balls[i].x)
        y1=int(Balls[i].y)
        if abs((event.x-x1))^2+abs((event.y-y1))^2<=Balls[i].r^2 :
            score1=score1+1
            Balls[i].r=0
            if score1==numb:
                quit()
            canv1.delete(ALL)
            canv1.create_text(0,10,text="Score:",anchor=W,fill="grey",font="Verdana 14")
            canv1.create_text(70,10,text=score1,anchor=W,fill="grey",font="Verdana 14")
def quit():
    F=open("Highscore.txt","a")
    F.write("\n")
    F.write(name)
    F.write(" - ")
    r=str(numb)
    F.write(r)
    H=list()
    with open("Highscore.txt","r") as F:
        H.append(F.read())
    canv.destroy()
    canv1.destroy()
    G=Label(text=H[0])
    G.pack()
def quit2(event):
    quit()
quit1.bind('<Button-1>',quit2)
new_ball()
canv.bind('<Button-1>', click)
root.mainloop()
mainloop()