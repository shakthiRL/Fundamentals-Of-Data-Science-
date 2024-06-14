import numpy as np

response_times = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

percentiles = np.percentile(response_times, [25, 50, 75])

print(f"25th percentile: {percentiles[0]}")
print(f"50th percentile (median): {percentiles[1]}")
print(f"75th percentile: {percentiles[2]}")
