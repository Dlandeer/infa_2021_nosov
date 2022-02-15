import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-1000,1000.01,0.01)
fx=input()
with plt.xkcd():
    eval(fx)
    plt.grid(True)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x)$')
plt.show()