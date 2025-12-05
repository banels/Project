

import pandas as pd
import matplotlib as mt


cap23 = pd.read_csv("Python-Project-Milanamos-data/cap23Clean.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/cap24Clean.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/seg23Clean.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/seg24Clean.csv")
print(len(cap23))
# seg23.sort_values("seg_revenue_usd",ascending=False,inplace=True)
cap23 = cap23.groupby(["origin", "destination", "operating_airline", "year", "month"], as_index=False).sum()
cap23.to_csv('cap23Clean.csv', index=False)
# merge the two lists and match corresponding routes and airlines and dates
#merged24 = pd.merge(cap24, seg24, how="left", left_on=['origin', 'destination', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'year', 'month'])
# Calculate load factor
##merged24['load_factor'] = merged24['seg_passengers'] / merged24['capacity']

#merged24 = pd.DataFrame(cap23.groupby())
#merged24 = cap23.groupby(["origin", "destination", "capacity"], as_index=False).sum()
#this is incomplete
#merged24.sort_values("load_factor",ascending=False,inplace=True)
#merged24.to_csv('merged24Clean.csv', index=False)
#print(len(seg23))
#print(len(merged24[merged24['load_factor'] > 1.2]))
#print(merged24.head(425))
print(len(cap23))
#change