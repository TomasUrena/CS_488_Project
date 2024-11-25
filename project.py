# Tomas Urena
# 11/08/2024
# Team Project 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gov salaries_Cleaned.csv', header = 0)

print(data.describe())
print()

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

# Contract Type: Average Wage 
plt.figure(figsize = (12, 6))
plt.subplot(2,1,1)
contractType = data.groupby('Contract Type')['Annual Wage'].mean()
plt.bar(contractType.index, contractType.values)
plt.title("Average Annual Wage By Contract Type")
plt.xlabel("Contract Types")
plt.ylabel("Average Annual Wage")
plt.tight_layout()

# Contract Type: Employee Count 
plt.subplot(2,1,2)
contractType = data.groupby('Contract Type')['Contract Type'].count()
plt.bar(contractType.index, contractType.values)
plt.title("Employee Count By Contract Type")
plt.xlabel("Contract Types")
plt.ylabel("Number Of Employees")
plt.tight_layout()
plt.show()

# Cleaned Job Titles: Average Wage 
plt.figure(figsize = (12, 6))
plt.subplot(2,1,1)
cjt = data.groupby('Cleaned Job Titles')['Annual Wage'].mean()
cityMan = cjt['City Manager']
cjt = cjt.drop('City Manager')
plt.bar('City Manager', cityMan, color = 'blue', label = 'City Manager') 
plt.bar(cjt.index, cjt.values, color = 'grey', label = 'Other') 
plt.title("Average Annual Wage By Job Titles")
plt.xlabel("Job Titles")
plt.ylabel("Average Annual Wage")
plt.xticks([], [])
plt.legend()
plt.tight_layout()

# Cleaned Job Titles: Employee Count 
plt.subplot(2,1,2)
cjt = data.groupby('Cleaned Job Titles')['Cleaned Job Titles'].count()
cityMan = cjt['City Manager']
cjt = cjt.drop('City Manager')
plt.bar('City Manager', cityMan, color = 'blue', label = 'City Manager') 
plt.bar(cjt.index, cjt.values, color = 'grey', label = 'Other') 
plt.title("Employee CountBy Job Titles")
plt.xlabel("Job Titles")
plt.ylabel("Number Of Employees")
plt.xticks([], [])
plt.legend()
plt.tight_layout()
plt.show()

# Role: Employee Count // NOT FINISHED 
plt.figure(figsize = (12, 6))
role = data.groupby('Role')['Role'].count()
plt.bar(role.index, role.values)
plt.title("Employee Count By Role")
plt.xlabel("Roles")
plt.ylabel("Number Of Employees")
plt.xticks(rotation = 90, ha = 'right')
plt.tight_layout()
plt.show()

# Department: Average Wage 
plt.figure(figsize = (8, 8))
plt.subplot(2,1,1)
department = data.groupby('Department')['Annual Wage'].mean()
plt.bar(department.index, department.values)
plt.title("Average Annual Wage By Department")
plt.xlabel("Department")
plt.ylabel("Average Annual Wage")
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()

# Department: Employee Count  
plt.subplot(2,1,2)
department = data.groupby('Department')['Department'].count()
plt.bar(department.index, department.values)
plt.title("Employee Count By Department")
plt.xlabel("Department")
plt.ylabel("Number Of Employees")
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()

# Area of Governance: Average Wage  
plt.figure(figsize = (12, 6))
plt.subplot(2,1,1)
governace = data.groupby('Area of Governance')['Annual Wage'].mean()
plt.bar(governace.index, governace.values)
plt.title("Average Annual Wage By Area of Governance")
plt.xlabel("Area of Governance")
plt.ylabel("Average Annual Wage")
plt.tight_layout()

# Area of Governance: Employee Count 
plt.subplot(2,1,2)
governace = data.groupby('Area of Governance')['Area of Governance'].count()
plt.bar(governace.index, governace.values)
plt.title("Employee Count By Area of Governance")
plt.xlabel("Area of Governance")
plt.ylabel("Number Of Employees")
plt.tight_layout()
plt.show()
