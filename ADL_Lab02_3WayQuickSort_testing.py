import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab02/3WayRadixQuickSort_testing.txt'

# Read the content of the file into a pandas DataFrame
data = pd.read_csv(file_path, skiprows=1)

# Convert the relevant columns to appropriate data types
data['N'] = pd.to_numeric(data['N'], errors='coerce')
data['Time(ms)'] = pd.to_numeric(data['Time(ms)'], errors='coerce')

# Drop any rows with NaN values that could have resulted from conversion errors
data.dropna(subset=['N', 'Time(ms)'], inplace=True)

# Group by the number of strings and calculate the average, min, and max time
grouped_data = data.groupby('N')['Time(ms)'].agg(['mean', 'min', 'max']).reset_index()

# Plot the average time with shaded area indicating the range using logarithmic scales
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['N'], grouped_data['mean'], marker='o', linestyle='-', label='Average Time')
plt.fill_between(grouped_data['N'], grouped_data['min'], grouped_data['max'], color='b', alpha=0.2, label='Min-Max Range')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Strings (N)')
plt.ylabel('Time (ms)')
plt.title('Performance of ThreeWayRadixQuickSort Algorithm of Number of Strings (N) vs. Time (ms)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
