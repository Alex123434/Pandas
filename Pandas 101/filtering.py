import pandas as pd

data = r"C:\Users\alexa\Panda-Basics\Pandas 101\train.csv"
df = pd.read_csv(data)


battery_power = df[df["battery_power"] >= 1000]
print(battery_power)

has_dual_sim = df[df["dual_sim"] == True]
print(has_dual_sim)

clock_battery = df[(df["clock_speed"] == 2.5) & 
                 (df["battery_power"] > 500)]

print(clock_battery)