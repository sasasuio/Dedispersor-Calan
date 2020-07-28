
import numpy as np
import matplotlib.pyplot as plt


npoints = 20
slope = 2
offset = 3
x = np.arange(npoints)
y = slope * x + offset + np.random.normal(size=npoints) # y = m*x+n+random
p = np.polyfit(x,y,1)	# Last argument is degree of polynomial
fp = np.poly1d(p)		# So we can call fp(x)

print(fp)

p2 = np.polyfit(x,y,2)
fp2 = np.poly1d(p2)

print(fp2)

fig, ax = plt.subplots()
ax.plot(x,y,color="blue")
ax.plot(x,fp(x),color="red",linestyle='--')
ax.plot(x,fp2(x),color="orange",linestyle='--')
ax.grid()
plt.show()
