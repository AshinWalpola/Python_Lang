import re
import pandas as pd
import matplotlib.pyplot as plt

# Read data from the file
file_path = '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/Insertion_Sort_testing.txt'

with open(file_path, 'r') as file:
    data = file.read()

# Extract relevant details using regular expressions
pattern = re.compile(r'Computation time for N = (\d+), K = \d+: (\d+) milliseconds')

matches = pattern.findall(data)

# Convert matches to a DataFrame
df = pd.DataFrame(matches, columns=['Array Size (N)', 'Computation Time (ms)'])
df['Array Size (N)'] = df['Array Size (N)'].astype(int)
df['Computation Time (ms)'] = df['Computation Time (ms)'].astype(int)

# Group by Array Size and calculate high, low, and average computation times
stats = df.groupby('Array Size (N)')['Computation Time (ms)'].agg(['min', 'max', 'mean']).reset_index()
stats.columns = ['Array Size (N)', 'Min Time (ms)', 'Max Time (ms)', 'Avg Time (ms)']

# Plot Array Size vs Computation Time
plt.figure(figsize=(10, 6))
plt.plot(stats['Array Size (N)'], stats['Avg Time (ms)'], marker='o', label='Average Time')
plt.fill_between(stats['Array Size (N)'], stats['Min Time (ms)'], stats['Max Time (ms)'], color='b', alpha=0.1, label='Min-Max Range')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Array Size (N)')
plt.ylabel('Computation Time (ms)')
plt.title('Insertion Sort Computation Time by Array Size')
plt.legend()
plt.grid(True)
plt.show()

