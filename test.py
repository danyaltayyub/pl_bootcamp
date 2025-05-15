import pandas as pd
import numpy as np

file_path = '/home/purelogics-2057/bootcamp/hourly_weather_10_days.csv'

df = pd.read_csv(file_path)


temp = df['temperature_C']
temp= temp.dropna()

print (temp)