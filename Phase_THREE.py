

import pandas as pd
import matplotlib as mt


cap23 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2024-01_2024-12.csv")

# seg24.sort_values("seg_revenue_usd",ascending=False,inplace=True)

# merge the two lists and match corresponding routes and airlines and dates
merged24 = pd.merge(cap24, seg24, how="left", left_on=['origin', 'destination', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'year', 'month'])
# Calculate load factor
merged24['load_factor'] = merged24['seg_passengers'] / merged24['capacity']

merged24 = pd.DataFrame(cap23.groupby())
#this is incomplete
merged24.sort_values("load_factor",ascending=False,inplace=True)
print(len(merged24))
print(len(merged24[merged24['load_factor'] > 1.2]))