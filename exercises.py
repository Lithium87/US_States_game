import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250822.csv")
print(df)

color = df["Primary Fur Color"].value_counts()
print(color)

data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(df[df["Primary Fur Color"] == "Gray"]), len(df[df["Primary Fur Color"] == "Cinnamon"]), len(df[df["Primary Fur Color"] == "Black"])]
}
df2 = pd.DataFrame(data)
df2.to_csv("squirrel_count.csv")