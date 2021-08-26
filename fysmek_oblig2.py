
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, cos, sin, sqrt
g = [0,9.81] 	# tyngdeakselerasjon
m = 0.1             #mass in KG
L0 = 1              #equilibrium length of rope in metre
k = 200             #spring constatn in N/m
 
theta1 = -60*pi/180
v0norm = 0
v0 = 0 

time = 10	# maximum tid vi ser på i sekunder
dt = 0.001	# tidssteg i sekunder
n = int(time/dt)

t = np.zeros(n)
r = np.zeros((n,2))
v = np.zeros((n,2))
a = np.zeros((n,2))

x0 = L0*cos(theta1)
y0 = L0*sin(theta1)
r[0] = [x0, y0] 
r0 = np.array([x0,y0])
v[0] = [0,0]	# Initialhastighet

for i in range(0, n-1):
    a[i] = -k*(np.linalg.norm(r[i])-L0)*(r[i]/np.linalg.norm(r[i]))/m -g
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + v[i+1]*dt
    t[i+1] = t[i] + dt 

fig, ax = plt.subplots(nrows=3, figsize=(6, 6))

ax[0].plot(r[:i, 0], r[:i, 1])
ax[0].set_xlabel("Posisjon x [m]")
ax[0].set_ylabel("Posisjon y [m]")

# Her plotter vi de to hastighetskomponentene for alle tider
ax[1].plot(t[:i], v[:i, 0])
ax[1].plot(t[:i], v[:i, 1])
ax[1].set_xlabel('Tid t [s]')
ax[1].set_ylabel('vx, vy [m/s]')
ax[1].legend(["vx", "vy"])

# Her plotter vi de to akselerasjonskomponentene for alle tider
ax[2].plot(t[:i], a[:i, 0])
ax[2].plot(t[:i], a[:i, 1])
ax[2].set_xlabel('Tid t [s]')
ax[2].set_ylabel('ax, ay [m/s^2]')
ax[2].legend(["ax", "ay"])

plt.show()




