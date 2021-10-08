from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
numb=int(input())
x=[ 0 for _ in range(numb)]
y=[ 0 for _ in range(numb)]
r=[ 0 for _ in range(numb)]
vx=[ 0 for _ in range(numb)]
vy=[ 0 for _ in range(numb)]
c=[ 0 for _ in range(numb)]
canv = Canvas(root,bg='white')
canv1=Canvas(root,width=90,height=20,bg="white")
canv1.pack()
canv1.create_text(0,10,text="Score:",anchor=W,fill="grey",font="Verdana 14")
canv.pack(fill=BOTH,expand=1)
score1=0 
colors = ['red','orange','yellow','green','blue']
def moving_ball():
    canv.delete(ALL)
    global x,y,r,vx,vy,c
    for i in range(0,numb):
        x[i]=x[i]+vx[i]*(0.01)
        y[i]=y[i]+vy[i]*(0.01)
        if x[i]+r[i]>=800 or x[i]-r[i] <=0:
            vx[i]=-vx[i]
        if y[i]+r[i] >= 600 or y[i]-r[i] <=0:
            vy[i]=-vy[i]
        canv.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = c[i], width=0)
    root.after(10,moving_ball)
    
def new_ball():
    global x,y,r,vx,vy,c
    canv.delete(ALL)
    for i in range(0,numb):
        x[i] = rnd(100, 700)
        y[i] = rnd(100, 500)
        r[i] = rnd(30, 50)
        vx[i]=rnd(-10,10)
        vy[i]=rnd(-10,10)
        c[i]=choice(colors)
        canv.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = c[i], width=0)
    moving_ball()
    root.after(1000,new_ball)
  
  
def click(event):
    global score1
    for i in range(0,numb):
        x1=int(x[i])
        y1=int(y[i])
        if abs((event.x-x1))^2+abs((event.y-y1))^2<=r[i]^2 :
            score1=score1+1
            canv1.delete(ALL)
            canv1.create_text(0,10,text="Score:",anchor=W,fill="grey",font="Verdana 14")
            canv1.create_text(70,10,text=score1,anchor=W,fill="grey",font="Verdana 14")
new_ball()
canv.bind('<Button-1>', click)
mainloop()