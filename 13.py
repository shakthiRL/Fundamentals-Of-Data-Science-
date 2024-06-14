import numpy as np
from scipy import stats

# Sample purchase amounts
purchase_amounts = [
    23.45, 35.50, 50.00, 23.45, 75.00, 100.00, 35.50, 23.45, 23.45, 150.00,
    200.00, 75.00, 50.00, 23.45, 23.45, 50.00, 35.50, 35.50, 100.00, 23.45
]

# Calculate the mean
mean_purchase_amount = np.mean(purchase_amounts)

# Identify the mode
mode_purchase_amount = stats.mode(purchase_amounts)

# Output the mean and mode
mean_purchase_amount, mode_purchase_amount.mode[0], mode_purchase_amount.count[0]
