import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
file_path = '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/UnshuffledQuick_Sort_testing.txt'

data = []

with open(file_path, 'r') as file:
    current_run = {
        'N': [],
        'Computation Time': [],
        'Comparisons': [],
        'Exchanges': []
    }
    for line in file:
        if line.startswith('Run'):
            if current_run['N']:
                data.append(current_run)
                current_run = {key: [] for key in current_run}
        elif line.startswith('Computation time for N'):
            parts = line.split(',')
            N_part = parts[0].split('=')[1].strip()
            time_part = parts[1].split(':')[1].strip().split()[0]
            
            current_run['N'].append(int(N_part))
            current_run['Computation Time'].append(float(time_part))
        elif line.startswith('Number of comparisons'):
            comparisons = int(line.split(':')[1].strip())
            current_run['Comparisons'].append(comparisons)
        elif line.startswith('Number of exchanges'):
            exchanges = int(line.split(':')[1].strip())
            current_run['Exchanges'].append(exchanges)
    if current_run['N']:
        data.append(current_run)

# Determine the maximum number of data points in any run
max_points = max(len(run['N']) for run in data)

# Function to pad data with NaN to ensure equal length arrays
def pad_data(run_data, length):
    padded = np.full(length, np.nan)
    padded[:len(run_data)] = run_data
    return padded

# Prepare arrays for the statistics
N = pad_data(data[0]['N'], max_points)
computation_times = np.array([pad_data(run['Computation Time'], max_points) for run in data])
comparisons = np.array([pad_data(run['Comparisons'], max_points) for run in data])
exchanges = np.array([pad_data(run['Exchanges'], max_points) for run in data])

# Calculate average, high, and low values ignoring NaNs
average_computation_time = np.nanmean(computation_times, axis=0)
high_computation_time = np.nanmax(computation_times, axis=0)
low_computation_time = np.nanmin(computation_times, axis=0)

average_comparisons = np.nanmean(comparisons, axis=0)
high_comparisons = np.nanmax(comparisons, axis=0)
low_comparisons = np.nanmin(comparisons, axis=0)

average_exchanges = np.nanmean(exchanges, axis=0)
high_exchanges = np.nanmax(exchanges, axis=0)
low_exchanges = np.nanmin(exchanges, axis=0)

# Plot Number array (N) vs. Computation time with shaded area for deviation
plt.figure()
plt.plot(N, average_computation_time, marker='o', label='Average Computation Time')
plt.fill_between(N, low_computation_time, high_computation_time, alpha=0.2, label='Deviation')
plt.xlabel('Array Size (N)')
plt.ylabel('Computation Time (milliseconds)')
plt.title('Unshuffled Quick Sort Computation Time vs. Array Size')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

# Plot Comparisons and Exchanges with time with shaded area for deviation
plt.figure()
plt.plot(average_computation_time, average_comparisons, marker='o', label='Average Comparisons')
plt.fill_between(average_computation_time, low_comparisons, high_comparisons, alpha=0.2, label='Comparisons Deviation')
plt.plot(average_computation_time, average_exchanges, marker='^', label='Average Exchanges')
plt.fill_between(average_computation_time, low_exchanges, high_exchanges, alpha=0.2, label='Exchanges Deviation')
plt.xlabel('Computation Time (milliseconds)')
plt.ylabel('Count')
plt.title('Comparisons and Exchanges with Time')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()
