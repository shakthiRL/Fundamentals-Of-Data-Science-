import pandas as pd
import matplotlib.pyplot as plt

data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [25, 30, 22, 35, 40, 22, 30, 25, 28, 35],
    'purchase_amount': [200, 150, 100, 300, 250, 150, 200, 100, 300, 250],
    'purchase_date': pd.date_range(start='2024-05-01', periods=10)
}

sales_data = pd.DataFrame(data)

sales_data['age'] = sales_data['age'].astype(int)

age_distribution = sales_data['age'].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(age_distribution)

plt.figure(figsize=(10, 5))
age_distribution.plot(kind='bar', color='skyblue')
plt.title('Frequency Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
