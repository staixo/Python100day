import pandas as pd
datafile = "Python100day/Intermediate/Panda/weather_data.csv"
data = pd.read_csv(datafile)
print(data.head())
print(data.tail())