import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-100,100,1000)

x = t**2+2*t+3

data = np.transpose([t,x])

np.savetxt("foo.csv", data, delimiter=",")

a, b = np.loadtxt("foo.csv", delimiter=',', usecols=(0, 1), unpack=True)

fig, ax = plt.subplots()
ax.plot(a, b)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud', title='Ejemplo CSV')
ax.grid()
plt.show()
