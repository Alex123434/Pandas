import pandas as pd

# ==========================================
# 1. SELECTING & SLICING DATA
# ==========================================

# By setting index_col="blue", Pandas will use the "blue" column 
# as the row labels instead of the default 0, 1, 2, 3...
file_path = r"C:\Users\alexa\Panda-Basics\Pandas 101\train.csv"
df = pd.read_csv(file_path, index_col="blue")

print("--- Standard Print (Truncated) ---")
print(df.head()) # Using .head() for a cleaner output

# ==========================================
# --- SELECTING COLUMNS ---
# ==========================================

# 1. Select a Single Column
# This returns a Pandas "Series"
print("\n--- Single Column ('dual_sim') ---")
print(df["dual_sim"])

# print(df["dual_sim"].to_string()) # Un-comment to see all rows of this column

# 2. Select Multiple Columns
# Notice the DOUBLE brackets [[ ]]. The outer brackets tell Pandas we are 
# making a selection, and the inner brackets are the Python list of column names.
print("\n--- Multiple Columns ---")
print(df[["dual_sim", "battery_power"]])


# ==========================================
# --- SELECTING ROWS & COLUMNS TOGETHER ---
# ==========================================

# To select an integer row (using iloc) but keep specific column names, 
# the easiest way is to select the columns first, THEN use .iloc.

# 1. Select a Single Row + Specific Columns
print("\n--- Row 1200 for Specific Columns ---")
# Step 1: df[["battery_power", "dual_sim"]] isolates just those two columns.
# Step 2: .iloc[1200] grabs the row at integer position 1200 from that smaller table.
print(df[["battery_power", "dual_sim"]].iloc[1200])

# 2. Select a Range of Rows (Slicing) + Specific Columns
print("\n--- Rows 1200 to 1499 for Specific Columns ---")
# In Python slicing [1200:1500], it includes 1200 but stops *before* 1500.
print(df[["battery_power", "dual_sim"]].iloc[1200:1500])

# Pro-Tip: If you wanted to use .loc instead (searching by your "blue" index labels), 
# the syntax puts rows and columns in the same bracket separated by a comma:
# print(df.loc["my_blue_label", ["battery_power", "dual_sim"]])