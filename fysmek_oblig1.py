

import numpy as np
import matplotlib.pyplot as plt
m = 0.1             #mass in KG
L0 = 1              #equilibrium length of rope in metre
k = 200             #spring constatn in N/m
theta1 = 30*pi/180  #starting angle in radians
g = 9.82            #gravity 

N = 10001 #steps dt = 0.001s
r = np.zeros((N,2)) #posisjon
v = np.zeros((N,2)) #hastighet
t = np.linspace(0,7,N) #tids array der dt = 0.01sekunder
a = np.zeros((N,2) #akselerasjon

r[0] = L0*sin(theta1), -L0*cos(theta1)
ax[0] = -k*(r-L0)*r*sin(theta1)/m 
ay[0] = -g + k*(r-L0)*r*cos(theta1)/m
#euler cromers metode:
for n in range (N-1):
    r = abs(x[n])+abs(y[n])
    theta = arcsin(x[n]/r)
    ax[n+1] = -k*(r-L0)*r*sin(theta)/m 
    ay[n+1] = -g + k*(r-L0)*r*cos(theta)/m
    v[n+1] = v[n] + a[n]*(t[n+1]-t[n])
    x[n+1] = x[n] + v[n]*(t[n+1]-t[n])




