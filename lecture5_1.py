# pip install matplotlib
# pip install numpy
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=5, linestyle='dashed', color='green')
ax.set_xlabel('X', fontsize=14, color='red')
ax.set_ylabel('SIN(X)', fontsize=14, color='red')
ax.set_title('y=sin(x)\nDemo', color='yellow',
             backgroundcolor='black', fontsize=20)
ax.grid(True)
plt.show()
