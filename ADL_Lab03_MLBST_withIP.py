import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_file_path = '/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab03/ADL_Lab03_testing.csv'
df = pd.read_csv(csv_file_path)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['Balance Constant C'], df['Reading Time (ms)'], marker='o', linestyle='-')
plt.yscale('log')
plt.title('Reading Time vs Balance Constant C')
plt.xlabel('Balance Constant C')
plt.ylabel('Reading Time (ms)')
plt.grid(True)
plt.show()