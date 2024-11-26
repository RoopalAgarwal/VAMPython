# Find revenue / sales / profit of 2025 Amazon, Flipkart, MMT, OYO, Zomato by using 10 years data
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
revenue = [88.99 , 107.01, 135.99, 177.87, 232.89, 280.52, 386.06, 469.82, 514.00, 524.96]
profit = [0.24, 0.59, 2.37, 3.03, 10.07, 11.59, 21.33, 33.36, 2.87, 9.06]
# plt.scatter(year,revenue,profit,marker='s')
# plt.show()
futureDataProfit=np.poly1d(np.polyfit(year,profit,3))
print("Profit: ",futureDataProfit(2025))
print("r2_score of profit: ",r2_score(profit, futureDataProfit(year)))

futureDataRevenue =np.poly1d(np.polyfit(year,revenue,3))
print("Revenue: ",futureDataRevenue(2025))
print("r2_score of revenue: ",r2_score(revenue,futureDataRevenue(year)))
