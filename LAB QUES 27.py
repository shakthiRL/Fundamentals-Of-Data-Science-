import numpy as np
from scipy import stats

# Hypothetical conversion rate data (replace with actual data)
conversion_rate_A = np.array([0.2, 0.25, 0.3, 0.28, 0.22])  # Design A
conversion_rate_B = np.array([0.15, 0.18, 0.2, 0.19, 0.21])  # Design B

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Print results
print(f"Two-Sample T-Test Results:")
print(f"T-Statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

# Determine significance at alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("Conclusion: There is a statistically significant difference in the mean conversion rates between website designs A and B.")
else:
    print("Conclusion: There is no statistically significant difference in the mean conversion rates between website designs A and B.")
