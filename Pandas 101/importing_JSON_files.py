import pandas as pd
import json # Sometimes needed for the pro-tip below!

# ==========================================
# 1. READING & INSPECTING JSON FILES
# ==========================================

# Load a standard, "flat" JSON file into a DataFrame
file_path = r"C:\Users\alexa\Panda-Basics\Pandas 101\samsung_earbuds.json"
df = pd.read_json(file_path)

# Print the DataFrame (Pandas will truncate it if it's too long, just like a CSV)
print("--- Standard JSON Print ---")
print(df)

# Just like with CSVs, you can use .head(), .info(), and .describe() here!
print("\n--- Quick Peek at the First 5 Rows ---")
print(df.head())


# ==========================================
# PRO-TIPS: Handling "Nested" (Messy) JSONs
# ==========================================
# If your JSON file has dictionaries inside of dictionaries, pd.read_json() 
# might just cram an entire dictionary into a single DataFrame cell. 
# To fix this and "flatten" the data into proper columns, use pd.json_normalize().

# Example of how to flatten a messy JSON (commented out for future reference):

# Step 1: Open the file using Python's built-in json module
# with open(file_path) as f:
#     raw_json_data = json.load(f)

# Step 2: Use json_normalize to flatten the nested data into neat columns
# flat_df = pd.json_normalize(raw_json_data)
# print("\n--- Flattened JSON Data ---")
# print(flat_df.head())