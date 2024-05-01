import matplotlib.pyplot as plt

#Authors: Mithila Seneviratne, Ashin Walpola

# Data for each sorting algorithm
sorting_algorithms = {
    'Insertion Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [3, 490, 299, 711, 1424, 2253],
        'Exchanges': [252949, 224392413, 754909460, 1802579865, -702138542, 1341175413],
        'Comparisons': [251950, 224362414, 754854461, 1802494866, -702258541, 1341025414]
    },
    'Selection Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [4, 239, 864, 2059, 4104, 6427],
        'Exchanges': [999, 29999, 54999, 84999, 119999, 149999],
        'Comparisons': [499500, 449985000, 1512472500, -682509796, -1389994592, -1634976888]
    },
    'Shell Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [3, 6, 7, 12, 17, 20],
        'Exchanges': [15881, 969423, 1965912, 3743632, 5202337, 6515174],
        'Comparisons': [7875, 579416, 1195903, 2468627, 3402330, 4115166]
    },
    'Merge Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [3, 5, 5, 9, 13, 15],
        'Exchanges': [999, 29999, 54999, 84999, 119999, 149999],
        'Comparisons': [8715, 408590, 797514, 1286346, 1874224, 2392613]
    },
    'Bottom Up Merge Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [2, 6, 16, 9, 14, 16],
        'Exchanges': [1001, 30004, 55004, 85009, 120004, 150006],
        'Comparisons': [8724, 410459, 802739, 1311876, 1881257, 2466419]
    },
    'Quick Sort': {
        'N': [1000, 30000, 55000, 85000, 120000, 150000],
        'Time': [1, 4, 7, 6, 9, 11],
        'Exchanges': [5964, 312794, 548333, 943488, 1332567, 1629808],
        'Comparisons': [11371, 525772, 1025259, 1770925, 2437236, 3050544]
    }
}

# Plotting
fig, axes = plt.subplots(3, 1, figsize=(10, 10))

for algorithm, data in sorting_algorithms.items():
    axes[0].plot(data['N'], data['Time'], label=algorithm)
    axes[1].plot(data['N'], data['Exchanges'], label=algorithm)
    axes[2].plot(data['N'], data['Comparisons'], label=algorithm)

axes[0].set_title('Computation Time Comparison')
axes[0].set_xlabel('Input Size (N)')
axes[0].set_ylabel('Computation Time (milliseconds)')
axes[0].legend()
axes[0].grid(True)

axes[1].set_title('Exchanges Comparison')
axes[1].set_xlabel('Input Size (N)')
axes[1].set_ylabel('Number of Exchanges')
axes[1].legend()
axes[1].grid(True)

axes[2].set_title('Comparisons Comparison')
axes[2].set_xlabel('Input Size (N)')
axes[2].set_ylabel('Number of Comparisons')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()
