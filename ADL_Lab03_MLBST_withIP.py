import matplotlib.pyplot as plt
import numpy as np

# Given data
C_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
times = [9792, 10464, 9776, 10159, 11252, 10978, 11675, 10666, 11098, 11388, 12332]


# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(C_values, times, marker='o', linestyle='-', color='Blue')
plt.yscale('log')
plt.xlabel('C Values')
plt.ylabel('Time (ms)')
plt.title('Time Taken to Read Database vs C Values')
plt.grid(True)
plt.show()
