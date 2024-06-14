import numpy as np
from scipy import stats

purchase_amounts = [50, 20, 20, 30, 50, 60, 100, 30, 50, 20, 40, 60, 70, 80, 90, 20]

mean_purchase = np.mean(purchase_amounts)

mode_purchase, count = stats.mode(purchase_amounts)

print(f"Mean (average) purchase amount: ${mean_purchase:.2f}")
print(f"Mode of the purchase amounts: ${mode_purchase[0]} (appeared {count[0]} times)")

