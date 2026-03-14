import pandas as pd

data = r"C:\Users\alexa\Panda-Basics\Pandas 101\train.csv"
df = pd.read_csv(data)

# Applies to whole df

# print(df.mean(numeric_only = True))

# print(df.sum(numeric_only = True))

# print(df.min(numeric_only = True))

# print(df.max(numeric_only = True))

# print(df.count())

# Applies to a single column

print(df["battery_power"].mean(numeric_only = True))

print(df["battery_power"].sum(numeric_only = True))

print(df["battery_power"].min(numeric_only = True))

print(df["battery_power"].max(numeric_only = True))

print(df["battery_power"].count())


# Group by

group = df.groupby("dual_sim")

print(group["battery_power"].mean())
