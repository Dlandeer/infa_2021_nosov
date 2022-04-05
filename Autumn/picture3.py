from graph import *
windowSize(500,600)
def unicorn(x,y,s):
    penColor("white")
    brushColor("white")
    oval(x+s,y+s/2,x-s,y-s/2)
    penSize(s/10)
    line(x+s-s/10,y,x+s-s/10,y+s)
    line(x-s+s/10,y,x-s+s/10,y+s+s/10)
    penSize(s/10+s/20)
    line(x+s-6*(s/10),y,x+s-6*(s/10),y+s+s/10)
    line(x-s+6*(s/10),y,x-s+6*(s/10),y+s)
    penSize(s/3)
    line(x+s-2*s/10,y,x+s-2*s/10,y-s)
    penSize(1)
    circle(x+s-s/5,y-3*s/4,s/3)
    oval(x+s-2*s/5,y-s+s/8,x+s+2*s/5,y-s+s/2)
    penColor(233,175,175)
    brushColor(233,175,175)
    p=[(x+s-s/5,y-s-s/20),(x+s,y-s),(x+s,y-2*s)]
    polygon(p)
    penColor(229, 128, 255)
    brushColor(229, 128, 255)
    circle(x+s-s/10,y-s+s/5,s/10)
    penColor("black")
    brushColor("black")
    circle(x+s-s/20,y-s+3*s/16,s/20)
    x1=x+s-s/10
    y1=y-s-s/20
    for i in range(1,15):
        if (i%2==0 and i>6) or i>10:
            x2=x1 -(i-5)*s/10
        else :
            x2=x1 -i*s/10
        if i> 8:    
            y2=y1 +(i-8)*s/40 +8*s/15
        else :
            y2=y1 + i*s/15
        r=randint(200,255)
        g=randint(200,255)
        b=randint(200,255)
        penColor(r,g,b)
        brushColor(r,g,b)
        oval(x2+s/5,y2+s/10,x2-s/5,y2-s/10)
    x1=x-s+s/10
    y1=y-s/10
    for i in range(1,30):
        x2=x1 -i*s/10
        if i%2==0 and i>6:
            x2=x1 - 6*s/10 +i*s/40
        if i%2==1 and i>6:
            x2=x1 - 6*s/10 +i*s/120
        if i> 8:    
            y2=y1 + 8*s/10 - (i-8)*s/40
        else :
            y2=y1 + i*s/10
        r=randint(200,255)
        g=randint(200,255)
        b=randint(200,255)
        penColor(r,g,b)
        brushColor(r,g,b)
        oval(x2+s/5,y2+s/10,x2-s/5,y2-s/10)
def tree(x,y,s):
    penColor(0,128,0)
    brushColor(0,128,0)
    oval(x+s,y+s/2,x-s,y-s/2)
    oval(x+s/2,y+3*s/2,x-s/2,y-s/2)
    oval(x+s/2,y-3*s/2,x-s/2,y+s/2)
    penColor(255,204,170)
    brushColor(255,204,170)
    circle(x+s/3,y-s,s/10)
    circle(x-s/3,y+s,s/10)
    circle(x+s-s/10,y-s/10,s/10)
    circle(x-s+s/10,y+s/10,s/10)
    penColor(230,230,230)
    brushColor(230,230,230)
    penSize(s/5)
    line(x,y+3*s/2,x,y+3*s)
brushColor(0,255,255)
penColor(0,255,255)
rectangle(0,0,500,300)
brushColor(0,255,0)
penColor(0,255,0)
rectangle(0,300,500,600)
tree(400,200,25)
tree(300,250,50)
tree(200,300,75)
tree(100,350,75)
unicorn(400,300,25)
unicorn(400,350,50)
unicorn(300,400,75)
unicorn(200,500,75)
brushColor(255,221,85)
penColor(255,221,85)
circle(500,50,100)
run()