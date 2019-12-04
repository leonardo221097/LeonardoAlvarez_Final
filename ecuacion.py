import numpy as np 
import matplotlib.pylab as plt



datos=np.loadtxt('ecuacion.dat')

x=datos[:,0]
y=datos[:,1]


plt.plot(x,y)
plt.savefig('resultado.png')
