import matplotlib.pyplot as plt
import numpy as np

# Data for Insertion Sort
insertion_sort_n = np.array([1024000, 1024000, 1024000, 1024000, 1024000])
insertion_sort_time = np.array([1325008, 1384049, 1677450, 1378898, 1320596])
insertion_sort_time_sorted = np.sort(insertion_sort_time)
insertion_sort_time_mean = np.mean(insertion_sort_time_sorted)
insertion_sort_time_min = np.min(insertion_sort_time_sorted)
insertion_sort_time_max = np.max(insertion_sort_time_sorted)

# Data for Selection Sort
selection_sort_n = np.array([2048000, 2048000, 2048000, 2048000, 2048000])
selection_sort_time = np.array([790018, 777015, 769858, 798940, 768079])
selection_sort_time_sorted = np.sort(selection_sort_time)
selection_sort_time_mean = np.mean(selection_sort_time_sorted)
selection_sort_time_min = np.min(selection_sort_time_sorted)
selection_sort_time_max = np.max(selection_sort_time_sorted)

# Data for Shell Sort
shell_sort_n = np.array([16384000, 16384000, 16384000, 16384000, 16384000])
shell_sort_time = np.array([654862, 451946, 424869, 440227, 453259])
shell_sort_time_sorted = np.sort(shell_sort_time)
shell_sort_time_mean = np.mean(shell_sort_time_sorted)
shell_sort_time_min = np.min(shell_sort_time_sorted)
shell_sort_time_max = np.max(shell_sort_time_sorted)

# Data for Merge Sort
merge_sort_n = np.array([16384000, 16384000, 16384000, 16384000, 16384000])
merge_sort_time = np.array([454979, 472089, 427431, 465302, 491016])
merge_sort_time_sorted = np.sort(merge_sort_time)
merge_sort_time_mean = np.mean(merge_sort_time_sorted)
merge_sort_time_min = np.min(merge_sort_time_sorted)
merge_sort_time_max = np.max(merge_sort_time_sorted)

# Data for Bottom-Up Merge Sort
bottom_up_merge_n = np.array([16384000, 16384000, 16384000, 16384000, 16384000])
bottom_up_merge_time = np.array([408605, 452914, 457386, 418135, 414209])
bottom_up_merge_time_sorted = np.sort(bottom_up_merge_time)
bottom_up_merge_time_mean = np.mean(bottom_up_merge_time_sorted)
bottom_up_merge_time_min = np.min(bottom_up_merge_time_sorted)
bottom_up_merge_time_max = np.max(bottom_up_merge_time_sorted)

# Data for Quick Sort
quick_sort_n = np.array([16384000, 16384000, 16384000, 16384000, 16384000])
quick_sort_time = np.array([455048, 468414, 418919, 486223, 463750])
quick_sort_time_sorted = np.sort(quick_sort_time)
quick_sort_time_mean = np.mean(quick_sort_time_sorted)
quick_sort_time_min = np.min(quick_sort_time_sorted)
quick_sort_time_max = np.max(quick_sort_time_sorted)

# Plotting
plt.figure(figsize=(15, 8))

plt.errorbar(1024000, insertion_sort_time_mean, yerr=[[insertion_sort_time_mean - insertion_sort_time_min], [insertion_sort_time_max - insertion_sort_time_mean]], fmt='o', label='Insertion Sort')
plt.errorbar(2048000, selection_sort_time_mean, yerr=[[selection_sort_time_mean - selection_sort_time_min], [selection_sort_time_max - selection_sort_time_mean]], fmt='o', label='Selection Sort')
plt.errorbar(16384000, shell_sort_time_mean, yerr=[[shell_sort_time_mean - shell_sort_time_min], [shell_sort_time_max - shell_sort_time_mean]], fmt='o', label='Shell Sort')
plt.errorbar(16384000, merge_sort_time_mean, yerr=[[merge_sort_time_mean - merge_sort_time_min], [merge_sort_time_max - merge_sort_time_mean]], fmt='o', label ='Merge Sort')
plt.errorbar(16384000, bottom_up_merge_time_mean, yerr=[[bottom_up_merge_time_mean - bottom_up_merge_time_min], [bottom_up_merge_time_max - bottom_up_merge_time_mean]], fmt='o', label ='Bottom-Up Merge Sort')
plt.errorbar(16384000, quick_sort_time_mean, yerr=[[quick_sort_time_mean - quick_sort_time_min], [quick_sort_time_max - quick_sort_time_mean]], fmt='o', label ='Quick Sort')

# Set x and y axes to logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Add labels and legend
plt.xlabel('Size of Input (log scale)')
plt.ylabel('Time Taken (log scale)')
plt.title('Computation Time for Various Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
