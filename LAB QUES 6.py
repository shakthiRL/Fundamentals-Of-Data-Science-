import pandas as pd

property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location1', 'Location2', 'Location1', 'Location3', 'Location2'],
    'bedrooms': [3, 5, 4, 2, 6],
    'area_sqft': [2000, 3000, 2500, 1800, 3500],
    'listing_price': [500000, 750000, 600000, 450000, 800000]
})

average_listing_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("Average listing price per location:")
print(average_listing_price_per_location)

properties_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
print("\nNumber of properties with more than four bedrooms:")
print(properties_more_than_four_bedrooms)


property_with_largest_area = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nProperty with the largest area:")
print(property_with_largest_area)
