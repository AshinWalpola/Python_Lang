import numpy as np
import matplotlib.pyplot as plt

# Read data from the text file
with open('/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Exercise 5 Prep.txt', 'r') as file:
    lines = file.readlines()

# Initialize dictionaries to store computation times for each array size
times = {}
array_size = None

# Parse data and store computation times
for line in lines:
    if line.startswith("Run"):
        run_num = int(line.split(":")[0].strip("Run "))
        times[run_num] = {}
    elif line.startswith("Sorted Array"):
        array_size = int(line.split(":")[1].strip().split()[0])
        times[run_num][array_size] = []
    elif line.startswith("Time taken"):
        time_taken = float(line.split(":")[1].strip().split()[0])
        times[run_num][array_size].append(time_taken)

# Calculate high, low, and average times for each array size
highs = []
lows = []
averages = []
array_sizes = sorted(times[1].keys())  # Get array sizes from any run
for size in array_sizes:
    run_times = [times[run][size] for run in times.keys()]
    high = np.max(run_times)
    low = np.min(run_times)
    average = np.mean(run_times)
    highs.append(high)
    lows.append(low)
    averages.append(average)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, highs, label='High')
plt.plot(array_sizes, lows, label='Low')
plt.plot(array_sizes, averages, label='Average')
plt.xlabel('Array Size')
plt.ylabel('Time taken (milliseconds)')
plt.title('Computation Times of Unshuffled Quick Sort')
plt.legend()
plt.grid(True)
plt.xscale('log')  # Set logarithmic scale for x-axis
plt.yscale('log')  # Set logarithmic scale for y-axis
plt.show()
