import pandas as pd
import matplotlib.pyplot as plt

# Data from the file
data = {
    "Tree Type": ["Median Lifting BST", "Redblack Tree", "Randomized BST"],
    "Reading Database (ms)": [6413, 10409, 14863],
    "Height": [49, 24, 35],
    "Weight": [13828655, 13828655, 13828655],
    "Average Distance": [27.85945, 21.786781, 22.642235]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Set up the plot
plt.figure(figsize=(14, 10))

# Plot Reading Database Time
plt.subplot(2, 2, 1)
plt.bar(df["Tree Type"], df["Reading Database (ms)"], color=['#648BBA', '#7BB274', '#EF934C'])
plt.title("Reading Database Time (ms)")
plt.xlabel("Tree Type")
plt.ylabel("Time (ms)")
plt.xticks(rotation=15)
plt.grid(True, linestyle='--', alpha=0.7)

# Plot Height of Tree
plt.subplot(2, 2, 2)
plt.bar(df["Tree Type"], df["Height"], color=['#648BBA', '#7BB274', '#EF934C'])
plt.title("Height of Tree")
plt.xlabel("Tree Type")
plt.ylabel("Height")
plt.xticks(rotation=15)
plt.grid(True, linestyle='--', alpha=0.7)

# Plot Average Distance
plt.subplot(2, 2, 3)
plt.bar(df["Tree Type"], df["Average Distance"], color=['#648BBA', '#7BB274', '#EF934C'])
plt.title("Average Distance")
plt.xlabel("Tree Type")
plt.ylabel("Average Distance")
plt.xticks(rotation=15)
plt.grid(True, linestyle='--', alpha=0.7)

# Hide the empty subplot
plt.subplot(2, 2, 4)
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()