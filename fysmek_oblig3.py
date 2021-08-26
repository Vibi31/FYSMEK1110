import matplotlib.pyplot as plt 
import numpy as np 
from numpy import sqrt, sign
k = 500
L0 = 0.5 
h = 0.3 
m = 5 #5kg
n = 1000 #steps
g = 9.82
nu = 0.05 #friksjons konstant
x = np.zeros(n)
ax = np.zeros(n)
v = np.zeros(n)
t = np.linspace(0,10,n)
Fx = np.zeros(n)
N = np.zeros(n)
x[0] = 0.65
K = np.zeros(n)

for i in range (n-1):
    N = k*h*(1-(L0/sqrt(x[i]**2 + h**2))) + m*g
    Fx[i] = -k*x[i]*(1 - (L0/sqrt(x[i]**2 + h**2)))
    Ff = nu*abs(N) #friksjons kraft
    Fnet = Fx[i] -(sign(v[i])*Ff)
    ax[i] = Fnet/m
    v[i+1] = v[i] + ax[i]*(t[i+1]-t[i])
    x[i+1] = x[i] + v[i+1]*(t[i+1]-t[i])
    K[i+1] = 0.5*m*v[i+1]**2


plt.plot(x,K)
plt.xlabel('posisjon')
plt.ylabel('Kinetisk energi')
plt.show()



