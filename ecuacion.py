import numpy as np
import matplotlib.pyplot as plt



datos = np.loadtxt("ecuacion.dat")

#para realizar las otras dos graficas me guié de la solucion del ejercicio 29 dada por el profesor.
plt.subplot(2,3,2)
numx=200
numt=50

t=np.linspace(0,1,numt)
x1=datos[:,numx//4]
plt.plot(t,x1)
plt.savefig("ecuacion.png")

