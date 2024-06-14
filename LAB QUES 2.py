import pandas as pd
import matplotlib.pyplot as plt

data = {
    'smoking': [10, 15, 8, 12, 20],  
    'lung_cancer_rates': [5, 8, 4, 6, 9]  
}

df = pd.DataFrame(data)

correlation_coefficient = df['smoking'].corr(df['lung_cancer_rates'])
print(f"Pearson's correlation coefficient: {correlation_coefficient:.2f}")

plt.scatter(df['smoking'], df['lung_cancer_rates'])
plt.xlabel('Smoking Habits')
plt.ylabel('Lung Cancer Rates')
plt.title('Scatter Plot: Smoking vs. Lung Cancer Rates')
plt.grid(True)
plt.show()
