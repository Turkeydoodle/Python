import  mathplotlib
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
plt.savefig('sine_wave.png')
