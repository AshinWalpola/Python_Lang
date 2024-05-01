import matplotlib.pyplot as plt

# Data for each sorting algorithm
sorting_algorithms = {
    "Insertion Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [2, 185, 154, 379, 763, 1211]
    },
    "Selection Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [2, 168, 546, 1295, 2585, 4031]
    },
    "Shell Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [2, 6, 7, 11, 15, 20]
    },
    "Merge Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [1, 5, 25, 17, 15, 16]
    },
    "Bottom UpMerge Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [1, 6, 13, 8, 14, 16]
    },
    "Quick Sort": {
        "N": [1000, 30000, 55000, 85000, 120000, 150000],
        "Time": [2, 1, 1, 1, 2, 2]
    }
}

# Plotting
plt.figure(figsize=(10, 6))

for algo, data in sorting_algorithms.items():
    plt.plot(data["N"], data["Time"], marker='o', label=algo)


plt.yscale('log')
plt.title("Sorting Algorithm Comparison")
plt.xlabel("Input Size (N)")
plt.ylabel("Computation Time (milliseconds) Log Scale")
plt.legend()
plt.grid(True)
plt.show()
