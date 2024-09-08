import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file

file_path ="C:\Users\PRIYANSHU\Downloads\Machine Learning A-Z (Codes and Datasets)-20231217T211344Z-001\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 4 - Simple Linear Regression\Python\Salary_Data.csv"

 

# Read the CSV file into a pandas DataFrame

df = pd.read_csv(file_path)

 

# Print the first 5 lines (+header) of the CSV file

print("First 5 Lines:")

print(df.head(5))

 

# Print the last 5 lines (+header) of the CSV file

print("\nLast 5 Lines:")

print(df.tail(5))