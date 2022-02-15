import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-1000,1000.01,0.01)
plt.plot(x,np.log((x**2+1)*np.exp(-np.absolute(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)**2))))
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x)=log_{1+tg\frac{1}{1+sin^2(x)}}(x^2+1)\exp\frac{-|x|}{10}})$')
plt.show()