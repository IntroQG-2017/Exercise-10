#!/usr/bin/env python3
"""Calculates a steady-state profile of a diffusive hillslope.

Description:
    This script calculates a steady-state profile of a diffusive hillslope
    with rivers incising at the lateral margins of the hillslope. It also
    loads a topographic profile for comparison with the model predictions.
    
    User-defined variables are listed at the top of the script
    
Usage:
    ./hillslope_profile_ex2.2.py
    
Author:
    FIRSTNAME LASTNAME - DD.MM.YYYY
"""

# Import NumPy and Matplotlib modules
import numpy as np
import matplotlib.pyplot as plt

#--- USER-DEFINED VARIABLES BELOW -----------------------------------------#

L = 10000      # Half-width (ridge to valley) of hillslope [m]
U = 0.5        # Hillslope uplift rate [mm/a]
kappa = 10.0   # Soil/sediment/rock diffusivity [m^2/a]

#--- END USER-DEFINED VARIABLES -------------------------------------------#

# Convert erosion rate from mm/a to m/a
U = U / 1000.0

# Read data file
data = np.loadtxt()

# Separate data file into different variables
data_x = 
data_h = 

# Define full width of hillslope
x = np.linspace()

# Define empty array to store hillslope elevations (h)
h = np.zeros(len(x))

# Loop over all x-values and calculate hillslope elevation
for
    h[i] = (U/(2.0*kappa)) * (L**2.0 - x[i]**2.0)

# Increase elevation of calculated profile to match observed river elevations


# Plot results
plt.plot(x,h,'k-')
plt.xlabel('Distance from divide [m]')
plt.ylabel('Elevation [m]')
plt.title('Predicted hillslope geometry: Diffusion model')

# Other calculated values go below here


# Display plot
plt.show()
