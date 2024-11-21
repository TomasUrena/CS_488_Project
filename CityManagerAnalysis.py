import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r"C:\Users\Carly\Desktop\school\CS 488\team project\New File to work with\gov salaries_Cleaned.xlsx", sheet_name='Data')

data = data.fillna(0)



# Filter data for City Manager
city_manager_data = data[data['Cleaned Job Titles'] == 'City Manager']

# Sort by year
city_manager_data = city_manager_data.sort_values(by='Year')

# Calculate annual salary increases for the City Manager
city_manager_data['Salary Increase ($)'] = city_manager_data['Annual Wage'].diff()
city_manager_data['Salary Increase (%)'] = city_manager_data['Annual Wage'].pct_change() * 100

# Format the data for display
table_data = city_manager_data[['Year', 'Annual Wage', 'Salary Increase ($)', 'Salary Increase (%)']].copy()
table_data['Year'] = table_data['Year'].astype(int)
table_data['Annual Wage'] = table_data['Annual Wage'].map('{:.0f}'.format)
table_data['Salary Increase ($)'] = table_data['Salary Increase ($)'].map('{:.0f}'.format)
table_data['Salary Increase (%)'] = table_data['Salary Increase (%)'].map('{:.0f}'.format)

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 5))

# Hide the axes
ax.axis('off')
ax.axis('tight')

# Create a table in the plot
ax.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    loc='center',
    cellLoc='center'
)

# Add a title and show the plot
plt.title("Annual Salary Increases for the City Manager", fontsize=14, pad=10)
plt.tight_layout()
plt.show()





# Calculate overall average annual wage by year
average_wages_by_year = data[['Year', 'Average Annual Wage']].drop_duplicates()

# Merge the City Manager's data with the overall average wages
comparison_data = city_manager_data.merge(
    average_wages_by_year, on='Year', suffixes=('', ' (Overall Average)')
)

# Calculate the percent difference
comparison_data['Percent Difference (%)'] = (
    (comparison_data['Annual Wage'] - comparison_data['Average Annual Wage']) /
    comparison_data['Average Annual Wage'] * 100
)


# Format the data to remove decimals
table_data = comparison_data[['Year', 'Annual Wage', 'Average Annual Wage', 'Percent Difference (%)']].copy()
table_data['Year'] = table_data['Year'].astype(int)
table_data['Annual Wage'] = table_data['Annual Wage'].map('{:.0f}'.format)
table_data['Average Annual Wage'] = table_data['Average Annual Wage'].map('{:.0f}'.format)  #
table_data['Percent Difference (%)'] = table_data['Percent Difference (%)'].map('{:.0f}'.format)  

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 4))

# Hide the axes
ax.axis('off')
ax.axis('tight')

# Create a table in the plot
ax.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    loc='center',
    cellLoc='center'
)

# Adjust layout and display the figure
plt.title("Comparison of City Manager's Annual Wage to Average Annual Wage", fontsize=14)
plt.tight_layout()
plt.show()






# Extract years and average annual wages for the plot
years = average_wages_by_year['Year']
overall_avg_wages = average_wages_by_year['Average Annual Wage']

# Plotting
plt.figure(figsize=(10, 6))

# Plot City Manager's salary
plt.plot(city_manager_data['Year'], city_manager_data['Annual Wage'], label='City Manager Salary', marker='o')

# Plot Overall Average Salary
plt.plot(years, overall_avg_wages, label='Overall Average Salary', linestyle='--')

# Add labels and title
plt.title('City Manager Salary vs. Overall Average Salary', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Salary ($)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()




# Calculate the percentage increase/decrease in salary
city_manager_data['Salary Increase (%)'] = city_manager_data['Annual Wage'].pct_change() * 100

# Identify years with either a 10% increase or decrease in salary
anomalies = city_manager_data[
    (city_manager_data['Salary Increase (%)'] > 10) | (city_manager_data['Salary Increase (%)'] < -10)
]

# Create a Matplotlib figure
table_data = anomalies[['Year', 'Annual Wage', 'Salary Increase (%)']].copy()

# Format Year and Annual Wage with no decimals
table_data['Year'] = table_data['Year'].astype(int)
table_data['Annual Wage'] = table_data['Annual Wage'].map('{:.0f}'.format)

# Format Salary Increase (%) with two decimals
table_data['Salary Increase (%)'] = table_data['Salary Increase (%)'].map('{:.2f}'.format)

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(7, 3))

# Hide axes
ax.axis('off')
ax.axis('tight')

# Create a table in the plot
table = ax.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    cellLoc='center',
    loc='center'
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)  # Adjust font size
table.auto_set_column_width(col=list(range(len(table_data.columns))))  # Adjust column width

# Add a title closer to the table
plt.title("Years with 10% or More Increase/Decrease in Salary for City Manager", fontsize=14, pad=10)

# Use tight layout to adjust spacing
plt.tight_layout(rect=[0, 0, 1, 0.85])

# Display the table
plt.show()






