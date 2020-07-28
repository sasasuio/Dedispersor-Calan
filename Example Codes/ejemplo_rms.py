import numpy as np 
import matplotlib.pyplot as plt

t = np.arange(0.0,3.0,0.01)

x = np.random.randn(len(t)) 
y = 5 * np.sin(2* np.pi *t)

z = np.array(x + y)

rms = np.sqrt(np.mean(z**2))

rms_p = len(t)*[rms]

fig, ax = plt.subplots()

ax.plot(t, z)
ax.plot(t, y, 'g--')	
ax.plot(t, rms_p)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud', title='Ejemplo RMS')
ax.grid()
plt.show()

