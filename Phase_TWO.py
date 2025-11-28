

from pathlib import Path


cwd = Path.cwd() # Current working directory
print(cwd)



print(sum(seg24["seg_passengers"])-sum(seg23["seg_passengers"]))
print(sum(seg24["seg_passengers"]))
print(sum(seg23["seg_passengers"]))

print(max(seg24["seg_revenue_usd"]))
print(min(seg24["seg_revenue_usd"]))

seg24.sort_values("seg_revenue_usd",ascending=False,inplace=True)
print(seg24["seg_revenue_usd"].head(10))