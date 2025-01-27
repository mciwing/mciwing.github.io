# import packages
import numpy as np
import matplotlib.pyplot as plt

# Definition of variables
phi_min = 0                # definition of starting angle in degrees
phi_max = 360              # definition of final angle in degrees
n = 100                    # number of points

# Calculations and data generation with numpy
# Gererate time-vector
t = np.linspace(np.radians(phi_min), np.radians(phi_max), n, endpoint=True)  
y = np.sin(t)  

# Visualization with matplotlib
plt.rcParams['text.usetex'] = False    # if True use LATEX font type

plt.figure()
plt.plot(t, y, 'k')

# Labels for the x- and y-axis
plt.xlabel(r'Angle $\theta$ in degrees', fontsize=12) 
plt.ylabel(r'Sine($\theta$)', fontsize=12)

# Change axes
startx, endx = np.radians(phi_min), np.radians(phi_max)
starty, endy = -1.1, 1.1
plt.axis([startx, endx, starty, endy])

# Add grid
plt.grid()

# Change scale of axes
ax = plt.gca()
axis_x = np.array([0, 90, 180, 270, 360])
axis_x = np.radians(axis_x)
plt.xticks(axis_x, [360, 450, 540, 630, 720])

# Add legend
ax.legend([r"Sine($\theta$)"], loc="lower left", fontsize=13) 

# Add title
plt.title(r"$sin(\theta) = cos(\theta - 90^\circ)$", fontsize=24)

# Add text using x- and y-coordinates
plt.text(3.5, 0.35, r'$1^\circ=\frac{2\pi}{360}~rad$', fontsize=13)

# Show graph
plt.show()