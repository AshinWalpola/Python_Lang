import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

#ADL Labor 02 - Exercise 05 Exchnages and Comparisons
#Authors: Ashin Walpola, Mithila Seneviratne

# Function to parse data from files
def parse_sort_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        current_run = {'N': [], 'Computation Time': [], 'Comparisons': [], 'Exchanges': []}
        for line in file:
            if line.startswith('Run'):
                if current_run['N']:
                    data.append(current_run)
                    current_run = {'N': [], 'Computation Time': [], 'Comparisons': [], 'Exchanges': []}
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
    'Shell Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Shell_Sort_testing.txt',
    '3WayRadixQuick Sort': '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/3WayRadixQuickSort_testing.txt'
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
    comparisons = np.array([pad_data(run['Comparisons'], max_points) for run in data])
    exchanges = np.array([pad_data(run['Exchanges'], max_points) for run in data])
    
    average_computation_time = np.nanmean(computation_times, axis=0)
    high_computation_time = np.nanmax(computation_times, axis=0)
    low_computation_time = np.nanmin(computation_times, axis=0)
    
    average_comparisons = np.nanmean(comparisons, axis=0)
    high_comparisons = np.nanmax(comparisons, axis=0)
    low_comparisons = np.nanmin(comparisons, axis=0)
    
    average_exchanges = np.nanmean(exchanges, axis=0)
    high_exchanges = np.nanmax(exchanges, axis=0)
    low_exchanges = np.nanmin(exchanges, axis=0)
    
    plot_data[name] = {
        'N': N,
        'Average Computation Time': average_computation_time,
        'High Computation Time': high_computation_time,
        'Low Computation Time': low_computation_time,
        'Average Comparisons': average_comparisons,
        'High Comparisons': high_comparisons,
        'Low Comparisons': low_comparisons,
        'Average Exchanges': average_exchanges,
        'High Exchanges': high_exchanges,
        'Low Exchanges': low_exchanges
    }

# Plot data for comparisons
plt.figure(figsize=(12, 8))
for name, data in plot_data.items():
    plt.plot(data['Average Computation Time'], data['Average Comparisons'], marker='o', label=f'{name} Average Comparisons')
    plt.fill_between(data['Average Computation Time'], data['Low Comparisons'], data['High Comparisons'], alpha=0.1, label=f'{name} Comparisons Min-Max Range')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Computation Time (ms)')
plt.ylabel('Number of Comparisons')
plt.title('Number of Comparisons by Computation Time for Various Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()

# Plot data for exchanges
plt.figure(figsize=(12, 8))
for name, data in plot_data.items():
    plt.plot(data['Average Computation Time'], data['Average Exchanges'], marker='o', label=f'{name} Average Exchanges')
    plt.fill_between(data['Average Computation Time'], data['Low Exchanges'], data['High Exchanges'], alpha=0.1, label=f'{name} Exchanges Min-Max Range')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Computation Time (ms)')
plt.ylabel('Number of Exchanges')
plt.title('Number of Exchanges by Computation Time for Various Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()