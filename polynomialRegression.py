# Polynomial Regression:- r2_score ~= 1 -> best
#                         r2_score ~= 0 -> bad

import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

age = [40,20,35,50,60,30,70,80]
salary = [20000, 40000, 18000, 15000, 12000, 25000, 35000, 50000]
# plt.scatter(age, salary, marker='*')
# plt.show()
futureSalary=np.poly1d(np.polyfit(age,salary,3))
print(futureSalary(55))
print(r2_score(salary,futureSalary(age)))