import pandas as pd
import matplotlib as mt
cap23 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2024-01_2024-12.csv")

from pathlib import Path


cwd = Path.cwd() # Current working directory
print(cwd)


#Evolution of Passengers (difference of total passengers between 2024 and 2023)

print(sum(seg24["seg_passengers"])-sum(seg23["seg_passengers"]))
print(sum(seg24["seg_passengers"]))
print(sum(seg23["seg_passengers"]))


#Identify most profitable origins/destinations in 2024

seg24.sort_values("seg_revenue_usd",ascending=False,inplace=True)
print(seg24["seg_revenue_usd"].head(10)) #values
print(seg24["leg_origin"].head(10)) #origins
print(seg24["leg_destination"].head(10)) #destinations



#Load Factor

# merge the two lists and match corresponding routes and airlines and dates
merged23 = pd.merge(cap23, seg23, how="left", left_on=['origin', 'destination', 'operating_airline', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'operating_airline', 'year', 'month'])
merged24 = pd.merge(cap24, seg24, how="left", left_on=['origin', 'destination', 'operating_airline', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'operating_airline', 'year', 'month'])
# Calculate load factor
merged23['load_factor'] = merged23['seg_passengers'] / merged23['capacity']
merged24['load_factor'] = merged24['seg_passengers'] / merged24['capacity']

#Average load factor by origin for 2023
origin_grouped_23 = merged23.groupby("origin")
print(origin_grouped_23.agg({'load_factor':'mean'}))

#Average load factor by destination for 2023
dest_grouped_23 = merged23.groupby(["year","month"])
print(dest_grouped_23.agg({'load_factor':'mean'}))

#Average load factor by month for 2024
date_grouped_24 = merged24.groupby(["year","month"])
print(date_grouped_24.agg({'load_factor':'mean'}))



#Revenue per Passenger:

#Average revenue per passenger for 2023
seg23['revenue_per_passenger'] = seg23['seg_revenue_usd'] / seg23['seg_passengers']
print(seg23['revenue_per_passenger'].mean)

#Average revenue per passenger for 2024
seg24['revenue_per_passenger'] = seg24['seg_revenue_usd'] / seg24['seg_passengers']
print(seg24['revenue_per_passenger'].mean)