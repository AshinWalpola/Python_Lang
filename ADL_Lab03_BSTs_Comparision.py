import matplotlib.pyplot as plt
import numpy as np

#Comparison of Insertion time for BST, Randomized BST, Red Black Tree and Median Lifting BST.

# Function to read and parse the data from the text files
def read_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(',')
            if len(parts) == 2:
                N_part, time_part = parts
                N = int(N_part.split(':')[1].strip())
                time = int(time_part.split(':')[1].strip().split()[0])
                if N not in data:
                    data[N] = []
                data[N].append(time)
    return data

# Read the data from the text files
bst_data = read_data('/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab03/ADL_Lab03_BST_testing.txt')
rbst_data = read_data('/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab03/ADL_Lab03_RandomizedBST_testing.txt')
RedBlackTree_data = read_data('/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab03/ADL_Lab03_RedBalckTree_testing.txt')
additional_data = read_data('/Users/ashinwalpola/Documents/University/HAW Hamburg/IE_3/AD-Dierks/Lab/Lab03/ADL_Lab03_MedianLiftingBST_testing.txt')

# Function to compute the average and standard deviation
def compute_stats(data):
    averages = {N: np.mean(times) for N, times in data.items()}
    std_devs = {N: np.std(times) for N, times in data.items()}
    return averages, std_devs

# Compute stats for each data set
bst_averages, bst_std_devs = compute_stats(bst_data)
rbst_averages, rbst_std_devs = compute_stats(rbst_data)
Red_averages, Red_std_devs = compute_stats(RedBlackTree_data)
mlbst_averages, mlbst_std_devs = compute_stats(additional_data)

# Plot the data with shaded ranges
plt.figure(figsize=(10, 6))

# Plot BST data
bst_N = list(bst_averages.keys())
bst_avg = list(bst_averages.values())
bst_std = list(bst_std_devs.values())
plt.plot(bst_N, bst_avg, 'o-', label='BST')
plt.fill_between(bst_N, np.array(bst_avg) - np.array(bst_std), np.array(bst_avg) + np.array(bst_std), alpha=0.2)

# Plot Randomized BST data
rbst_N = list(rbst_averages.keys())
rbst_avg = list(rbst_averages.values())
rbst_std = list(rbst_std_devs.values())
plt.plot(rbst_N, rbst_avg, 's-', label='Randomized BST')
plt.fill_between(rbst_N, np.array(rbst_avg) - np.array(rbst_std), np.array(rbst_avg) + np.array(rbst_std), alpha=0.2)

# Plot Red Black Tree Data
Red_N = list(Red_averages.keys())
Red_avg = list(Red_averages.values())
Red_std = list(Red_std_devs.values())
plt.plot(Red_N, Red_avg, '^-', label='RedBlackTree')
plt.fill_between(Red_N, np.array(Red_avg) - np.array(Red_std), np.array(Red_avg) + np.array(Red_std), alpha=0.2)

# Plot Median Lifting BST Data
mlbst_N = list(mlbst_averages.keys())
mlbst_avg = list(mlbst_averages.values())
mlbst_std = list(mlbst_std_devs.values())
plt.plot(mlbst_N, mlbst_avg, 'd-', label='Median Lifting BST')
plt.fill_between(mlbst_N, np.array(mlbst_avg) - np.array(mlbst_std), np.array(mlbst_avg) + np.array(mlbst_std), alpha=0.2)

# Enable grid lines for both major and minor ticks
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.xlabel('N (number of elements)')
plt.ylabel('Insertion time (milliseconds)')
plt.title('N vs Insertion Time for BST, Randomized BST, Red Black Tree, and Median Lifting BST')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')

plt.show()
