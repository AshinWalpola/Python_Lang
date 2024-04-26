import numpy as np
import matplotlib.pyplot as plt

#Simulation Data for Channel Length Modulation

# Given data
Vgs_values = np.linspace(1, 5, 5)  # UGS values
Vds_values = np.array([2, 4, 6, 8, 10])  # UDS values
Id_max = 2  # Maximum current (mA)

# Simulate output characteristics for each UGS and UDS
Id_Data = {}
for Vgs in Vgs_values:
    Id = Id_max * (1 - np.exp(-Vds_values / (Vgs + 1)))  # Exponential equation for ID = f(UDS)
    Id_Data[Vgs] = Id

# Plot MOSFET output characteristics for each Vgs value
plt.figure(figsize=(10, 7))
for Vgs in Vgs_values:
    plt.plot(Vds_values, Id_Data[Vgs], label=f'UGS = {Vgs} V')

# Calculate and plot channel length modulation point
VDS1_idx = 1  # Index corresponding to UDS = 4V
VDS2_idx = 3  # Index corresponding to UDS = 8V
VDS1 = Vds_values[VDS1_idx]
VDS2 = Vds_values[VDS2_idx]
ID1 = [Id_Data[Vgs][VDS1_idx] for Vgs in Vgs_values]
ID2 = [Id_Data[Vgs][VDS2_idx] for Vgs in Vgs_values]
ΔVDS = VDS2 - VDS1
ΔID = np.array(ID2) - np.array(ID1)
λ = ΔID / ΔVDS

plt.plot(VDS2, ID2[0], marker='o', markersize=10, color='red', label=f'CLM Point (λ = {λ[0]:.4f})')

plt.title('MOSFET Output Characteristics')
plt.xlabel('Drain-Source Voltage (UDS) (V)')
plt.ylabel('Drain Current (ID) (mA)')
plt.grid(True)
plt.legend()
plt.show()

print(f"The channel length modulation parameter (λ) is {λ[0]:.4f}.")