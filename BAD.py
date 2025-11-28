import pandas as pd
import matplotlib as mt
cap23 = pd.read_csv("BigAhhDati\Python-Project-Milanamos-data\CAP_US_US_2023-01_2023-12.csv")
cap24 = pd.read_csv("BigAhhDati\Python-Project-Milanamos-data\CAP_US_US_2024-01_2024-12.csv")
seg23 = pd.read_csv("BigAhhDati\Python-Project-Milanamos-data\SEG_F_US_US_2023-01_2023-12.csv")
seg24 = pd.read_csv("BigAhhDati\Python-Project-Milanamos-data\SEG_F_US_US_2024-01_2024-12.csv")

#change

print(sum(seg24["seg_passengers"])-sum(seg23["seg_passengers"]))
print(sum(seg24["seg_passengers"]))
print(sum(seg23["seg_passengers"]))

print(max(seg24["seg_revenue_usd"]))
print(min(seg24["seg_revenue_usd"]))

seg24.sort_values("seg_revenue_usd",ascending=False,inplace=True)
print(seg24["seg_revenue_usd"].head(10))