import matplotlib.pyplot as plt 
import numpy as np 
from numpy import sqrt

U0 = 150
m = 23  #23 kg
x0 = 2
alpha = 39.48
N = 100

t = np.linspace(0,10,N)
x = np.linspace(0,x0,N)
a = np.zeros(N)
v = np.zeros(N)
#x[0] = x0  #oppgave h
x[0] = -5 #oppgave h
#v[0] = sqrt(4*U0/m) #initial hastighet v0 oppgave h
v[0] = 10 #initial hastighet v0 oppgave i

for i in range (N-1):
    if abs(x[i]) < x0:
        a[i] = ((-U0*x[i])/(abs(x[i])*x0))/m + (-alpha*v[i])/m
    v[i+1] = v[i] + a[i]*(t[i+1]-t[i])
    x[i+1] = x[i] + v[i+1]*(t[i+1]-t[i])

plt.plot(t,x)
plt.xlabel('tid')
plt.ylabel('posisjon x')
plt.show()
