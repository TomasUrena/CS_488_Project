# Tomas Urena
# 11/08/2024
# Team Project 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gov salaries.csv', header = 0)
print(data)

# preprocess_data
data['Year'] = data['Year'].astype(int)
data['Annual Wage'] = data['Annual Wage'].astype(float)

# trend_analysis
plt.figure(figsize=(12, 6))
avg_wage_per_year = data.groupby('Year')['Average Annual Wage'].mean()
plt.plot(avg_wage_per_year.index, avg_wage_per_year.values, marker='o')
plt.title("Average Annual Wage Progression (2016-2023)")
plt.xlabel("Year")
plt.ylabel("Average Annual Wage")
plt.grid(True)
plt.show()
