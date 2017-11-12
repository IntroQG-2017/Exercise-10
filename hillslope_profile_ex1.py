#!/usr/bin/env python3
"""Calculates a steady-state profile of a diffusive hillslope.

Description:
    This script calculates a steady-state profile of a diffusive hillslope with
    rivers incising at the lateral margins of the hillslope.
    
    User-defined variables are listed at the top of the script
    
Usage:
    ./hillslope_profile_ex1.py
    
Author:
    XXX YYY - DD.MM.YYYY
"""

# Import NumPy and Matplotlib modules
import numpy as np
import matplotlib.pyplot as plt

#--- USER-DEFINED VARIABLES -----------------------------------------------#

L = 10.0        # Half-width (ridge to valley) of hillslope [m]
U = 0.2         # Hillslope uplift rate [mm/a]
kappa = 0.01    # Soil/sediment/rock diffusivity [m^2/a]

#--- END USER-DEFINED VARIABLES -------------------------------------------#

# Convert erosion rate from mm/a to m/a
U = U / 1000.0

# Define range for full width of hillslope
x = np.linspace(-L, L, 21)

# Define empty array to store elevation values (h)
h = np.zeros(len(x))

# Loop over all values of x and calculate hillslope elevation
for i in range(len(x)):
    # INSERT EQUATION HERE

# Plot results
plt.plot(x, h, 'k-')
plt.xlabel('Distance from divide [m]')
plt.ylabel('Elevation [m]')
plt.title('Predicted hillslope geometry: Diffusion model')

# Other calculated values go below


# Display plot
plt.show()
