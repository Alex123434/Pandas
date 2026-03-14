import pandas as pd

# ==========================================
# 1. READING & INSPECTING CSV FILES
# ==========================================

# The 'r' before the string stands for "raw string". 
# It tells Python to read the backslashes (\) exactly as they are, 
# which is essential for Windows file paths so they don't cause errors.
file_path = r"C:\Users\alexa\Panda-Basics\Pandas 101\train.csv"
df = pd.read_csv(file_path)

# --- Viewing the Data ---

# 1. Standard Print (Truncated)
# If the file is large, Pandas automatically hides the middle rows 
# and shows you just the first 5 and last 5 rows.
print("--- Standard Print ---")
print(df)

# 2. Print ALL Data
# .to_string() forces Pandas to print every single row and column. 
# WARNING: Be careful using this with massive datasets, or your terminal will be flooded!
print("\n--- Print Entire Dataset ---")
# print(df.to_string()) # Left commented out for safety

# ==========================================
# PRO-TIPS: Better ways to inspect new data
# ==========================================

# Print only the first 5 rows (perfect for a quick peek at the columns)
print("\n--- First 5 Rows ---")
print(df.head()) 

# Print only the first 10 rows
# print(df.head(10)) 

# Print only the last 5 rows
print("\n--- Last 5 Rows ---")
print(df.tail())

# Get a quick technical summary (shows column names, data types, and if any data is missing)
print("\n--- DataFrame Info ---")
print(df.info())

# Get quick math statistics for your number columns (average, min, max, etc.)
print("\n--- DataFrame Statistics ---")
print(df.describe())