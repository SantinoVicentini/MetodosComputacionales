import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(- 100, 100, 10000)
y = 4 * x ** 3 + 1.2 * x ** 2 + 12
plt.figure(0)
plt.plot(x, y)
plt.title("Prueba entorno" )
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
