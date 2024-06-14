import numpy as np

# Sample recovery times in days
recovery_times = [
    5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24
]

# Calculate the percentiles
percentiles = np.percentile(recovery_times, [10, 50, 90])

# Output the percentiles
percentiles_dict = {
    "10th Percentile": percentiles[0],
    "50th Percentile (Median)": percentiles[1],
    "90th Percentile": percentiles[2]
}

percentiles_dict
