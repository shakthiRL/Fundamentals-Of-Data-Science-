order_data = {
  "OrderID": [1001, 1002, 1003, 1004, 1005],
  "CustomerID": [123, 456, 123, 789, 456],
  "ProductID": [34, 21, 56, 34, 21],
  "Quantity": [2, 1, 3, 1, 2],
  "TotalPrice": [20.00, 10.00, 42.00, 10.00, 25.00]
}
import pandas as pd

orders_df = pd.DataFrame(order_data)
print(orders_df.head())
print("\ninfo\n")
print(orders_df.info())
print("\ndes\n")
print(orders_df.describe())

total_sales=orders_df['TotalPrice'].sum()
avg_order_value=orders_df['TotalPrice'].mean()
print(f"Total Sales: ${total_sales}")
print("Average Order Value:",avg_order_value)
