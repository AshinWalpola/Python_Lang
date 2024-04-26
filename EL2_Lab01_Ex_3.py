import numpy as np
import matplotlib.pyplot as plt

#IE3_EL2_Labor01_Exercise_03
#Author: Ashin Walpola

# Experimental Data
Vgs_values = np.array([0.1, 0.2, 0.7, 0.7559, 0.8133, 0.8528])

# Drain Current for each Vgs
Id_Data = {
    0.1: np.array([0, 0, 0, 0, 0]),
    0.2: np.array([0.004, 0.0004, 0.0004, 0.0004, 0.0004]),
    0.7: np.array([0.1357, 0.1355, 0.1359, 0.1366, 0.1369]),
    0.7559: np.array([0.362, 0.363, 0.364, 0.368, 0.371]),
    0.8133: np.array([0.978, 0.979, 0.995, 0.968, 0.976]),
    0.8528: np.array([1.787, 1.824, 1.858, 1.879, 1.878])
}

# Plot MOSFET output characteristics for each Vgs value
plt.figure(figsize=(10, 7))

# Uds values
Uds_values = np.linspace(-0.1, 0.1, 5)  # Voltage range

for Vgs in Vgs_values:
    Id = Id_Data[Vgs]
    plt.plot(Uds_values, Id, marker='o', linestyle='-', label=f'Vgs = {Vgs} V')

# Customize the plot
plt.title('MOSFET Output Characteristics (Ohmic Region)')
plt.xlabel('Drain-Source Voltage (Uds) (V)')
plt.ylabel('Drain Current (Id) (mA)')
plt.ylim(-0.3, 0.3)  # Current range
plt.grid(True)
plt.legend()

# Show plot
plt.show()
