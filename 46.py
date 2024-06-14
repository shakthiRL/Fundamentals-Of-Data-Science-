from scipy import stats

# Example conversion rate data (replace with actual data)
conversion_rate_A = [0.25, 0.28, 0.31, 0.29, 0.26]
conversion_rate_B = [0.30, 0.32, 0.29, 0.27, 0.33]

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(conversion_rate_A, conversion_rate_B)

# Output the results
print(f"T-statistic: {t_statistic:.2f}")
print(f"P-value: {p_value:.4f}")

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and B.")
