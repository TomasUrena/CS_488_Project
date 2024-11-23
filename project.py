# Tomas Urena
# 11/08/2024
# Team Project 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gov salaries_Cleaned.csv', header = 0)

# preprocess the data
data['Year'] = data['Year'].astype(int)
data['Annual Wage'] = data['Annual Wage'].astype(float)

# trend analysis for Annual Wage
plt.figure(figsize = (12, 6))
wageByYear = data.groupby('Year')['Annual Wage'].mean()
plt.plot(wageByYear.index, wageByYear.values, marker = 'o')
plt.title("Average Annual Wage Progression (2016-2023)")
plt.xlabel("Year")
plt.ylabel("Average Annual Wage")
plt.grid(True)
plt.show()

# trend analysis for Number of Employees
plt.figure(figsize = (12, 6))
numEmps = data.groupby('Year')['Number of Employees'].max()
plt.plot(numEmps.index, numEmps.values, marker = 'o')
plt.title("Number of Employees Progression (2016-2023)")
plt.xlabel("Year")
plt.ylabel("Employees")
plt.grid(True)
plt.show()

print(data.describe())
print()

# Contract Type 
plt.figure(figsize = (12, 6))
contractType = data.groupby('Contract Type')['Annual Wage'].mean()
plt.bar(contractType.index, contractType.values)
plt.title("Average Annual Wage By Contract Type")
plt.xlabel("Contract Types")
plt.ylabel("Average Annual Wage")
plt.tight_layout()
plt.show()

# Cleaned Job Titles NOT FINISHED 
plt.figure(figsize = (12, 6))
cjt = data.groupby('Cleaned Job Titles')['Annual Wage'].mean()
plt.bar(cjt.index, cjt.values)
plt.title("Average Annual Wage By Job Titles")
plt.xlabel("Job Titles")
plt.ylabel("Average Annual Wage")
plt.tight_layout()
plt.show()

# Role NOT FINISHED 
plt.figure(figsize = (12, 6))
role = data.groupby('Role')['Annual Wage'].mean()
plt.bar(role.index, role.values)
plt.title("Average Annual Wage By Role")
plt.xlabel("Roles")
plt.ylabel("Average Annual Wage")
plt.tight_layout()
plt.show()

# Department NOT FINISHED 
plt.figure(figsize = (12, 6))
department = data.groupby('Department')['Annual Wage'].mean()
plt.bar(department.index, department.values)
plt.title("Average Annual Wage By Department")
plt.xlabel("Department")
plt.ylabel("Average Annual Wage")
plt.tight_layout()
plt.show()

# Area of Governance  
plt.figure(figsize = (12, 6))
governace = data.groupby('Area of Governance')['Annual Wage'].mean()
plt.bar(governace.index, governace.values)
plt.title("Average Annual Wage By Area of Governance")
plt.xlabel("Area of Governance")
plt.ylabel("Average Annual Wage")
plt.tight_layout()
plt.show()
