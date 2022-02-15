from array import array
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2,2.001,0.001)
def weir_funct(x):
    fw=0
    for n in range(1000000):
       fw=fw+ np.power(1/2,n)*np.cos(np.power(3,n)*np.pi*x)
    return fw
plt.plot(x,weir_funct(x))
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x)=\sum_{n=0}^\infty a^n\cos{b^n\pi*x}$')
plt.show()