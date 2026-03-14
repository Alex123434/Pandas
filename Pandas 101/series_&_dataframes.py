import pandas as pd

# ==========================================
# 1. PANDAS SERIES (1-Dimensional Data)
# ==========================================

data = [1, 2, 3, 98, 32, 54, 12]
series = pd.Series(data)

# Print an entire series
print("--- Entire Series ---")
print(series)

# Print specific elements
# Note: .loc[] searches by the index label, .iloc[] searches by integer position.
# Because we didn't specify custom labels, they work similarly here.
print("\n--- Selecting Elements ---")
print("Element at label 1:", series.loc[1]) 
print("Element at position 2:", series.iloc[2])

# Update values in a series
series.loc[3] = 67
print("\n--- Series after updating index 3 to 67 ---")
print(series)

# Filtering by values
print("\n--- Filtering values >= 50 ---")
print(series[series >= 50])


# --- Creating a Series from a Dictionary ---
# Keys automatically become the index labels, and values become the data.
print("\n--- Series from a Dictionary ---")
calories = {"day1": 420, "day2": 380, "day3": 390}
dict_series = pd.Series(calories)
print(dict_series)
print("Value for day2:", dict_series.loc["day2"]) # Using .loc with the string index


# ==========================================
# 2. PANDAS DATAFRAMES (2-Dimensional Data)
# ==========================================

df_data = {
    "Name": ["Jones", "Pedro", "Jessica"],
    "Age": [30, 67, 21]
}

# Creating a DataFrame with custom row indices
df = pd.DataFrame(df_data, index=["Emp1", "Emp2", "Emp3"])

print("\n--- Entire DataFrame ---")
print(df)

# Locating Rows
# .loc[] uses the explicit label name we gave it.
print("\n--- Selecting row by label (loc) ---")
print(df.loc["Emp1"])

# .iloc[] uses the numerical index (0-based), ignoring custom labels.
print("\n--- Selecting row by position (iloc) ---")
print(df.iloc[2])

# Add a new column
# The list must have the same number of items as the DataFrame has rows.
df["Position"] = ["Trainer", "Unassigned", "Escort"]
print("\n--- DataFrame with new 'Position' column ---")
print(df)

# Add a single new row
# We create a new small DataFrame and concatenate it to the existing one.
new_row = pd.DataFrame(
    [{"Name": "Feijoo", "Age": 34, "Position": "General"}], 
    index=["Emp4"]
)
df = pd.concat([df, new_row])

# Add multiple new rows
new_rows = pd.DataFrame(
    [
        {"Name": "Alex", "Age": 28, "Position": "Analyst"},
        {"Name": "Katie", "Age": 19, "Position": "Manager"}
    ], 
    index=["Emp5", "Emp6"]
)
df = pd.concat([df, new_rows])

print("\n--- DataFrame after adding new rows ---")
print(df)