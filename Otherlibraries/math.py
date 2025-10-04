import matplotlib.pyplot as plt
import numpy as np
x = np.sin(np.linspace(10, 100, 100))
y = np.cos(x)
z = np.tan(np.linspace(1, 10, 10))
lsit = [1,2,3,4,5,6,7,8,9]
lsit2 = bin(lsit[1])
plt.plot(x, y,z)
plt.legend(['X vs Y', 'Z'])
plt.bar(lsit, lsit2)
plt.title('Numpy and Matplotlib Plot')
plt.xlabel('X Output')
plt.ylabel('Y output')
plt.grid(True)
plt.show()
