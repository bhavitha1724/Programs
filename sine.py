import matplotlib.pyplot as plt
import numpy as np
fs=4000
f1=400
n=100
a=5
x=np.arange(n)
y=np.cos(2*np.pi*f1*x/fs)
plt.plot(x,(a*y))
plt.xlabel('x')
plt.ylabel('y')
plt.show() 
