import numpy as np
import matplotlib.pyplot as plt

#IE3_EL2_Labor01_Exercise_02
#Author: Ashin Walpola

# Experimental Data
Ugs_values = np.array([0.5423, 0.6852, 0.7531, 0.8246, 0.8444])
Id_values = np.array([0.00046, 0.0917, 0.3448, 1.1783,1.5973])

# Q-point current
Q_point_Id = 0.4  # mA


plt.plot(Ugs_values, Id_values, marker='o', linestyle='-', label=f'Vgs')
# Find the index i such that Id_values[i] < Q_point_Id < Id_values[i+1]
for i in range(len(Id_values) - 1):
    if Id_values[i] <= Q_point_Id <= Id_values[i + 1]:
        # Linear interpolation between two points (i and i+1)
        Q_point_Ugs = Ugs_values[i] + ((Q_point_Id - Id_values[i]) / (Id_values[i + 1] - Id_values[i])) * (Ugs_values[i + 1] - Ugs_values[i])
        break

print("Gate-Source Voltage at Q-point (Ugs):", Q_point_Ugs)

# Slope around the Q-point (approximated as a nearby point)
delta_Id = Id_values[i + 1] - Id_values[i]
delta_Ugs = Ugs_values[i + 1] - Ugs_values[i]

# Calculate beta (transconductance parameter)
beta = delta_Id / delta_Ugs
print("Transconductance parameter (beta):", beta)

# Customize the plot
plt.title('MOSFET Transfer Characteristics')
plt.xlabel('Gate-Source Voltage (Ugs) (V)')
plt.ylabel('Drain Current (Id) (mA)')
plt.grid(True)
plt.legend()

# Show plot
plt.show()