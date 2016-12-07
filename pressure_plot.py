#!/usr/bin/env python
# Pressure distribution in a reservoir solving Darcy Equation by explicit finite difference method
# Unsteady state 
import numpy as np
from numpy import zeros
from numpy import array
from numpy import arange
from numpy import linspace
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Use these lines for input user data
'''
L = input ('Enter the lenght of the reservoir: ')
q = input ('Enter the number of grid blocks: ')
dt = input ('Enter the time step: ')
pj = input ('Enter the pressure at the first block: ')
pq = input ('Enter the pressure at the last block: ')
timestep = input ('Enter the number of time steps: ')
'''

#Defining data manually
L = 20.                 #length of the reservoir (m) 
q = 20                  #number of grid blocks
dt = 0.01               #timestep (s)
pj = 101.325            #pressure at first block (kPa)
pq = pj/10              #pressure at last block (kPa)
timestep = 50           #number of timesteps

#Calculate Dx and Dt/Dx
dx = L/q
alfa = dt/(dx**2)

#Create array
pressure = zeros([timestep,q])
print '\033[0;36mCreate array\n\033[0m', pressure

#Initialize array
pressure[0, 0] = pj
pressure[0, q - 1] = pq
print '\n\033[0;36mInitialize array\n\033[0m', pressure

#Set up boundary conditions
for i in range(1, timestep):
 pressure[i, 0] = pressure[0, 0]
 pressure[i, q - 1] = pressure[0, q - 1]
print '\n\033[0;36mSet up Boundary conditions\n\033[0m', pressure

#Set up initial conditions
for j in range(1, q - 1):
 pressure[0, j] = pressure[0, q - 1]
print '\n\033[0;36mSet up Initial conditions\n\033[0m', pressure

#Calculate pressure distribution
for i in range(1, timestep):
 for j in range(1, q - 1):
  pressure[i,j] = pressure[i-1,j] + (alfa*(pressure[i-1, j+1] + pressure[i-1, j-1] - 2*pressure[i-1, j]))
print '\n\033[0;36mFinal Pressure distribution\n\033[0m', pressure

#Create table of lengths
length = linspace(0, L, q)
print length

#Plots
for i in range(0, timestep):
 plt.plot(length,pressure[i,:])
 plt.xlabel('Length of reservoir (m)')
 plt.ylabel('Pressure (kPa)')
plt.annotate('time = t', xy=(1.7, 70), xytext=(2, 80),
            arrowprops=dict(facecolor='red', shrink=0.01),
            )
plt.annotate('time = 0', xy=(1.5, 10), xytext=(0.1, 0.5),
            arrowprops=dict(facecolor='blue', shrink=0.01),
            )
plt.title('Pressure distribution by finite differences')
plt.grid(True)
plt.show()

#3D Plots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#loop over timesteps
for i in range(0, timestep):
 ax.plot(length, pressure[i,:], i*dt*1000) 

#TEST FOR PLOT TYPES
 #ax.scatter(length, pressure[i,:], i)
 #ax.plot_wireframe(length, pressure[i,:], i*dt*1000, rstride=1, cstride=1)
 #surf ax.plot_surface(length, pressure, i, rstride=1, cstride=1, cmap=cm.coolwarm,
 #                       linewidth=0, antialiased=False)
 #ax.plot_trisurf(length, pressure, i, cmap=cm.jet, linewidth=0.2)
 #ax.zaxis.set_major_locator(LinearLocator(10))
 #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
 #fig.colorbar(surf, shrink=0.5, aspect=5) 

ax.set_xlabel('Length of reservoir (m)')
ax.set_ylabel('Pressure (kPa)')
ax.set_zlabel('time (s)')
plt.title('Pressure distribution over time by finite differences')
#ax.legend()
fig.savefig('test01.png')
plt.show()
