import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Python100day/Intermediate/Panda/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data.head())
print(data['Primary Fur Color'].unique())
print(data['Primary Fur Color'].value_counts())
print(data.groupby(['Primary Fur Color'])['Primary Fur Color'].count())
fur_color = data['Primary Fur Color'].value_counts()
fur_color.plot(kind='bar')

fur_color.to_csv('Python100day/Intermediate/Panda/fur_color.csv',index=True)