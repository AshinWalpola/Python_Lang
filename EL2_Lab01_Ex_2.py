import numpy as np
import matplotlib.pyplot as plt

#IE3_EL2_Labor01_Exercise_02
#Author: Ashin Walpola

# Experimental Data
Ugs_values = np.array([0.5423, 0.6852, 0.7531, 0.8246, 0.8444])
Id_values = np.array([0.00046, 0.0917, 0.3448, 1.1783,1.5973])

plt.plot(Ugs_values, Id_values, marker='o', linestyle='-', label=f'Vgs')

# Customize the plot
plt.title('MOSFET Transfer Characteristics')
plt.xlabel('Gate-Source Voltage (Ugs) (V)')
plt.ylabel('Drain Current (Id) (mA)')
plt.grid(True)
plt.legend()

# Show plot
plt.show()