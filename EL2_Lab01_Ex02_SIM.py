import numpy as np
import matplotlib.pyplot as plt

# Experimental Data
Vgs_values = np.linspace(0.1, 0.9, 9)  # UGS values
Id_max = 2  # Maximum current (mA)
UDS = 5  # Constant voltage (V)

# Simulate transfer characteristics for each UGS
plt.figure(figsize=(10, 7))
for Vgs in Vgs_values:
    Id = Id_max * (1 - np.exp(-Vgs / (Vgs + 1)))  # Exponential equation for ID = f(UGS)
    plt.plot(Vgs, Id, marker='o', linestyle='-', label=f'UGS = {Vgs:.2f} V')

# Mark threshold voltage (UGS(th))
Vgs_th = 0.7  # Threshold voltage for the BS108 MOSFET
plt.axvline(x=Vgs_th, color='r', linestyle='--', label=f'Threshold Voltage (UGS(th) = {Vgs_th} V)')

# Calculate and mark transconductance parameter (β) for the operating point ID = 0.4mA
ID_operating = 0.4  # Operating current in mA
Vgs_operating = 0.7  # Threshold voltage in V
gm_operating = np.interp(Vgs_operating, Vgs_values, Id_max * (1 - np.exp(-Vgs_values / (Vgs_values + 1))))
β = gm_operating / (Vgs_operating - Vgs_th)
plt.plot(Vgs_operating, ID_operating, marker='o', color='g', markersize=10, label=f'β @ ID=0.4mA (β = {β:.4f} A/V)')

plt.title('MOSFET Transfer Characteristics')
plt.xlabel('Gate-Source Voltage (UGS) (V)')
plt.ylabel('Drain Current (ID) (mA)')
plt.grid(True)
plt.legend()
plt.show()

# Analyze measurement results to find parameter k
K = np.max(Id_max * (1 - np.exp(-Vgs_values / (Vgs_values + 1))) / (Vgs_values - Vgs_th)**2)
print(f"The parameter k for the approximation is {K:.4f}.")