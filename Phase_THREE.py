

import pandas as pd
import matplotlib as mt


cap23 = pd.read_csv("Python-Project-Milanamos-data/cap23Clean.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/cap24Clean.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/seg23Clean.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/seg24Clean.csv")
# print(len(cap23))
# seg23.sort_values("seg_revenue_usd",ascending=False,inplace=True)
#cap23.to_csv('cap23Clean.csv', index=False)
# merge the two lists and match corresponding routes and airlines and dates
merged23 = pd.merge(cap23, seg23, how="left", left_on=['origin', 'destination', 'operating_airline' ,'year', 'month'], right_on=['leg_origin', 'leg_destination', 'operating_airline', 'year', 'month'])
# Calculate load factor
merged23['load_factor'] = merged23['seg_passengers'] / merged23['capacity']
merged23 = merged23.replace([float('inf'), float('-inf')], pd.NA)
merged23 = merged23.dropna()
#merged23 = pd.DataFrame(cap23.groupby())
#merged23 = cap23.groupby(["origin", "destination", "capacity"], as_index=False).sum()
#this is incomplete
merged23.sort_values("load_factor",ascending=False,inplace=True)
merged23.to_csv('merged23Clean.csv', index=False)
print(len(merged23))
print(len(merged23[merged23['load_factor'] > 1.02]))
print(merged23.head(320))
# print(len(cap23))
#change