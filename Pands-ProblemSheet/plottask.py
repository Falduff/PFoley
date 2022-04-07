#plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

import matplotlib.pyplot as plt
import numpy as np

#the 3 functions
x = np.linspace(0,4)
f = x
g = x**2
h = x**3

#plotting the functions
plt.plot (x,f,'y', label = "f(x) = x")
plt.plot (x,g, 'c', label = "g(x) = x^2")
plt.plot (x,h,'m', label = "h(x) = x^3")

plt.legend(loc='upper left')

plt.show()
