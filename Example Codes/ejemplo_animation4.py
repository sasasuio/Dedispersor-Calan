
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

	
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([],[],lw=2)
	
def init():
    line.set_data([], [])
    return line,
	
def animate(t):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x -  0.001 * t))
    line.set_data(x, y)
    return line,
	
anim = animation.FuncAnimation(fig,animate,blit=True,interval=10,init_func=init,repeat=True)

plt.show()
