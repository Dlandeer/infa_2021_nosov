import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
p,v=np.polyfit(x,y,deg=1,cov=True)
x=np.arange(0,5.01,0.01)
y=np.arange(-1,1.01,0.01)
p1=np.poly1d(p)
plt.plot(x,p1(x),x,v[0][0]*x**2 +(v[0][1]+v[1][0])*x+ v[1][1])
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'Expiriment')
plt.show()