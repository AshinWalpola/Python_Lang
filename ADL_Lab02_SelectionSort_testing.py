import re
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Function to read and extract data from the text file
def extract_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    # Regular expression to find lines with computation time and N
    pattern = re.compile(r'Computation time for N = (\d+), K = \d+: (\d+) milliseconds')
    matches = pattern.findall(data)
    
    # Extract array sizes and computation times
    data_dict = defaultdict(list)
    for match in matches:
        array_size = int(match[0])
        comp_time = int(match[1])
        data_dict[array_size].append(comp_time)
    
    return data_dict

# Function to calculate statistics
def calculate_statistics(data_dict):
    array_sizes = sorted(data_dict.keys())
    means = []
    highs = []
    lows = []
    
    for size in array_sizes:
        times = data_dict[size]
        means.append(np.mean(times))
        highs.append(np.max(times))
        lows.append(np.min(times))
    
    return array_sizes, means, highs, lows

# Function to plot the data
def plot_data(array_sizes, means, highs, lows):
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, means, marker='o', label='Mean')
    plt.fill_between(array_sizes, lows, highs, color='b', alpha=0.1, label='High/Low Range')
    plt.title('Selection Sort Computation Time vs. Array Size')
    plt.xlabel('Array Size (N)')
    plt.ylabel('Computation Time (milliseconds)')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

# Main script
file_path = '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Selection_Sort_testing.txt'
data_dict = extract_data(file_path)
array_sizes, means, highs, lows = calculate_statistics(data_dict)
plot_data(array_sizes, means, highs, lows)
