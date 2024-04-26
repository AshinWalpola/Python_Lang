import numpy as np
import matplotlib.pyplot as plt

# Experimental Data
Ugs_values = np.array([0.5423, 0.6852, 0.7531, 0.8246, 0.8444])
Id_values = np.array([0.00046, 0.0917, 0.3448, 1.1783, 1.5973])

# Interpolate to find Ugs for ID = 0.4mA
Ugs_04mA = np.interp(0.4, Id_values, Ugs_values)

# Plot MOSFET Transfer Characteristics
plt.figure(figsize=(10, 7))
plt.plot(Ugs_values, Id_values, marker='o', linestyle='-', label='Vgs')

# Calculate transconductance parameter (gm) for the operating point ID = 0.4mA
d_Id_d_Ugs = np.diff(Id_values) / np.diff(Ugs_values)
Ugs_midpoints = (Ugs_values[:-1] + Ugs_values[1:]) / 2
gm_04mA = np.interp(Ugs_04mA, Ugs_midpoints, d_Id_d_Ugs)
plt.plot(Ugs_04mA, 0.4, marker='o', markersize=10, color='purple', label=f'gm @ ID = 0.4mA')

# Mark threshold voltage (Vth)
Vth = Ugs_values[np.argmax(Id_values)]
plt.axvline(x=Vth, color='red', linestyle='--', label=f'Threshold Voltage (Vth = {Vth:.4f} V)')

# Derive parameter K
coefficients = np.polyfit(Ugs_values - Vth, Id_values, 2)
K = 1 / (2 * coefficients[0])

# Plot derived parameter K on the graph
Id_fit = K * (Ugs_values - Vth)**2
plt.plot(Ugs_values, Id_fit, linestyle='--', color='green', label=f'ID Fit (K = {K:.6f} mA/V^2)')

# Customize the plot
plt.title('MOSFET Transfer Characteristics')
plt.xlabel('Gate-Source Voltage (Ugs) (V)')
plt.ylabel('Drain Current (Id) (mA)')
plt.grid(True)
plt.legend()

# Show plot
plt.show()
