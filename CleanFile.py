

import pandas as pd
import re

# Load the file
file_path = (r"C:\Users\Carly\Desktop\school\CS 488\team project\New File to work with\gov salaries.xlsx")
xls = pd.ExcelFile(file_path)

# Load the "Data" and "Job Titles Clean" sheets
data_df = xls.parse('Data')
titles_clean_df = xls.parse('Job Titles Clean')

# Create the mapping dictionary, ensuring all keys and values are strings
title_mapping = {str(wrong): str(correct) for wrong, correct in zip(titles_clean_df['Wrong'], titles_clean_df['Correct']) if pd.notna(wrong) and pd.notna(correct)}

# Function to clean up each job title
def clean_job_title(job_title):
    job_title = str(job_title)

    # Apply each replacement from the mapping
    for wrong, correct in title_mapping.items():
        if '&' in wrong:
            wrong = wrong.replace('&', 'and')
            correct = correct.replace('&', 'and')
        job_title = re.sub(rf'\b{re.escape(wrong)}\b', correct, job_title)

    # Handle "Insp" or "Inspe" based on their position
    job_title = re.sub(r'\b(Insp|Inspe)\b(?=\s+\w)', 'Inspections', job_title)  # "Insp"/"Inspe" before another word
    job_title = re.sub(r'\b(Insp|Inspe)\b$', 'Inspector', job_title)

    # Remove periods
    job_title = re.sub(r'\.\s*', ' ', job_title)

    # Replace multiple spaces with a single space
    job_title = re.sub(r'\s+', ' ', job_title).strip()

    # Capitalize each word in the job title
    job_title = ' '.join(word.capitalize() for word in job_title.split())

    return job_title

# Apply the function to the "Job Title" column and create a new column "Cleaned Job Titles"
data_df['Cleaned Job Titles'] = data_df['Job Title'].apply(clean_job_title)

# Save the updated file
data_df.to_excel('updated_excel_file.xlsx', sheet_name='Data', index=False)