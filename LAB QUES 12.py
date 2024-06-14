import numpy as np

recovery_times = [5, 7, 8, 10, 12, 13, 15, 16, 20, 21, 22, 25, 30]

percentiles = np.percentile(recovery_times, [10, 50, 90])

print(f"10th percentile: {percentiles[0]}")
print(f"50th percentile (median): {percentiles[1]}")
print(f"90th percentile: {percentiles[2]}")
