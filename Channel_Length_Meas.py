import numpy as np
import matplotlib.pyplot as plt

# Experimental Data
Vgs_values = np.array([0.1, 0.2, 0.7, 0.7559, 0.8133, 0.8528])

# Drain Current for each Ugs
Id_Data = {
    0.1: np.array([0, 0, 0, 0, 0]),
    0.2: np.array([0.004, 0.0004, 0.0004, 0.0004, 0.0004]),
    0.7: np.array([0.1357, 0.1355, 0.1359, 0.1366, 0.1369]),
    0.7559: np.array([0.362, 0.363, 0.364, 0.368, 0.371]),
    0.8133: np.array([0.978, 0.979, 0.995, 0.968, 0.976]),
    0.8528: np.array([1.787, 1.824, 1.858, 1.879, 1.878])
}

# Calculate slope for each Vgs
slopes = []
Uds_values = np.linspace(0, 10, 5)
for Vgs in Vgs_values:
    Id = Id_Data[Vgs]
    slope = np.gradient(Id, Uds_values)
    slopes.append(slope)


# Plot slopes vs. Vgs
plt.figure(figsize=(10, 7))
for i, Vgs in enumerate(Vgs_values):
    plt.plot(Uds_values, slopes[i], marker='o', linestyle='-', label=f'Vgs = {Vgs} V')

# Find and plot channel-length modulation (CLM) point
max_slope_index = np.argmax(np.max(slopes, axis=1))
max_slope_Vgs = Vgs_values[max_slope_index]
max_slope_Uds = Uds_values[np.argmax(slopes[max_slope_index])]
plt.plot(max_slope_Uds, np.max(slopes[max_slope_index]), marker='o', markersize=10, color='red', label='CLM Point')

plt.title('Slope of MOSFET Output Characteristics (Channel Length Modulation)')
plt.xlabel('Drain-Source Voltage (Uds) (V)')
plt.ylabel('Slope (dId/dUds)')
plt.grid(True)
plt.legend()
plt.show() 