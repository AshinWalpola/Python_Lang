import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

#ADL Labor 02 - Exercise 05 - Comparisons
#Authors: Ashin Walpola, Mithila Seneviratne

# Function to parse data from files
def parse_sort_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        current_run = {'N': [], 'Computation Time': []}
        for line in file:
            if line.startswith('Run'):
                if current_run['N']:
                    data.append(current_run)
                    current_run = {'N': [], 'Computation Time': []}
            elif line.startswith('Computation time for N'):
                parts = line.split(',')
                N_part = parts[0].split('=')[1].strip()
                time_part = parts[1].split(':')[1].strip().split()[0]
                current_run['N'].append(int(N_part))
                current_run['Computation Time'].append(float(time_part))
        if current_run['N']:
            data.append(current_run)
    return data

# Function to pad data with NaN to ensure equal length arrays
def pad_data(run_data, length):
    padded = np.full(length, np.nan)
    padded[:len(run_data)] = run_data
    return padded

# Paths to the data files for each algorithm
file_paths = {
    'Quick Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Quick_Sort_testing.txt',
    'Insertion Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Insertion_Sort_testing.txt',
    'Merge Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Merge_Sort_testing.txt',
    'Bottom-Up Merge Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/BottomUpMerge_Sort_testing.txt',
    'Unshuffled Quick Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/UnshuffledQuick_Sort_testing.txt',
    'Selection Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Selection_Sort_testing.txt',
    'Shell Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Shell_Sort_testing.txt'
}

# Parse the data for each sorting algorithm
sort_data = {name: parse_sort_data(path) for name, path in file_paths.items()}

# Determine the maximum number of data points in any run
max_points = max(max(len(run['N']) for run in data) for data in sort_data.values())

# Prepare data for plotting
plot_data = {}
for name, data in sort_data.items():
    N = pad_data(data[0]['N'], max_points)
    computation_times = np.array([pad_data(run['Computation Time'], max_points) for run in data])
    average_computation_time = np.nanmean(computation_times, axis=0)
    high_computation_time = np.nanmax(computation_times, axis=0)
    low_computation_time = np.nanmin(computation_times, axis=0)
    plot_data[name] = (N, average_computation_time, low_computation_time, high_computation_time)

# Plot data
plt.figure(figsize=(12, 8))
for name, (N, avg, low, high) in plot_data.items():
    plt.plot(N, avg, marker='o', label=f'{name} Average Time')
    plt.fill_between(N, low, high, alpha=0.1, label=f'{name} Min-Max Range')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Array Size (N)')
plt.ylabel('Computation Time (ms)')
plt.title('Computation Time by Array Size for Various Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()