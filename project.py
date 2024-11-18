# Tomas Urena
# 11/08/2024
# Team Project 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gov salaries.csv', header = 0)

# preprocess the data
data['Year'] = data['Year'].astype(int)
data['Annual Wage'] = data['Annual Wage'].astype(float)

# trend analysis for Average Annual Wage
plt.figure(figsize = (12, 6))
wageByYear = data.groupby('Year')['Average Annual Wage'].mean()
plt.plot(wageByYear.index, wageByYear.values, marker = 'o')
plt.title("Average Annual Wage Progression (2016-2023)")
plt.xlabel("Year")
plt.ylabel("Average Annual Wage")
plt.grid(True)
plt.show()

# trend analysis for Number of Employees
plt.figure(figsize = (12, 6))
plt.plot(data['Year'], data['Number of Employees'], marker = 'o')
plt.title("Number of Employees Progression (2016-2023)")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.grid(True)
plt.show()