#Student: Brean Prefontaine
#E/M Spring 2018 homework assignment #1
#Disclaimer: I did borrow the general structure of this code from the following source however I have modified it and added my own needs into the code: https://scipython.com/blog/visualizing-a-vector-field-with-matplotlib/
#modifciations include commenting the code more, taking out the color mapping feature so that only black field lines are visible, and creating three subplots for each different charge distribution that was needed for the homework. 

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle #to actually draw the charges


#creating a function that calculates the x and y component of the vector of the Electric Field
def E(q, r0, x, y):
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

# Grid of x, y points that we will be using in this plot
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

#create plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
fig.suptitle('Various Electric Fields')

#this is where we define the number of charges that will be in our plot; if more than 1 charge, the charges will be alternating between postively anf negatively charged particles

#############################################################
##sorry the code got so long...  I know I could have put this in one big loop and made the number of charges an array or list of some sort but I forgot how to do this so it just got really long...



#negative charge
nq = 1 #number of charges
charges = []

q = - 1
charges.append((q, (np.cos(2*np.pi/nq), np.sin(2*np.pi/nq)))) #this is equally spacing the charges on a unit circle just to have a really nice looking plot

# Electric field vector, E=(Ex, Ey), as separate components
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey

# Add filled circles for the charges themselves using 
charge_colors = {True: 'red', False: 'blue'} 
for q, pos in charges:
    ax1.add_artist(Circle(pos, 0.1, color=charge_colors[q>0]))


ax1.streamplot(x, y, Ex, Ey, color='black', linewidth=1, density=2)
ax1.set_title('Negative point charge', size = 10)



#postive charge
charges_pos = []

q = 1
charges_pos.append((q, (np.cos(2*np.pi/nq), np.sin(2*np.pi/nq)))) 

Ex_pos, Ey_pos = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges_pos:
    ex_pos, ey_pos = E(*charge, x=X, y=Y)
    Ex_pos += ex_pos
    Ey_pos += ey_pos


for q, pos in charges_pos:
    ax2.add_artist(Circle(pos, 0.1, color=charge_colors[q>0]))


ax2.streamplot(x, y, Ex_pos, Ey_pos, color='black', linewidth=1, density=2)
ax2.set_title('Positive point charge', size = 10)



#Dipole
nq = 2
charges_di = []
for i in range(nq):
    q = i%2 * 2 - 1
    charges_di.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))


Ex_di, Ey_di = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges_di:
    ex_di, ey_di = E(*charge, x=X, y=Y)
    Ex_di += ex_di
    Ey_di += ey_di

for q, pos in charges_di:
    ax3.add_artist(Circle(pos, 0.1, color=charge_colors[q>0]))


ax3.streamplot(x, y, Ex_di, Ey_di, color='black', linewidth=1, density=2)
ax3.set_title('Dipole', size = 10)



#quadropole
nq = 4
charges_quad = []
for i in range(nq):
    q = i%2 * 2 - 1
    charges_quad.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

Ex_quad, Ey_quad = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges_quad:
    ex_quad, ey_quad = E(*charge, x=X, y=Y)
    Ex_quad += ex_quad
    Ey_quad += ey_quad

for q, pos in charges_quad:
    ax4.add_artist(Circle(pos, 0.1, color=charge_colors[q>0]))


ax4.streamplot(x, y, Ex_quad, Ey_quad, color='black', linewidth=1, density=2)
ax4.set_title('Quadropole', size = 10)
######################################################################

plt.show()
