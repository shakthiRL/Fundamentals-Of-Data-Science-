import numpy as np

# Sample response times in milliseconds (ms)
response_times = [
    102, 110, 150, 200, 250, 300, 350, 400, 450, 500,
    550, 600, 650, 700, 750, 800, 850, 900, 950, 1000
]

# Calculate the percentiles
percentiles = np.percentile(response_times, [25, 50, 75])

# Output the percentiles
percentiles_dict = {
    "25th Percentile": percentiles[0],
    "50th Percentile (Median)": percentiles[1],
    "75th Percentile": percentiles[2]
}

print(percentiles_dict)
