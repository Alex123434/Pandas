import pandas as pd

data = [1, 2, 3, 98, 32, 54, 12]

series = pd.Series(data)

# Print an entire series
print(series)

# Print an element for a series

print(series.loc[1])
print(series.iloc[2])

# Update values in a series

series.loc[3] = 67

print(series)

# Filtering by values

print(series[series >= 50])

# You can do the same with dictionaries
# Write an example