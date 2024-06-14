import numpy as np

sales_data = np.array([
    [100, 150, 200],  
    [120, 180, 220],  
    [90, 130, 190]    
])

average_price = sales_data.mean()
print("Average price of all products sold:", average_price)
