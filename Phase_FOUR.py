import pandas as pd
import matplotlib.pyplot as mt
cap23 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("Python-Project-Milanamos-data/CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("Python-Project-Milanamos-data/SEG_F_US_US_2024-01_2024-12.csv")

# merge the two lists and match corresponding routes and airlines and dates
merged23 = pd.merge(cap23, seg23, how="left", left_on=['origin', 'destination', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'year', 'month'])
merged24 = pd.merge(cap24, seg24, how="left", left_on=['origin', 'destination', 'year', 'month'], right_on=['leg_origin', 'leg_destination', 'year', 'month'])

#Bar chart for top 10 origin by revenue 2023
TopRevenue23 = merged23.sort_values("seg_revenue_usd",ascending=False).head(10)
#print(TopRevenue23)
#mt.bar(x=TopRevenue23['origin'], height=TopRevenue23['seg_revenue_usd'])
#mt.show()

#Bar chart for top 10 origin by revenue 2024
TopRevenue24 = merged24.sort_values("seg_revenue_usd",ascending=False).head(10)
#mt.bar(x=TopRevenue24['origin'], height=TopRevenue24['seg_revenue_usd'])
#mt.show()

#Bar chart for top 10 destination by revenue 2023
#mt.bar(x=TopRevenue23['destination'], height=TopRevenue23['seg_revenue_usd'])
#mt.show()

#Bar chart for top 10 destination by revenue 2024
#mt.bar(x=TopRevenue24['destination'], height=TopRevenue24['seg_revenue_usd'])
#mt.show()



#Line chart passenger evolution
date_grouped_24 = merged24.groupby(["year","month"])
mt.plot(x=date_grouped_24['month'],y=date_grouped_24['seg_passengers'])
mt.show()        



#Heatmap for load factor by origin/destination/period