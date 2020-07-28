import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-100,100,1000)

x = np.random.randn(len(t))

data = np.transpose([t,x])


while True:

	print("Para capturar el espectro presione 1")
	num = input()
	 
	if num == 1:
		plt.close()
		fig, ax = plt.subplots()
		ax.plot(t, x)
		
		ax.set(xlabel='tiempo (s)', ylabel='Amplitud', title='Ejemplo CSV')
		ax.grid()
		plt.ion()
		plt.show()
		
		x = np.random.randn(len(t))

		data = np.transpose([t,x])
		
		np.savetxt("foo.csv", data, delimiter=",")
		
		num = 0
	
