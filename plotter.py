from matplotlib import pyplot as plt
import matplotlib.animation as animation
import bcolz
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    b = bcolz.open('db')
    yar = [j[0] for j in b[-10:]]
    xar = np.arange(len(yar))
    ax1.clear()
    ax1.plot(xar, yar)
    print(yar)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
