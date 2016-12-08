#!/usr/bin/env python
#A script to calculate pressure heads by explicit finite differences using Gauss-Siedel iteration
#Dirichlet conditions are applied (heads  

from math import sin, radians
import numpy as np
from numpy import array
from numpy import linspace
from numpy import ones
import matplotlib.pyplot as plt

#Defining constants for water-rock matrix  

mu_f = 0.89e-3    #viscosity of freshwater at 293K (Pa*s = kg/m*s)
ro_f = 998.2      #density of freshwater (kg/m3)
g = 9.806         #gravity acceleration (m/s2)
k1 = 1e-16        #intrinsic permeability layer 1 (m2)

#Create a 10x10 grid with x,y coordinates and set initial conditions t = 0
#P = ones([10,10])
#P = P*5
#P[4:6,4:6] = 0

#Create a 100x100 grid with x,y coordinates and set initial conditions t = 0
P = ones([100,100])
P = P*5
P[45:54,45:54] = 0.

print 'Initial conditions, pressure heads (m) \n', P

#Specify boundary conditions
grid = P.shape
nrow = grid[0]
ncol = grid[1]
print grid
print 'Grid is a ', nrow, ' by ', ncol, ' matrix.'

#Performing Gauss-Siedel iteration
ni = 1 
conv_crit = 1e-3
converged = False
while (not converged):
 max_err = 0 
 for i in range(1, nrow - 1): 
  for j in range(1, ncol - 1): 
   P_old = P[i, j]
   P[i, j] = (P[i - 1, j] + P[i + 1, j] + P[i, j - 1] + P[i, j + 1]) / 4.

#Compare obtained head values to those at previous iteration
   diff = P[i, j] - P_old
   if (diff > max_err):
    max_err = diff

#Continue to iterate as long as head values continue to change within some preset limit
 if (max_err < conv_crit):
  converged = True
 ni = ni + 1 
print 'number of iterations = ', ni - 1  #Iteration level
print 'Pressure heads at hydrostatic equilibrium, h (m) =\n', P


'''
#plot
plt.subplot(1,1,1)
plt.plot(length_plot,QF1)
plt.plot(length_plot,QF2)
plt.plot(length_plot,QF3)
plt.xlabel('Length of reservoir (m)')
plt.ylabel('Flux (m/day)') 
plt.show()
'''
