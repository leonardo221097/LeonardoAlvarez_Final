import numpy as np
import matplotlib.pyplot as plt
#para realizar este ejercicio me guie de la solucion del ejercicio 14 dada por el profesor para poder obtener la probabilidad de sigma

def proba(x_values, sigma):
    return (1/np.sqrt(2.0 * np.pi)*sigma)*np.exp(-0.5*(x_values/sigma)**2) 

def likelihood(x_values, sigma):
    like = (1.0/9.0)*sigma/sigma # esto asegura de tener like del mismo tipo que sigma
    for x in x_values:
        like = like * proba(x, sigma)
    return like



x_data = np.loadtxt('valores.txt')
n_points = 10**5
sigma = np.linspace(1,10,n_points)
l = likelihood(x_data, sigma)
plt.plot(sigma,l)
plt.hist(sigma)
plt.savefig('sigma.png')


