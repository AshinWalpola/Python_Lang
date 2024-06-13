import re
import matplotlib.pyplot as plt

# Initialize lists to store extracted data
K_values = []
computation_times = []
comparisons = []
exchanges = []

# Read the data file
with open('/Users/ashinwalpola/Documents/XCode/IE3/ADL_Lab/ADL_Lab01/ADL_Lab 01 Exercise 4b Results.txt', 'r') as file:
    lines = file.readlines()

# Extract data from each line
for line in lines:
    match = re.match(r"Computation time for N = \d+, K = (\d+): (\d+) milliseconds", line)
    if match:
        K_values.append(int(match.group(1)))
        computation_times.append(int(match.group(2)))

    match = re.match(r"Comparisons: (\d+)", line)
    if match:
        comparisons.append(int(match.group(1)))

    match = re.match(r"Exchanges: (\d+)", line)
    if match:
        exchanges.append(int(match.group(1)))

# Plot the graph for computation time
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(K_values, computation_times, marker='o', label='Computation Time')
plt.title('Analysis of Sorting Algorithm')
plt.xlabel('K')
plt.ylabel('Computation Time (milliseconds)')
plt.grid(True)
plt.legend()

# Plot the graph for comparisons and exchanges
plt.subplot(2, 1, 2)
plt.plot(K_values, comparisons, marker='o', label='Comparisons')
plt.plot(K_values, exchanges, marker='o', label='Exchanges')
plt.xlabel('K')
plt.ylabel('Count')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
