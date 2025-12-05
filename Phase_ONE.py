import pandas as pd
import matplotlib as mt
cap23 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2024-01_2024-12.csv")

#phase 1:
#Display top of each dataframe
print(cap23.head())
print(cap24.head())
print(seg23.head())
print(seg24.head())

#Display descriptive stats
print('Minimum: ' + str(seg24["seg_revenue_usd"].min()) + ' Maximum: ' + str(seg24["seg_revenue_usd"].max()) + ' Mean: ' + str(seg24["seg_revenue_usd"].mean()))

