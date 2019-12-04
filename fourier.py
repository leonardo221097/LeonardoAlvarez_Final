import numpy as np 
import matplotlib.pylab as plt


datos=np.loadtxt('sol.dat')

an=datos[:,0]
an1=an[3481::]
mes=datos[:,1]
mes1=mes[3481::]
dia=datos[:,2]
dia1=dia[3481::]
num=datos[:,3]
num1=num[3481::]

plt.plot(an1,num1)


T=[]
for i in range (len(an1)):
    s=an1[i]* num1[i]  
    T.append(s)

plt.savefig('solar.png')


