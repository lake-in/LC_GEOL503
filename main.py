# main.py

Chemical Weathering Feedback Box Model
GEOL 503 Final Project - Laikyn

Simulates a simple climate-carbon feedback system using
carbon reservoirs (rock & atmosphere) and global temperature.

import numpy as np
import matplotlib.pyplot as plt

# Constants (modifiable)
c1 = 0.01  # Rate of carbon release from rock to atmosphere
c2 = 0.005  # Rate of carbon burial from atmosphere to rock
c3 = 0.02  # Temperature sensitivity to atmospheric carbon

# Initial conditions
rock_0 = 1000  # Initial carbon in rock box (GtC or arbitrary units)
atmo_0 = 300   # Initial carbon in atmosphere box
T_0 = 15       # Initial global temperature (°C)

# Time settings
time_steps = 1000
time = np.arange(time_steps)

# Arrays to hold values
rock = np.zeros(time_steps)
atmo = np.zeros(time_steps)
T = np.zeros(time_steps)

# Set initial state
rock[0] = rock_0
atmo[0] = atmo_0
T[0] = T_0

# Main model loop
for i in range(1, time_steps):
    rock[i] = rock[i-1] - c1 * rock[i-1] + c2 * atmo[i-1]
    atmo[i] = atmo[i-1] + c1 * rock[i-1] - c2 * atmo[i-1]
    T[i] = T_0 + c3 * (atmo[i] - atmo_0)
  
# Plot results
plt.figure(figsize=(12, 6))
plt.plot(time, rock, label='Carbon in Rock (GtC)', color='brown')
plt.plot(time, atmo, label='Carbon in Atmosphere (GtC)', color='green')
plt.plot(time, T, label='Global Temperature (°C)', color='red')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.title('Chemical Weathering Feedback Model')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig('outputs/time_series_plot.png')
plt.show()
