# Import necessary libraries
import pandas as pd

# 1. Read and write data using Pandas

# Reading data from a CSV file
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'  # Sample CSV file
data = pd.read_csv(url)

# Display the first few rows of the dataset
print(data.head())

# Writing data to a CSV file (locally)
data.to_csv('airtravel_output.csv', index=False)

# 2. Perform data cleaning and preprocessing tasks

# Example of handling missing data

# Adding some NaN values for demonstration
data.loc[0, 'JAN'] = None
data.loc[1, 'FEB'] = None

# Dropping rows with missing values
cleaned_data = data.dropna()
print(cleaned_data.head())

# Filling missing values with the mean of the column
filled_data = data.fillna(data.mean(numeric_only=True))
print(filled_data.head())

# 3. Manipulate data using Pandas data structures

# Creating a Pandas Series
series_data = pd.Series([100, 200, 300, 400], index=['a', 'b', 'c', 'd'])
print(series_data)

# Creating a Pandas DataFrame
df_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
})
print(df_data)

# Selecting specific rows/columns using loc and iloc
print(df_data.loc[0])  # Select by index label
print(df_data.iloc[1])  # Select by index position

# 4. Apply data analysis techniques with Pandas

# Descriptive statistics
print(data.describe())

# Grouping and aggregation
grouped_data = data.groupby('Year').sum()
print(grouped_data)

# Filtering data
filtered_data = data[data['JAN'] > 340]  # Example: Filtering rows where JAN > 340
print(filtered_data)

# Saving cleaned and processed data back to a CSV
filled_data.to_csv('cleaned_airtravel_output.csv', index=False)
