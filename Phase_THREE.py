

import pandas as pd
import matplotlib as mt


cap23 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2024-01_2024-12.csv")

# seg24.sort_values("seg_revenue_usd",ascending=False,inplace=True)

# merge the two lists and match corresponding routes and airlines and dates
merged23 = pd.merge(cap23, seg23, how="left", left_on=['origin', 'destination', 'operating_airline', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'operating_airline', 'year', 'month'])
# Calculate load factor
merged23['load_factor'] = merged23['seg_passengers'] / merged23['capacity']


#this is incomplete
merged23.sort_values("load_factor",ascending=True,inplace=True)

print(merged23['load_factor'].head)