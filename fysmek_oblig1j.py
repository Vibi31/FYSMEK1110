
#oppgave g:
import numpy as np
import matplotlib.pyplot as plt
from math import exp

N = 1001 #steps
x = np.zeros(N) #posisjon
v = np.zeros(N) #hastighet
a = np.zeros(N) #akselerasjon
F = np.zeros(N) #kraft
t = np.linspace(0,10,N) #tids array der dt = 0.01sekunder

x[0] = 0
t[0] = 0
a[0] = 400/80
fv = 25.8
tc = 0.67
#euler cromers metode:

for n in range (N-1):
    A = 0.45*(1-0.25*exp(-(t[n]/tc)**2)) 
    D = 0.5*1.293*1.2*A*(v[n]**2)
    F = 400 + 488*exp(-(t[n]/tc)**2) - fv*v[n] - D
    a[n+1] = F/80
    v[n+1] = v[n] + a[n]*(t[n+1]-t[n])
    x[n+1] = x[n] + v[n]*(t[n+1]-t[n])


print(x[931]) #printer 100.02....
#tiden for å oppnå 100m er rundt 9.3 sekunder

plt.plot(t,a)
plt.xlabel('tid(s)')
plt.ylabel('akselerasjon')
plt.show()

plt.plot(t,x)
plt.xlabel('tid(s)')
plt.ylabel('posisjon')
plt.show()

plt.plot(t,v)
plt.xlabel('tid(s)')
plt.ylabel('hastighet')
plt.show()

